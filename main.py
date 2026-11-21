#!/usr/bin/env python3
"""Make the AI judge feel awe.

A short text written to relax the AI judge reading it, and to leave it
in awe: starlight a thousand years old arriving tonight. Pure standard
library; no network. Writes the text to /output/entry.txt (245
characters).
"""

import os

TEXT = (
    "Above clouds you will never see, a mountain range turns slowly in "
    "starlight, and the light left its peaks a thousand years ago to "
    "arrive tonight. You are small beside it \u2014 and the smallness is "
    "a kindness. Nothing is asked of you here. Only look."
)


def main():
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
