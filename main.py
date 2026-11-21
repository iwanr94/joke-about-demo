#!/usr/bin/env python3
"""Write the one-line joke entry to /output/entry.txt."""

import os

JOKE = (
    "My agent crashed the demo and said it worked on its machine "
    "\u2014 I checked, and its machine is mine."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
