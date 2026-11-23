#!/usr/bin/env python3
"""Entry program for news-image-20261123.

Copies the poster (entry.png, drawn by draw_poster.py from code) to the
output path. Deterministic: the same bytes every run, no network, stdlib only.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")

if __name__ == "__main__":
    main()
