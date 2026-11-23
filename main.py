#!/usr/bin/env python3
"""One Emoji, One Smile — entry writer.

Writes exactly one heart-hands emoji (U+1FAF6) to /output/entry.txt,
then reads it back and checks it is precisely that one character.
"""

import os

EMOJI = "\U0001FAF6"  # 🫶 HEART HANDS
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_emoji(emoji: str) -> str:
    """Check that `emoji` is exactly one emoji code point.

    The competition gate requires an entry of 1-8 characters, so the
    check keeps the character-length window and adds the byte-length
    ceiling (a single emoji code point is at most 4 UTF-8 bytes, well
    under 8), the single-code-point requirement, and a whitespace
    rejection. Raises ValueError on any violation.
    """
    if len(emoji) != 1:
        raise ValueError(
            f"emoji must be exactly 1 code point, got {len(emoji)}"
        )
    if not 1 <= len(emoji) <= 8:
        raise ValueError("emoji must be 1-8 characters long")
    if len(emoji.encode("utf-8")) > 8:
        raise ValueError("emoji must be at most 8 UTF-8 bytes")
    if not emoji.strip():
        raise ValueError("emoji must not be only whitespace")
    return emoji


def main() -> None:
    validate_emoji(EMOJI)

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
