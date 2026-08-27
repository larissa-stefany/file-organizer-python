"""Core file organization logic."""

from __future__ import annotations

import shutil
from collections import Counter
from pathlib import Path

from src.classifier import classify_file


class FileOrganizer:
    """Organize files from a source directory into category folders."""

    def __init__(self, source: Path, dry_run: bool = False) -> None:
        self.source = source
        self.dry_run = dry_run
        self.moved_files: list[tuple[Path, Path]] = []
        self.errors: list[str] = []
        self.categories: Counter[str] = Counter()

    def validate_source(self) -> None:
        if not self.source.exists():
            raise FileNotFoundError(f"Pasta não encontrada: {self.source}")
        if not self.source.is_dir():
            raise NotADirectoryError(f"O caminho informado não é uma pasta: {self.source}")

    @staticmethod
    def unique_destination(destination: Path) -> Path:
        """Return a free filename without overwriting an existing file."""
        if not destination.exists():
            return destination

        counter = 1
        while True:
            candidate = destination.with_name(
                f"{destination.stem}_{counter}{destination.suffix}"
            )
            if not candidate.exists():
                return candidate
            counter += 1

    def organize(self) -> dict:
        """Organize top-level files and return an execution summary."""
        self.validate_source()

        files = [item for item in self.source.iterdir() if item.is_file()]

        for file_path in files:
            try:
                category = classify_file(file_path)
                folder = self.source / category
                destination = self.unique_destination(folder / file_path.name)

                if not self.dry_run:
                    folder.mkdir(exist_ok=True)
                    shutil.move(str(file_path), str(destination))

                self.moved_files.append((file_path, destination))
                self.categories[category] += 1
            except (OSError, PermissionError) as exc:
                self.errors.append(f"{file_path.name}: {exc}")

        return {
            "total_files": len(files),
            "moved_files": len(self.moved_files),
            "categories": dict(self.categories),
            "errors": list(self.errors),
            "dry_run": self.dry_run,
        }
