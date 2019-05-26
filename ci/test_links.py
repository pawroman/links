import asyncio
import itertools
import pathlib
import re

from dataclasses import dataclass, field
from typing import Iterable, List, Optional

import aiohttp
import mistune
import pytest


# ../README.md  (relative to current file)
README_FILE_PATH = pathlib.Path(__file__).parents[1] / "README.md"

SKIP_HEADER_LINK_CHECKS = frozenset(("links", "Table of Contents"))

CHECK_HEADER_LINKS_UP_TO_LEVEL = 3

SKIP_HEADER_SORT_CHECKS = frozenset(
    ("links", "Table of Contents", "Prelude", "Other Lists")
)

IGNORE_ERRORS_FOR_URLS = frozenset(
    (
        # Travis CI gets 403 Forbidden here :(
        "https://vimeo.com/293912618/5ccecc85d4",
        "https://webcache.googleusercontent.com/search?q=cache:dEddeFq1R_gJ:https://speice.io/2019/02/understanding-allocations-in-rust.html",
    )
)

DEFAULT_TIMEOUT_SECONDS = 40
DEFAULT_TIMEOUT = aiohttp.ClientTimeout(total=DEFAULT_TIMEOUT_SECONDS)


@dataclass(frozen=True)
class Header:
    text: str
    level: int

    slug: str


class MarkdownList:
    pass


class ListItem:
    pass


@dataclass(frozen=True)
class Link:
    # only use url for hashing and comparison
    # -- we use this to deduplicate links for accessing them
    url: str = field(compare=True, hash=True)
    title: str = field(compare=False, hash=False)
    text: str = field(compare=False, hash=False)

    header: Optional[Header] = field(compare=False, hash=False)
    list: Optional[MarkdownList] = field(compare=False, hash=False)
    list_item: Optional[ListItem] = field(compare=False, hash=False)


class StructuredRenderer(mistune.Renderer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._current_list: Optional[List] = None
        self._current_list_item: Optional[ListItem] = None

        self._headers: List[Header] = []
        self._links: List[Link] = []

    @property
    def headers(self):
        return self._headers

    @property
    def links(self):
        return self._links

    def header(self, text, level, raw=None):
        slug = github_slugify(text)
        header = Header(text, level, slug=slug)

        self._headers.append(header)

        return super().header(text, level, raw=raw)

    def link(self, link, title, text):
        self._register_link(link, title, text)

        return super().link(link, title, text)

    def list(self, body, ordered=True):
        self._current_list = MarkdownList()

        return super().list(body, ordered=ordered)

    def list_item(self, text):
        self._current_list_item = ListItem()

        return super().list_item(text)

    def image(self, src, title, text):
        self._register_link(src, title, text)

        return super().image(src, title, text)

    def _register_link(self, url, title, text):
        # markdown escaping messes up underscores in links
        normalized_url = url.replace(r"\_", "_")

        link = Link(
            normalized_url,
            title,
            text,
            header=self._headers[-1],
            list=self._current_list,
            list_item=self._current_list_item,
        )
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
    iterable: Iterable, attr: str, message: str = "", casefold: bool = True
):
    attrs = (getattr(obj, attr) for obj in iterable)
    normalized_attrs = [attr.casefold() if casefold else attr for attr in attrs]

    assert_sorted(normalized_attrs, message=message)


@pytest.fixture(scope="session")
def renderer() -> StructuredRenderer:
    rend = StructuredRenderer()

    with README_FILE_PATH.open() as f:
        md = mistune.Markdown(renderer=rend)
        md.render(f.read())

    return rend


@pytest.fixture(scope="session")
def external_links(renderer: StructuredRenderer) -> List[Link]:
    # deduplicate as there might be repeats, but keep original order
    unique_links = dict.fromkeys(renderer.links)

    return [link for link in unique_links if link.url.startswith(("http", "https"))]


@pytest.fixture(scope="session")
def internal_links(renderer: StructuredRenderer) -> List[Link]:
    return [link for link in renderer.links if link.url.startswith("#")]


@pytest.fixture(scope="session")
def headers(renderer: StructuredRenderer) -> List[Header]:
    return renderer.headers


@pytest.mark.asyncio
@pytest.mark.external
async def test_external_links_are_all_valid(external_links, event_loop):
    # fetch all responses fully asynchronously, iterate as completed

    async for link, response in fetch_all_links(external_links, event_loop):
        is_ok = response.status == 200

        if not is_ok and link.url in IGNORE_ERRORS_FOR_URLS:
            print(f"Ignored response: {response.status} {response.reason} for: {link}")
            continue

        assert is_ok, f"Couldn't open: {link}"


async def fetch_all_links(external_links, event_loop):
    async with aiohttp.ClientSession(loop=event_loop) as session:
        fetch_coros = [fetch_link(link, session) for link in external_links]

        for fetch_task in asyncio.as_completed(fetch_coros, loop=event_loop):
            result = await fetch_task
            yield result


async def fetch_link(link: Link, session: aiohttp.ClientSession):
    method = choose_fetch_method_for_link(link, session)
    method_name = method.__name__.upper()

    try:
        async with method(link.url, timeout=DEFAULT_TIMEOUT) as response:
            print(
                f"Opening ({method_name}): {link} -> {response.status} {response.reason}"
            )

            return link, response
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        print(f"Error opening {link}: {e}")
        raise


def choose_fetch_method_for_link(link: Link, session: aiohttp.ClientSession):
    if link.url.endswith((".png", ".pdf")):
        # assume that large static files are OK if HEAD request succeeds
        return session.head

    return session.get


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

    assert link_slugs == header_slugs


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


def test_external_links_are_sorted_in_lists(external_links):
    for (header, markdown_list), links in itertools.groupby(
        external_links, lambda link: (link.header, link.list)
    ):
        if header.level < CHECK_HEADER_LINKS_UP_TO_LEVEL:
            continue

        # skip repeated list items (e.g. we only want first link in a list item)
        first_links = []
        seen_list_items = set()

        for link in links:
            if link.list_item in seen_list_items:
                continue

            first_links.append(link)
            seen_list_items.add(link.list_item)

        assert_attr_sorted(
            first_links, "text", f"Links not sorted in a list under {header}"
        )
