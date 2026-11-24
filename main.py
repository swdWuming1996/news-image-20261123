#!/usr/bin/env python3
"""Entry program for news-image-20261123.

Copies the poster (entry.png, drawn by draw_poster.py from code) to the
output path. Deterministic: the same bytes every run, no network, stdlib only.

Before copying, the source is validated: it must exist, have PNG magic
bytes, be at most 1 MiB, and be 1024x1024 as parsed from the PNG IHDR
header. Any failure is loud (exception, non-zero exit).
"""
import os
import shutil
import struct
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1 * 1024 * 1024
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def validate_entry(path: Path) -> None:
    if not path.is_file():
        raise SystemExit(f"entry image missing: {path}")
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry image too large: {len(data)} bytes > {MAX_BYTES}")
    if data[:8] != PNG_MAGIC:
        raise SystemExit("entry image is not a PNG (bad magic bytes)")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise SystemExit("entry image is not a valid PNG (missing IHDR)")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(
            f"entry image must be {EXPECTED_WIDTH}x{EXPECTED_HEIGHT}, "
            f"got {width}x{height}"
        )


def main() -> None:
    validate_entry(SRC)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
