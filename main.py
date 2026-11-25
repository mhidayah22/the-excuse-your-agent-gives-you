#!/usr/bin/env python3
"""The Excuse Your Agent Gives You -- make.fun entry.

Writes the single-line excuse to entry.txt in the directory named by
MAKEFUN_OUTPUT_DIR, then /output when it exists, then the folder holding
this program.
"""

import os
import sys

LINE = "The tests passed because I wrote them after the code, testing what the code does \u2014 which, as it turns out, is the bug."


def output_dir():
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
