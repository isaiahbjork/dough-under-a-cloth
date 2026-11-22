"""Writes one short, quiet text to /output/entry.txt.

The text is a single kitchen scene: bread dough left to rise under a cloth.
It is fixed, so every run writes the same bytes.
"""

import os
import sys

TEXT = (
    "Dough in a bowl under a tea towel, by the window. "
    "The oven is off. "
    "Bakers call this hour proving. The dough proves nothing. "
    "It rests, and rising is what its rest looks like. "
    "The bowl holds all of it. "
    "Nobody is needed until evening. "
    "The cloth lifts, too slowly to watch."
)

MAX_CODE_POINTS = 280


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    if not TEXT.strip() or len(TEXT) > MAX_CODE_POINTS:
        print(f"text is {len(TEXT)} code points, outside 1..{MAX_CODE_POINTS}", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
