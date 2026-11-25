#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands (make.fun).

Writes the entry -- one joke about cats, one line --
to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'My cat sat on my keyboard and wrote a better commit message than I have all year — the code review approved it before I did.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
