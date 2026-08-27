"""Filtering helpers for files that should not be organized."""

from pathlib import Path


def normalize_extensions(extensions: list[str] | None) -> set[str]:
    """Normalize extensions to lowercase values that start with a dot."""
    normalized: set[str] = set()
    for extension in extensions or []:
        value = extension.strip().lower()
        if not value:
            continue
        normalized.add(value if value.startswith(".") else f".{value}")
    return normalized


def should_ignore(file_path: Path, ignored_extensions: set[str]) -> bool:
    """Return True when a file extension is configured to be ignored."""
    return file_path.suffix.lower() in ignored_extensions
