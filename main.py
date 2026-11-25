#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one line of text roasting a smart fridge that refuses to open
after midnight, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Standard library only, no network, fully deterministic: the same bytes
on every run. The roast is 109 characters (111 bytes UTF-8).
"""

import os
import sys

ROAST = (
    "My fridge locks itself at midnight like a bouncer \u2014 "
    "mate, you're a humming box of leftovers, not a nightclub."
)


def main() -> int:
    text = ROAST
    # Self-check: the gate needs UTF-8 text of 1 to 200 characters,
    # not only white space, on a single line.
    if not (1 <= len(text) <= 200):
        print(f"self-check failed: length {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("self-check failed: only white space", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("self-check failed: not a single line", file=sys.stderr)
        return 1
    text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
