import tempfile
import unittest
from pathlib import Path

from src.preservation import mirror_export


class PreservationTests(unittest.TestCase):
    def test_mirrors_binary_files_incrementally_and_removes_stale_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / "export", root / "vault"
            nested = source / "nested"
            nested.mkdir(parents=True)
            binary = nested / "attachment.dat"
            binary.write_bytes(b"\x00binary\xff")
            first = mirror_export(source, output)
            mirrored = output / "Raw" / "Export" / "nested" / "attachment.dat"
            self.assertEqual((first.files, first.copied, first.skipped), (1, 1, 0))
            self.assertEqual(mirrored.read_bytes(), b"\x00binary\xff")
            second = mirror_export(source, output)
            self.assertEqual((second.copied, second.skipped), (0, 1))
            binary.write_bytes(b"changed")
            changed = mirror_export(source, output)
            self.assertEqual(changed.copied, 1)
            self.assertEqual(mirrored.read_bytes(), b"changed")
            binary.unlink()
            removed = mirror_export(source, output)
            self.assertEqual(removed.removed, 1)
            self.assertFalse(mirrored.exists())
