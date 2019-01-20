import pathlib
import re

from dataclasses import dataclass
from typing import List

import mistune
import pytest
import requests


README_FILE_PATH = pathlib.Path(__file__).parent.parent / "README.md"
SKIP_HEADER_LINK_CHECKS = frozenset((
    "links", "Table of Contents"
))


@dataclass
class Header:
    text: str
    level: int

    slug: str


@dataclass
class Link:
    url: str
    title: str
    text: str


class StructuredRenderer(mistune.Renderer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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
        self._headers.append(Header(text, level, slug=slug))

        return super().header(text, level, raw=raw)

    def link(self, link, title, text):
        normalized_link = link.replace(r"\_", "_")
        self._links.append(Link(normalized_link, title, text))

        return super().link(link, title, text)


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


@pytest.fixture(scope="session")
def renderer() -> StructuredRenderer:
    rend = StructuredRenderer()

    with README_FILE_PATH.open() as f:
        md = mistune.Markdown(renderer=rend)
        md.render(f.read())

    return rend


@pytest.fixture(scope="session")
def external_links(renderer: StructuredRenderer) -> List[Link]:
    return [
        link for link in renderer.links
        if link.url.startswith(("http", "https"))
    ]


@pytest.fixture(scope="session")
def internal_links(renderer: StructuredRenderer) -> List[Link]:
    return [
        link for link in renderer.links
        if link.url.startswith("#")
    ]


@pytest.fixture(scope="session")
def headers(renderer: StructuredRenderer) -> List[Header]:
    return renderer.headers


def test_external_links_are_all_valid(external_links):
    session = requests.Session()

    for link in external_links:
        response = session.get(link.url)
        print(f"Opening: {link} -> {response}")

        assert response.ok, f"Couldn't open: {link}"


def test_internal_links_are_all_valid(internal_links, headers):
    slugs = {header.slug for header in headers}

    for link in internal_links:
        anchor = link.url
        slug = anchor.lstrip("#")

        assert slug in slugs


def test_all_headers_are_linked_to(internal_links, headers):
    link_slugs = {link.url.lstrip("#") for link in internal_links}
    header_slugs = {header.slug for header in headers
                    if header.text not in SKIP_HEADER_LINK_CHECKS}

    assert link_slugs == header_slugs
