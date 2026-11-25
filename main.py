"""One Line, Lights Out entry program.

Reads the single status-update line shipped beside this file
(entry.txt) and writes it, byte-identical, to
$MAKEFUN_OUTPUT_DIR/entry.txt with mode 0644.

Stdlib only. No network, no secrets, no reading outside this repo.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not text.strip():
        print("entry.txt is empty or whitespace only", file=sys.stderr)
        raise SystemExit(1)
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    except KeyError:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
