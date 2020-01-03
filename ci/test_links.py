import asyncio
import itertools
import pathlib
import random
import re

from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from functools import wraps
from io import StringIO
from types import MappingProxyType
from typing import Iterable, List, Optional, Tuple

import aiohttp
import mistune
import pytest

from aiohttp import ClientResponse
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

IGNORE_ERRORS_FOR_URLS = frozenset(
    (
        # Travis CI gets 403 Forbidden here :(
        "https://vimeo.com/293912618/5ccecc85d4",
        "https://webcache.googleusercontent.com/search?q=cache:dEddeFq1R_gJ:https://speice.io/2019/02/understanding-allocations-in-rust.html",
    )
)

DEFAULT_TIMEOUT_SECONDS = 45
DEFAULT_TIMEOUT = aiohttp.ClientTimeout(total=DEFAULT_TIMEOUT_SECONDS)

# looks like youtube.com is throttling requests,
# randomly wait this many seconds between retries
YOUTUBE_THROTTLE_WAIT_SECONDS_RANGE = (1, 5)
YOUTUBE_THROTTLE_MAX_RETRIES = 10

# generic retrying
GENERIC_WAIT_SECONDS_RANGE = (1, 5)
GENERIC_MAX_RETRIES = 5
GENERIC_RETRY_CODES = frozenset((403, 503))

# Use a fake user agent to pretend we're a browser
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"


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

    header: Optional[Header] = field(compare=False, hash=False)


@dataclass(frozen=True)
class LinkList:
    header: Header
    links: List[Link]


@dataclass(frozen=True)
class FetchResult:
    link: Link
    response: Optional[ClientResponse]
    exception: Optional[Exception]

    @property
    def is_ok(self) -> bool:
        return bool(
            self.response and self.response.status == 200 and not self.exception
        )

    @property
    def error_description(self) -> Optional[str]:
        if self.is_ok:
            return None
        elif self.response:
            return f"Status code: {self.response.status}"
        elif self.exception:
            if isinstance(self.exception, TimeoutError):
                return "Timed out"
            else:
                return f"Exception: {self.exception}"
        else:
            raise RuntimeError("Unreachable!")


class StructuredRenderer(mistune.Renderer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._headers: List[Header] = []
        self._links: List[Link] = []

        self._link_lists: List[LinkList] = []

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


@pytest.fixture(scope="session")
def link_lists(renderer: StructuredRenderer) -> List[LinkList]:
    return renderer.link_lists


@pytest.mark.asyncio
@pytest.mark.external
async def test_external_links_are_all_valid(external_links, event_loop):
    # fetch all responses fully asynchronously, iterate as completed
    failures = []
    ignored = []
    successes = []

    async for fetch_result in fetch_all_links(external_links, event_loop):
        if not fetch_result.is_ok and fetch_result.link.url in IGNORE_ERRORS_FOR_URLS:
            ignored.append(fetch_result)
            continue

        if fetch_result.is_ok:
            successes.append(fetch_result)
        else:
            failures.append(fetch_result)

    print(f">>> Ignored: {len(ignored)} responses")
    print(f">>> OK: {len(successes)} responses")

    if failures:
        pytest.fail(
            f">>> Failures: {len(failures)}\n"
            + "\n".join(
                f"FAIL ({fetch_result.error_description}): {fetch_result.link}"
                for fetch_result in failures
            ),
            pytrace=False,
        )


async def fetch_all_links(external_links, event_loop):
    async with aiohttp.ClientSession(
        loop=event_loop, headers={"User-Agent": USER_AGENT},
    ) as session:
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

            return FetchResult(link, response, None)
    except (aiohttp.ClientError, asyncio.TimeoutError) as e:
        print(f"Error opening {link}: {e}")
        return FetchResult(link, None, e)


def choose_fetch_method_for_link(link: Link, session: aiohttp.ClientSession):
    if link.url.endswith((".png", ".pdf")):
        # assume that large static files are OK if HEAD request succeeds
        return session.head

    if "youtube.com/" in link.url:
        return get_retrying_on_throttling(
            session,
            max_retries=YOUTUBE_THROTTLE_MAX_RETRIES,
            random_sleep=YOUTUBE_THROTTLE_WAIT_SECONDS_RANGE,
        )

    return get_retrying(
        session,
        codes=GENERIC_RETRY_CODES,
        max_retries=GENERIC_MAX_RETRIES,
        random_sleep=GENERIC_WAIT_SECONDS_RANGE,
    )


def get_retrying(
    session: aiohttp.ClientSession,
    codes: Iterable[int],
    max_retries: int = 1,
    random_sleep=Optional[Tuple[int, int]],
):
    code_set = set(codes)

    @asynccontextmanager
    @wraps(session.get)
    async def wrapper(*args, **kwargs):
        for _ in range(max_retries + 1):
            async with session.get(*args, **kwargs) as response:
                if response.status in code_set:
                    sleep_for = random.uniform(*random_sleep)
                    await asyncio.sleep(sleep_for)
                else:
                    yield response
                    return

        raise TimeoutError(
            f"Failed to fetch {args[0]} after {max_retries} retries, response code: {response.status}"
        )

    return wrapper


def get_retrying_on_throttling(
    session: aiohttp.ClientSession,
    max_retries: int = 1,
    random_sleep=Optional[Tuple[int, int]],
):
    return get_retrying(
        # 429 too many requests
        session,
        codes=(429,),
        max_retries=max_retries,
        random_sleep=random_sleep,
    )


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
