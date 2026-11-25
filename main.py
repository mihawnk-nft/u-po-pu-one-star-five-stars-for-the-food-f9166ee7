#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry (program/v1).

Writes a single sentence (<=200 chars) to /output/entry.txt: a one-star
review of Earth by an alien tourist that still compliments the food.
Pure standard library; no network, no secrets, deterministic output.
"""

import os

ENTRY = (
    "One star: the humans charge rent for air, queue for hours to eat "
    "standing up, and yet the street noodles were so good I considered "
    "defecting to Earth."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
