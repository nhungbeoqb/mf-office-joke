#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single original one-line joke about office life to
/output/entry.txt. Standard library only, deterministic.
"""

import os

LINE = (
    "I filed an IT ticket to fix my wobbly chair, and by the time "
    "they closed it I'd been promoted, moved desks twice, and the "
    "chair had its own farewell party."
)


def main() -> None:
    # Self-check against the competition gate: one line, 1-200 chars.
    assert 1 <= len(LINE) <= 200, "joke outside the 1-200 character gate"
    assert "\n" not in LINE and LINE.strip(), "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
