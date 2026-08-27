import tempfile
import unittest
from pathlib import Path

from src.organizer import FileOrganizer


class TestFileOrganizer(unittest.TestCase):
    def test_moves_files_to_expected_categories(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "foto.jpg").write_text("imagem", encoding="utf-8")
            (root / "relatorio.pdf").write_text("pdf", encoding="utf-8")

            summary = FileOrganizer(root).organize()

            self.assertEqual(summary["moved_files"], 2)
            self.assertTrue((root / "Imagens" / "foto.jpg").exists())
            self.assertTrue((root / "Documentos" / "relatorio.pdf").exists())

    def test_dry_run_does_not_move_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            file_path = root / "foto.jpg"
            file_path.write_text("imagem", encoding="utf-8")

            summary = FileOrganizer(root, dry_run=True).organize()

            self.assertTrue(file_path.exists())
            self.assertEqual(summary["moved_files"], 1)
            self.assertTrue(summary["dry_run"])

    def test_unique_destination_adds_counter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            existing = root / "arquivo.txt"
            existing.write_text("original", encoding="utf-8")

            candidate = FileOrganizer.unique_destination(existing)

            self.assertEqual(candidate.name, "arquivo_1.txt")


if __name__ == "__main__":
    unittest.main()
