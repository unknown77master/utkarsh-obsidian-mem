import argparse
import json
import tempfile
import unittest
from pathlib import Path

from migrate import run


class IncrementalArchiveTests(unittest.TestCase):
    def test_archive_is_written_for_an_unchanged_conversation(self):
        record = [{"id": "c1", "title": "Title", "create_time": 1_704_067_200, "current_node": "n1", "mapping": {"n1": {"id": "n1", "parent": None, "message": {"id": "m1", "author": {"role": "user"}, "content": {"parts": ["I use Python for projects."]}, "create_time": 1_704_067_200}}}}]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / "export", root / "vault"
            source.mkdir()
            (source / "conversations-000.json").write_text(json.dumps(record), encoding="utf-8")
            self.assertEqual(run(argparse.Namespace(source=source, output=output, dry_run=False, archive_conversations=False)), 0)
            self.assertEqual(run(argparse.Namespace(source=source, output=output, dry_run=False, archive_conversations=True)), 0)
            self.assertTrue((output / "Archive" / "2024" / "2024-01-01" / "Title--c1.md").is_file())
