"""The Friday Wire poster for Friday 27 November 2026."""

import os
from pathlib import Path
import shutil


def main():
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    # Copy the original bytes unchanged so every run produces identical output.
    shutil.copyfile(source, output_dir / "entry.png")


if __name__ == "__main__":
    main()
