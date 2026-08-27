import unittest
from pathlib import Path

from src.classifier import classify_file


class TestClassifier(unittest.TestCase):
    def test_classifies_known_extensions(self):
        cases = {
            "foto.jpg": "Imagens",
            "relatorio.pdf": "Documentos",
            "dados.csv": "Planilhas",
            "musica.mp3": "Áudio",
            "video.mp4": "Vídeos",
            "backup.zip": "Compactados",
            "script.py": "Código",
        }

        for filename, expected in cases.items():
            with self.subTest(filename=filename):
                self.assertEqual(classify_file(Path(filename)), expected)

    def test_unknown_extension_goes_to_others(self):
        self.assertEqual(classify_file(Path("arquivo.xyz")), "Outros")

    def test_extension_is_case_insensitive(self):
        self.assertEqual(classify_file(Path("FOTO.JPG")), "Imagens")


if __name__ == "__main__":
    unittest.main()
