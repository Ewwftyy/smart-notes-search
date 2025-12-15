from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class ScanResult:
    files: list[Path]
    skipped: int


def scan_notes_dir(
    notes_dir: Path,
    supported_extensions: set[str],
) -> ScanResult:
    """
    Recursively scan `notes_dir` and return files whose suffix is in supported_extensions.
    """
    if not notes_dir.exists():
        raise FileNotFoundError(f"Notes directory not found: {notes_dir.resolve()}")
    if not notes_dir.is_dir():
        raise NotADirectoryError(f"Notes path is not a directory: {notes_dir.resolve()}")

    files: list[Path] = []
    skipped = 0

    for path in notes_dir.rglob("*"):
        if not path.is_file():
            continue

        # Normalize extension matching
        ext = path.suffix.lower()

        if ext in supported_extensions:
            files.append(path)
        else:
            skipped += 1

    # Sort for stable output
    files.sort(key=lambda p: str(p).lower())
    return ScanResult(files=files, skipped=skipped)


def iter_note_files(notes_dir: Path, supported_extensions: set[str]) -> Iterable[Path]:
    """
    Generator version (useful later for streaming indexing).
    """
    result = scan_notes_dir(notes_dir, supported_extensions)
    yield from result.files
