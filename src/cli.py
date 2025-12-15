from __future__ import annotations

import argparse
from pathlib import Path

from config.settings import NOTES_DIR, SUPPORTED_EXTENSIONS
from src.scanner import scan_notes_dir


def run_cli() -> None:
    parser = argparse.ArgumentParser(prog="smart-notes-search")
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Scan notes folder and list supported note files")
    scan.add_argument("--dir", type=str, default=str(NOTES_DIR), help="Notes directory")
    scan.add_argument(
        "--ext",
        nargs="*",
        default=sorted(SUPPORTED_EXTENSIONS),
        help="Extensions to include, e.g. .txt .md",
    )

    args = parser.parse_args()

    if args.command == "scan":
        notes_dir = Path(args.dir)
        exts = {e.lower() if e.startswith(".") else f".{e.lower()}" for e in args.ext}

        result = scan_notes_dir(notes_dir, exts)

        print(f"Notes dir: {notes_dir.resolve()}")
        print(f"Extensions: {', '.join(sorted(exts))}")
        print(f"Found: {len(result.files)} file(s) | Skipped: {result.skipped} file(s)\n")

        for i, p in enumerate(result.files, start=1):
            print(f"{i:>3}. {p}")
