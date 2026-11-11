"""cutest-cat-01 entry #2: copies the bundled sleeping-cat picture out.

The grader runs this as `python3 -P -s /bot/main.py` with the repository
read-only at /bot and a writable output directory (MAKEFUN_OUTPUT_DIR,
the grader's /output). The picture ships in the repository as entry.png;
this program copies it, byte for byte, to <output>/entry.png and exits.
It runs identically every time, so the two grading runs agree.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
