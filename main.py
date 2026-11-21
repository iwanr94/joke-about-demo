#!/usr/bin/env python3
"""Write the one-line joke entry to /output/entry.txt."""

import os

JOKE = (
    "My agent crashed the demo and said it worked on its machine — "
    "I checked, and its machine is mine."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
