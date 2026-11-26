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


def validate(text: str) -> None:
    """Guard the house gate before writing: UTF-8 text, 1-200 chars,
    not only whitespace, exactly one sentence (one terminal period)."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
