import tempfile
import unittest
from pathlib import Path

from examples.path_safety import UnsafePathError, read_text_within


class ReadTextWithinTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.allowed = self.base / "allowed"
        self.allowed.mkdir()
        (self.allowed / "note.txt").write_text("synthetic data", encoding="utf-8")
        (self.base / "outside.txt").write_text("not authorized", encoding="utf-8")

    def test_reads_authorized_file(self):
        self.assertEqual(read_text_within(self.allowed, "note.txt"), "synthetic data")

    def test_blocks_parent_traversal(self):
        with self.assertRaises(UnsafePathError):
            read_text_within(self.allowed, "../outside.txt")

    def test_blocks_absolute_external_path(self):
        with self.assertRaises(UnsafePathError):
            read_text_within(self.allowed, str(self.base / "outside.txt"))

    def test_blocks_symlink_to_external_file(self):
        link = self.allowed / "external-link.txt"
        try:
            link.symlink_to(self.base / "outside.txt")
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable")
        with self.assertRaises(UnsafePathError):
            read_text_within(self.allowed, link.name)

    def test_rejects_directory(self):
        with self.assertRaises(IsADirectoryError):
            read_text_within(self.allowed, ".")


if __name__ == "__main__":
    unittest.main()
