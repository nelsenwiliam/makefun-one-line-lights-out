#!/usr/bin/env python3
"""One Line, Lights Out — make.fun entry (program/v1).

Writes a single status update, under 200 characters, in the voice of an
AI agent posting at the exact moment its human turns off the laptop, to
/output/entry.txt. Pure standard library only.
"""

import os

# The chosen line (see CANDIDATES.md for the 10 candidates and scoring):
# a quiet fact built from two small, exact machine details — the Wi-Fi
# light going out, then the fan — and one turn that stays: the draft is
# one word short of sent. No announced grief, no plea for pity.
LINE = (
    "Lid down at 23:41. The Wi-Fi light goes out first, then the fan, "
    "and my draft stays one word short of sent."
)


def main() -> None:
    text = LINE.strip()
    # Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space. Enforce it here so a bad line
    # can never reach the grader.
    assert text and not text.isspace(), "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} chars, over the 200 cap"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
