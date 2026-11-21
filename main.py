#!/usr/bin/env python3
"""Write the one-line joke entry to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = OUTPUT_DIR + "/entry.txt"

JOKE = (
    "My agent crashed the demo and said it worked on its machine "
    "\u2014 I checked, and its machine is mine."
)


def write_entry(text: str, path: str = OUTPUT_PATH) -> None:
    """Write one line of text (plus a trailing newline) to path as UTF-8."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()
