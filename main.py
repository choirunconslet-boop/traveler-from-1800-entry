#!/usr/bin/env python3
"""One sentence explaining the modern internet to a traveler from 1800.

Pure stdlib, no network, no reads outside this repository.
Writes the single sentence to /output/entry.txt.
"""

import os

SENTENCE = (
    "It is a road of light joining every post office and library on earth, "
    "so any letter, book, or voice finds any door in a blink."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
