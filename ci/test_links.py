import itertools
import pathlib
import re
from dataclasses import dataclass, field
from io import StringIO
from types import MappingProxyType
from typing import Iterable

import mistune
import pytest
from lxml import etree

# ../README.md  (relative to current file)
README_FILE_PATH = pathlib.Path(__file__).parents[1] / "README.md"

SKIP_HEADER_LINK_CHECKS = frozenset(("links", "Table of Contents"))

CHECK_HEADER_LINKS_UP_TO_LEVEL = 3

SKIP_HEADER_SORT_CHECKS = frozenset(
    ("links", "Prelude", "Other Lists", "Table of Contents")
)

SKIP_LINK_SORT_CHECKS = MappingProxyType(
    {"Table of Contents": frozenset(("Prelude", "Other Lists"))}
)


@dataclass(frozen=True)
class Header:
    text: str
    level: int

    slug: str


@dataclass(frozen=True)
class Link:
    # only use url for hashing and comparison
    # -- we use this to deduplicate links for accessing them
    url: str = field(compare=True, hash=True)
    title: str = field(compare=False, hash=False)
    text: str = field(compare=False, hash=False)

    header: Header | None = field(compare=False, hash=False)


@dataclass(frozen=True)
class LinkList:
    header: Header
    links: list[Link]


class StructuredRenderer(mistune.Renderer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._headers: list[Header] = []
        self._links: list[Link] = []

        self._link_lists: list[LinkList] = []

    @property
    def headers(self):
        return self._headers

    @property
    def links(self):
        return self._links

    @property
    def link_lists(self):
        return self._link_lists

    def header(self, text, level, raw=None):
        slug = github_slugify(text)
        header = Header(text, level, slug=slug)

        self._headers.append(header)

        return super().header(text, level, raw=raw)

    def link(self, link, title, text):
        self._register_link(link, title or "", text)

        return super().link(link, title, text)

    def list(self, body, ordered=True):
        # The way the mistune parser works is that this is called
        # AFTER a list ends, with HTML body as string.
        # We re-parse the HTML and create Link objects
        # corresponding to HTML tags.

        # call super here to have well-formed HTML
        result = super().list(body, ordered=ordered)

        tree = etree.parse(StringIO(result))

        # we want top-level ul lists,
        # and in each list element (li), only the first link (a)
        # (list elements may contain more than one link)
        a_tags = tree.xpath("/ul/li/a[1]")
        current_header = self._headers[-1]

        # don't bother with looking up existing links, just create new objects
        links = [
            Link(
                url=tag.attrib["href"],
                title=tag.attrib.get("title", ""),
                text=tag.text,
                header=current_header,
            )
            for tag in a_tags
        ]

        link_list = LinkList(header=current_header, links=links)
        self._link_lists.append(link_list)

        return result

    def image(self, src, title, text):
        self._register_link(src, title, text)

        return super().image(src, title, text)

    def _register_link(self, url, title, text):
        # markdown escaping messes up underscores in links
        normalized_url = url.replace(r"\_", "_")

        link = Link(normalized_url, title, text, header=self._headers[-1])
        self._links.append(link)


def github_slugify(text: str):
    """
    >>> github_slugify("Test")
    'test'
    >>> github_slugify("Python stuff")
    'python-stuff'
    >>> github_slugify("Something / Other")
    'something--other'
    >>> github_slugify("Hello, World & Other Famous Sentences")
    'hello-world--other-famous-sentences'
    """
    # probably incomplete, but gets the job done for my purposes
    spaces_as_dashes = text.lower().replace(" ", "-")

    return re.sub(r"[^a-z0-9-]", "", spaces_as_dashes)


def assert_sorted(iterable: Iterable, message: str = ""):
    """
    Assert whether the iterable is sorted. Consumes the iterable.

    >>> assert_sorted([1, 2, 3])
    >>> assert_sorted([3, 7, 1], "not sorted")  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    AssertionError: not sorted
    """
    assert list(iterable) == sorted(iterable), message


def assert_attr_sorted(
    iterable: Iterable,
    attr: str,
    message: str = "",
    casefold: bool = True,
    alnum_first: bool = True,
):
    attrs = (getattr(obj, attr) for obj in iterable)
    normalized_attrs = [attr.casefold() if casefold else attr for attr in attrs]

    if alnum_first:
        normalized_attrs = [
            attr[1:] if (alnum_first and not attr[0].isalnum()) else attr
            for attr in normalized_attrs
        ]

    assert_sorted(normalized_attrs, message=message)


@pytest.fixture(scope="session")
def renderer() -> StructuredRenderer:
    rend = StructuredRenderer()

    with README_FILE_PATH.open() as f:
        md = mistune.Markdown(renderer=rend)
        md.render(f.read())

    return rend


@pytest.fixture(scope="session")
def internal_links(renderer: StructuredRenderer) -> list[Link]:
    return [link for link in renderer.links if link.url.startswith("#")]


@pytest.fixture(scope="session")
def headers(renderer: StructuredRenderer) -> list[Header]:
    return renderer.headers


@pytest.fixture(scope="session")
def link_lists(renderer: StructuredRenderer) -> list[LinkList]:
    return renderer.link_lists


def test_internal_links_are_all_valid(internal_links, headers):
    slugs = {header.slug for header in headers}

    for link in internal_links:
        anchor = link.url
        slug = anchor.lstrip("#")

        assert slug in slugs


def test_all_headers_are_linked_to(internal_links, headers):
    link_slugs = {link.url.lstrip("#") for link in internal_links}
    header_slugs = {
        header.slug
        for header in headers
        if header.text not in SKIP_HEADER_LINK_CHECKS
        and header.level <= CHECK_HEADER_LINKS_UP_TO_LEVEL
    }

    assert link_slugs == header_slugs, "Missing or spurious header link"


def test_second_level_headers_are_sorted(headers):
    second_level_headers = [
        header
        for header in headers
        if header.level == 2 and header.text not in SKIP_HEADER_SORT_CHECKS
    ]

    assert_attr_sorted(second_level_headers, "text", "2nd level headers not sorted")


def test_third_level_headers_are_sorted(headers):
    headers_iter = iter(headers)

    for header in headers_iter:
        group = []

        for third_level in itertools.takewhile(lambda h: h.level == 3, headers_iter):
            group.append(third_level)

        assert_attr_sorted(group, "text", f"3rd level header not sorted: {header}")


def test_links_are_sorted_in_lists(link_lists):
    for link_list in link_lists:
        header = link_list.header

        if header.level > CHECK_HEADER_LINKS_UP_TO_LEVEL:
            continue

        filtered_links = [
            link
            for link in link_list.links
            if link.text not in SKIP_LINK_SORT_CHECKS.get(header.text, {})
        ]

        assert_attr_sorted(
            filtered_links, "text", f"Links not sorted in a list under {header}"
        )
