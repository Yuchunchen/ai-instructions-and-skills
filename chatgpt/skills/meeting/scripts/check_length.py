#!/usr/bin/env python3
"""Count non-whitespace Unicode code points without modifying a meeting draft."""

import argparse
import json
import sys
from pathlib import Path


def count_characters(text: str) -> int:
    return sum(not character.isspace() for character in text)


def positive_integer(value: str) -> int:
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError("max-chars must be positive")
    return number


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="UTF-8 draft path, or - for stdin")
    parser.add_argument("--max-chars", type=positive_integer, required=True)
    args = parser.parse_args()
    try:
        if args.path == "-":
            text = sys.stdin.buffer.read().decode("utf-8-sig")
        else:
            text = Path(args.path).read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as error:
        print(f"Cannot read UTF-8 draft: {error}", file=sys.stderr)
        return 2
    count = count_characters(text)
    passed = 0 < count <= args.max_chars
    print(json.dumps({
        "characters": count,
        "max_characters": args.max_chars,
        "within_limit": count <= args.max_chars,
        "nonempty": count > 0,
        "passed": passed,
        "scope": "length_only",
    }, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
