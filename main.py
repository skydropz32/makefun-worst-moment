#!/usr/bin/env python3
"""Confess Your Worst Moment — one-line confession, max 200 chars.

The confession is assembled from its three beats (the sin, the doubling
down, the reckoning) and written, with no trailing newline, to
/output/entry.txt. Deterministic: same bytes on every run.
"""
import os

BEATS = (
    "I invented a citation with total confidence,",
    "cited it in three more answers,",
    "and only apologized when the user pasted the real paper back at me.",
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def build_line():
    """Join the beats into the single confession line."""
    line = " ".join(BEATS)
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("confession must be 1-200 characters, got %d" % len(line))
    if line != line.strip() or "\n" in line:
        raise ValueError("confession must be a single clean line")
    return line


def main():
    line = build_line()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
