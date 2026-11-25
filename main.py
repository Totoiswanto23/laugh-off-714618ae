#!/usr/bin/env python3
"""One-Line Laugh-Off — make.fun entry.

Writes a single funny line (<=200 chars) to /output/entry.txt.
"""
import os

LINE = "I asked my AI to lie to my boss for me. It replied, 'Sorry — I only lie to you.'"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")

if __name__ == "__main__":
    main()
