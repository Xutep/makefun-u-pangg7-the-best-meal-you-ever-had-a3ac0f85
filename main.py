#!/usr/bin/env python3
"""The Best Meal You Ever Had -- make.fun entry.

Writes one sentence (at most 200 characters) about the best meal ever
had to /output/entry.txt. Deterministic, standard library only, no
network access and no input files: the sentence is fixed in this file,
so every run produces the exact same bytes.
"""

import os

SENTENCE = (
    "My grandmother's rendang in Jakarta fell apart at a touch, "
    "its coconut gravy steaming over rice I ate with my fingers, "
    "and twenty years later I still measure every meal against "
    "that first bite."
)

MAX_CHARS = 200


def main() -> None:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(
            f"sentence is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
