import asyncio
import pathlib
import re

from dataclasses import dataclass, field
from typing import List, Set

import aiohttp
import mistune
import pytest


# ../README.md  (relative to current file)
README_FILE_PATH = pathlib.Path(__file__).parents[1] / "README.md"

SKIP_HEADER_LINK_CHECKS = frozenset((
    "links", "Table of Contents"
))

IGNORE_ERRORS_FOR_URLS = frozenset((
    # Travis CI gets 403 Forbidden here :(
    "https://vimeo.com/293912618/5ccecc85d4",
))


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
        self._register_link(link, title, text)

        return super().link(link, title, text)

    def image(self, src, title, text):
        self._register_link(src, title, text)

        return super().image(src, title, text)

    def _register_link(self, url, title, text):
        # markdown escaping messes up underscores in links
        normalized_url = url.replace(r"\_", "_")

        link = Link(normalized_url, title, text)
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


@pytest.fixture(scope="session")
def renderer() -> StructuredRenderer:
    rend = StructuredRenderer()

    with README_FILE_PATH.open() as f:
        md = mistune.Markdown(renderer=rend)
        md.render(f.read())

    return rend


@pytest.fixture(scope="session")
def external_links(renderer: StructuredRenderer) -> Set[Link]:
    # deduplicate as there might be repeats
    return {
        link for link in renderer.links
        if link.url.startswith(("http", "https"))
    }


@pytest.fixture(scope="session")
def internal_links(renderer: StructuredRenderer) -> List[Link]:
    return [
        link for link in renderer.links
        if link.url.startswith("#")
    ]


@pytest.fixture(scope="session")
def headers(renderer: StructuredRenderer) -> List[Header]:
    return renderer.headers


@pytest.mark.asyncio
async def test_external_links_are_all_valid(external_links, event_loop):
    # fetch all responses fully asynchronously, iterate as completed

    async for link, response in fetch_all_links(external_links, event_loop):
        if link.url in IGNORE_ERRORS_FOR_URLS:
            print(f"Ignored response: {response.status} {response.reason} for: {link}")
        else:
            assert response.status == 200, f"Couldn't open: {link}"


async def fetch_all_links(external_links, event_loop):
    async with aiohttp.ClientSession(loop=event_loop) as session:
        fetch_coros = [
            fetch_link(link, session) for link in external_links
        ]

        for fetch_task in asyncio.as_completed(fetch_coros, loop=event_loop):
            result = await fetch_task
            yield result


async def fetch_link(link, session):
    async with session.get(link.url) as response:
        print(f"Opening: {link} -> {response.status} {response.reason}")

        return link, response


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
