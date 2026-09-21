"""Small defensive example: read only files within an authorized root.

This module does not scan or contact any external system.
"""

from pathlib import Path


class UnsafePathError(ValueError):
    """The requested file is outside the approved directory."""


def read_text_within(root: Path, requested: str) -> str:
    """Read an existing UTF-8 file confined to root, including symlink resolution."""
    trusted_root = root.resolve(strict=True)
    if not trusted_root.is_dir():
        raise NotADirectoryError(trusted_root)

    candidate = (trusted_root / requested).resolve(strict=True)
    if not candidate.is_relative_to(trusted_root):
        raise UnsafePathError("File is outside the approved directory")
    if not candidate.is_file():
        raise IsADirectoryError(candidate)
    return candidate.read_text(encoding="utf-8")
