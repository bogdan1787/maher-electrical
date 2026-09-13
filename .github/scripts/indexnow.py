#!/usr/bin/env python3
"""Submit new or changed URLs to IndexNow after deployment.

Maps changed .html files from the push to their canonical URLs and POSTs
them to api.indexnow.org (Bing, Yandex and other participating engines).
Falls back to every URL in sitemap.xml when the diff cannot be computed,
when the push includes a changed sitemap, or on manual dispatch.
"""
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

HOST = os.environ.get("HOST", "maherelectrical.ie")
KEY = os.environ["INDEXNOW_KEY"]
BASE = f"https://{HOST}"
KEY_LOCATION = f"{BASE}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def changed_urls():
    """Return sorted URLs for changed HTML files, or None to submit everything."""
    if os.environ.get("EVENT_NAME") == "workflow_dispatch":
        return None
    before = os.environ.get("EVENT_BEFORE", "")
    sha = os.environ.get("SHA", "HEAD")
    if not before or set(before) == {"0"}:
        return None
    result = subprocess.run(
        ["git", "diff", "--name-only", before, sha],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        return None
    urls = set()
    for path in result.stdout.splitlines():
        path = path.strip()
        if not path:
            continue
        if path == "sitemap.xml":
            return None
        if not path.endswith(".html") or path.startswith("."):
            continue
        if path == "index.html":
            urls.add(f"{BASE}/")
        elif path.endswith("/index.html"):
            urls.add(f"{BASE}/{path[: -len('index.html')]}")
        else:
            urls.add(f"{BASE}/{path}")
    return sorted(urls)


def sitemap_urls():
    with urllib.request.urlopen(f"{BASE}/sitemap.xml", timeout=30) as response:
        body = response.read().decode("utf-8")
    return re.findall(r"<loc>(.*?)</loc>", body)


def wait_for_deploy(urls, attempts=20, delay=15):
    """Wait until the key file and at least one submitted URL are live."""
    for _ in range(attempts):
        try:
            with urllib.request.urlopen(KEY_LOCATION, timeout=15) as response:
                if KEY in response.read().decode("utf-8"):
                    probe = urls[0]
                    try:
                        with urllib.request.urlopen(probe, timeout=15) as page:
                            if page.status == 200:
                                return True
                    except urllib.error.HTTPError as exc:
                        if exc.code != 404:
                            return True
                    except Exception:
                        pass
        except Exception:
            pass
        time.sleep(delay)
    return False


def main():
    urls = changed_urls()
    if urls is None:
        try:
            urls = sitemap_urls()
        except Exception as exc:
            print(f"Could not fetch sitemap.xml: {exc}")
            return 1
    if not urls:
        print("No new or changed HTML URLs in this push; nothing to submit.")
        return 0
    if not wait_for_deploy(urls):
        print("Site not reachable yet; skipping IndexNow submission.")
        return 0
    payload = json.dumps(
        {"host": HOST, "key": KEY, "keyLocation": KEY_LOCATION, "urlList": urls}
    ).encode("utf-8")
    request = urllib.request.Request(
        ENDPOINT, data=payload, headers={"Content-Type": "application/json; charset=utf-8"}
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            print(f"IndexNow responded {response.status} for {len(urls)} URL(s)")
            return 0 if response.status in (200, 202) else 1
    except urllib.error.HTTPError as exc:
        print(f"IndexNow error {exc.code}: {exc.read().decode(errors='replace')}")
        return 1
    except Exception as exc:
        print(f"IndexNow request failed: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
