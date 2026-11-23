#!/usr/bin/env python3
"""One Emoji, One Smile — entry writer.

Writes exactly one heart-hands emoji (U+1FAF6) to /output/entry.txt,
then reads it back and checks it is precisely that one character.
"""

import os

EMOJI = "\U0001FAF6"  # 🫶 HEART HANDS
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    if not (1 <= len(EMOJI) <= 8):
        raise ValueError("emoji must be 1-8 characters long")
    if not EMOJI.strip():
        raise ValueError("emoji must not be only whitespace")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()

    if written != EMOJI:
        raise ValueError(
            f"verification failed: expected exactly {EMOJI!r}, got {written!r}"
        )

    print(f"Wrote one emoji to {OUTPUT_PATH}: {written!r}")


if __name__ == "__main__":
    main()
