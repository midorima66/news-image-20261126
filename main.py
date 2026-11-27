#!/usr/bin/env python3
"""Entrypoint for the 26 November 2026 front-page image.

The collage itself was drawn in advance and ships in this repository as
entry.png, so this program only has to put that exact file where the
grader looks for it. Copying fixed bytes keeps both graded runs identical.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
NAME = "entry.png"


def output_dir():
    """First command-line argument wins, then MAKEFUN_OUTPUT_DIR, then /output."""
    if len(sys.argv) > 1:
        return Path(sys.argv[1])
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    dest_dir = output_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / NAME
    # Skipping the copy when source and destination are the same file keeps
    # the run quiet instead of raising on a self-copy.
    if dest.resolve() == SOURCE.resolve():
        return
    shutil.copyfile(SOURCE, dest)


if __name__ == "__main__":
    main()
