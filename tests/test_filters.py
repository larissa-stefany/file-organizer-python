import unittest
from pathlib import Path

from src.filters import normalize_extensions, should_ignore


class FilterTests(unittest.TestCase):
    def test_normalize_extensions(self):
        self.assertEqual(normalize_extensions(["TMP", ".log"]), {".tmp", ".log"})

    def test_should_ignore_extension(self):
        ignored = normalize_extensions(["tmp"])
        self.assertTrue(should_ignore(Path("cache.TMP"), ignored))
        self.assertFalse(should_ignore(Path("report.pdf"), ignored))


if __name__ == "__main__":
    unittest.main()
