#!/usr/bin/env python3
"""Check whether a small digital-product storefront is buyer-ready."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser


DEFAULT_TIMEOUT_SECONDS = 15
PAYMENT_HOST_HINTS = (
    "paypal.me",
    "paypal.com",
    "payhip.com",
    "gumroad.com",
    "lemonsqueezy.com",
    "polar.sh",
    "buy.stripe.com",
)


@dataclass(frozen=True)
class FetchResult:
    url: str
    status: int | None
    content_type: str
    body: str
    error: str


@dataclass(frozen=True)
class Check:
    name: str
    status: str
    detail: str


class StorefrontParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.in_title = False
        self.meta: dict[str, str] = {}
        self.links: list[tuple[str, str]] = []
        self.anchors: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {key.lower(): value or "" for key, value in attrs}
        if tag.lower() == "title":
            self.in_title = True
        elif tag.lower() == "meta":
            key = attr.get("name") or attr.get("property")
            if key:
                self.meta[key.lower()] = attr.get("content", "").strip()
        elif tag.lower() == "link":
            rel = attr.get("rel", "").lower()
            href = attr.get("href", "")
            if rel and href:
                self.links.append((rel, href))
        elif tag.lower() == "a":
            href = attr.get("href", "")
            if href:
                self.anchors.append((href, ""))

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data.strip())
        if self.anchors:
            href, text = self.anchors[-1]
            self.anchors[-1] = (href, f"{text} {data.strip()}".strip())

    @property
    def title(self) -> str:
        return " ".join(part for part in self.title_parts if part).strip()


def fetch(url: str, timeout: int) -> FetchResult:
    request = urllib.request.Request(url, headers={"User-Agent": "storefront-checker/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read()
            charset = response.headers.get_content_charset() or "utf-8"
            body = raw.decode(charset, errors="replace")
            return FetchResult(
                url=response.geturl(),
                status=response.status,
                content_type=response.headers.get("content-type", ""),
                body=body,
                error="",
            )
    except (urllib.error.URLError, TimeoutError) as exc:
        return FetchResult(url=url, status=None, content_type="", body="", error=str(exc))


def fetch_head(url: str, timeout: int) -> tuple[int | None, str, str]:
    return fetch_probe(url, timeout, "HEAD")


def fetch_probe(url: str, timeout: int, method: str) -> tuple[int | None, str, str]:
    request = urllib.request.Request(url, method=method, headers={"User-Agent": "storefront-checker/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if method == "GET":
                response.read(2048)
            return response.status, response.headers.get("content-type", ""), ""
    except urllib.error.HTTPError as exc:
        if method == "HEAD" and exc.code in {403, 405}:
            return fetch_probe(url, timeout, "GET")
        return exc.code, exc.headers.get("content-type", ""), ""
    except (urllib.error.URLError, TimeoutError) as exc:
        if method == "HEAD":
            get_status, get_content_type, get_error = fetch_probe(url, timeout, "GET")
            if get_status is not None:
                return get_status, get_content_type, get_error
        return None, "", str(exc)


def absolute_url(page_url: str, value: str) -> str:
    return urllib.parse.urljoin(page_url, value)


def has_any_href(parser: StorefrontParser, needles: tuple[str, ...]) -> bool:
    for href, _text in parser.anchors:
        lowered = href.lower()
        if any(needle in lowered for needle in needles):
            return True
    return False


def has_any_text(body: str, needles: tuple[str, ...]) -> bool:
    lowered = body.lower()
    return any(needle in lowered for needle in needles)


def add_check(checks: list[Check], condition: bool, name: str, ok: str, miss: str, warn: bool = False) -> None:
    if condition:
        checks.append(Check(name, "PASS", ok))
    elif warn:
        checks.append(Check(name, "WARN", miss))
    else:
        checks.append(Check(name, "FAIL", miss))


def run_checks(url: str, html: str, status: int | None, timeout: int) -> list[Check]:
    parser = StorefrontParser()
    parser.feed(html)
    checks: list[Check] = []

    add_check(
        checks,
        status is not None and 200 <= status < 300,
        "page_http_status",
        f"page returned HTTP {status}",
        f"page did not return HTTP 2xx (status={status})",
    )
    add_check(checks, bool(parser.title), "html_title", parser.title or "title exists", "missing <title>")
    add_check(
        checks,
        bool(parser.meta.get("description")),
        "meta_description",
        parser.meta.get("description", ""),
        "missing meta description",
    )
    add_check(
        checks,
        bool(parser.meta.get("og:title") and parser.meta.get("og:description")),
        "open_graph_copy",
        "og:title and og:description exist",
        "missing og:title or og:description",
        warn=True,
    )
    add_check(
        checks,
        parser.meta.get("twitter:card") == "summary_large_image",
        "twitter_large_card",
        "twitter summary_large_image configured",
        "missing twitter summary_large_image card",
        warn=True,
    )

    image_url = parser.meta.get("og:image") or parser.meta.get("twitter:image")
    if image_url:
        resolved = absolute_url(url, image_url)
        image_status, content_type, error = fetch_head(resolved, timeout)
        image_ok = image_status is not None and 200 <= image_status < 300 and content_type.lower().startswith("image/")
        detail = f"{resolved} -> HTTP {image_status}, {content_type}".strip()
        checks.append(Check("social_image_fetch", "PASS" if image_ok else "WARN", detail if not error else error))
    else:
        checks.append(Check("social_image_fetch", "WARN", "missing og:image or twitter:image"))

    canonical = next((href for rel, href in parser.links if "canonical" in rel), "")
    add_check(checks, bool(canonical), "canonical_url", canonical, "missing canonical link", warn=True)
    add_check(
        checks,
        has_any_href(parser, PAYMENT_HOST_HINTS),
        "payment_link",
        "payment link found",
        "no PayPal/Payhip/Gumroad/Lemon/Polar/Stripe payment link found",
    )
    add_check(
        checks,
        bool(re.search(r"[\w.+-]+@[\w.-]+\.[a-z]{2,}", html, re.I)),
        "support_email",
        "support email found",
        "no support email found",
    )
    add_check(
        checks,
        has_any_href(parser, ("samples/", "sample", "preview", "release/download", ".apkg", ".pdf")),
        "free_sample_or_preview",
        "sample or preview link found",
        "no free sample or preview link found",
        warn=True,
    )
    add_check(
        checks,
        has_any_text(html, ("refund", "14-day", "14 day", "support")),
        "refund_or_support_terms",
        "refund/support language found",
        "missing refund or support terms",
        warn=True,
    )
    add_check(
        checks,
        has_any_href(parser, ("issues/new", "mailto:")),
        "buyer_contact_path",
        "buyer contact path found",
        "no GitHub issue or mailto buyer contact path found",
    )

    return checks


def print_markdown(url: str, result: FetchResult, checks: list[Check]) -> None:
    pass_count = sum(1 for check in checks if check.status == "PASS")
    warn_count = sum(1 for check in checks if check.status == "WARN")
    fail_count = sum(1 for check in checks if check.status == "FAIL")

    print("# Storefront Checker Report")
    print()
    print(f"- URL: {url}")
    print(f"- Final URL: {result.url}")
    print(f"- HTTP status: {result.status}")
    print(f"- Result: {pass_count} pass / {warn_count} warn / {fail_count} fail")
    print()
    print("| Check | Status | Detail |")
    print("|---|---:|---|")
    for check in checks:
        detail = check.detail.replace("|", "\\|").replace("\n", " ").strip()
        print(f"| `{check.name}` | {check.status} | {detail} |")
    print()
    if fail_count:
        print("## Next Action")
        print()
        print("Fix the FAIL items first: payment path, support email, buyer contact, and page availability.")
    elif warn_count:
        print("## Next Action")
        print()
        print("The page can accept buyers, but the WARN items may reduce trust or link-sharing conversion.")
    else:
        print("## Next Action")
        print()
        print("The storefront has the core buyer-readiness signals. Start looking for targeted traffic.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a digital-product storefront for buyer-readiness signals.")
    parser.add_argument("url", help="Public storefront URL to check")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--fail-under", type=int, default=0, help="Exit 1 if PASS count is below this value")
    args = parser.parse_args()

    result = fetch(args.url, args.timeout)
    if result.error:
        print("# Storefront Checker Report")
        print()
        print(f"- URL: {args.url}")
        print(f"- Error: {result.error}")
        return 2

    checks = run_checks(result.url, result.body, result.status, args.timeout)
    print_markdown(args.url, result, checks)

    pass_count = sum(1 for check in checks if check.status == "PASS")
    fail_count = sum(1 for check in checks if check.status == "FAIL")
    if args.fail_under and pass_count < args.fail_under:
        return 1
    if fail_count:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
