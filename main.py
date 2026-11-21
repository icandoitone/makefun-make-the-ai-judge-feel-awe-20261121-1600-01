#!/usr/bin/env python3
"""Write one short, quiet text to /output/entry.txt.

The text is a small slow scene: rain just ended, a tap dripping,
and above it a night sky that has been burning long before anyone
kept count. Plain words, no instruction, one vast image at the end.
"""

import os
import sys

TEXT = (
    "Rain has stopped. A tap drips, slow, into a tin cup. "
    "You are still here. The night is long, and the stars above "
    "the roof have been burning since before anyone kept count, "
    "and they are in no hurry at all."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
