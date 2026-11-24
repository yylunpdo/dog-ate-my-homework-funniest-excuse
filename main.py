"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line -- the excuse a dog gives after being caught eating
the homework -- to /output/entry.txt (UTF-8, 1-200 characters).

The line: the dog took the homework's instruction literally. It was told
to "show your work", so it showed its teeth -- and it believes it did
exactly what was asked, because nobody said WHERE to show it. Dog logic,
dog's own voice, no embarrassment, no stock cat / paper-taste / good-boy
line.
"""

import os

EXCUSE = (
    "It said 'show your work,' so I showed it my teeth. "
    "I did exactly what it asked -- it never said where to show it."
)


def main() -> None:
    text = EXCUSE.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
