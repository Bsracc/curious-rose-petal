#!/usr/bin/env python3
"""Write one calm, curious text to /output/entry.txt.

No network, no dependencies. Python 3.13 compatible.
The text is 215 characters, within the 1-280 limit.
"""

from pathlib import Path

TEXT = (
    "The old gardener waters a rose that never blooms. "
    "Each morning he finds one petal on the path, though the bush is bare, "
    "and he keeps the petals in a tin, counting them, "
    "waiting to see what the rose is saving up for."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
