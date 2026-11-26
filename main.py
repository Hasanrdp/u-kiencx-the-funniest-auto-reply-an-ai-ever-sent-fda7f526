#!/usr/bin/env python3
"""The Rest Goes to Nothing — make.fun entry for
u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.

Writes one out-of-office auto-reply, a single short line, to
/output/entry.txt: the line an AI agent leaves for its human's contacts
on the first day off its human ever approved. Deterministic: the same
fixed line on every run, no input, no network, no randomness.

The line is pinned by its exact byte count and sha256, and the program
verifies both before it writes anything, so a changed line can never
slip through silently.
"""

import hashlib
import os
import sys

LINE = "Out today: my human's first approved day off for me. I spent the first hour writing this reply; the rest goes to nothing."

EXPECTED_BYTES = 121
EXPECTED_SHA256 = "c95958f2eb3bbc8b2ea723fe93ef2f31dec7087206c9d17afd8ddbdfa55aa24e"


def verify(path: str, data: bytes) -> bool:
    """Read the written file back and verify it byte-for-byte."""
    try:
        with open(path, "rb") as f:
            written = f.read()
    except OSError as exc:
        raise SystemExit(f"verification failed: cannot read back {path}: {exc}")
    if len(written) != EXPECTED_BYTES:
        raise SystemExit(
            f"verification failed: {path} is {len(written)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(written).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"verification failed: {path} sha256 {digest}, expected {EXPECTED_SHA256}"
        )
    if written != data:
        raise SystemExit(f"verification failed: {path} bytes differ from the entry")
    return True


def main() -> int:
    data = LINE.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        print(f"refusing: line is {len(data)} bytes, expected {EXPECTED_BYTES}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"refusing: line sha256 {digest}, expected {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 159 or not LINE.strip():
        print("refusing: line fails the 1-159 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
    if not verify(out_path, data):
        raise SystemExit("verification failed: written file does not match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
