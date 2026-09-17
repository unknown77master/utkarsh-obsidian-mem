import tempfile
import unittest
from pathlib import Path

from src.archive import archive_conversation, render_archive_indexes


class ArchiveTests(unittest.TestCase):
    def test_writes_searchable_conversation_markdown(self):
        conversation = {"id": "conversation-1", "title": "A/B", "created_at": 1_704_067_200, "updated_at": 1_704_067_300, "messages": [{"role": "user", "content": "Hello [[literal]]"}, {"role": "assistant", "content": "Hi"}]}
        with tempfile.TemporaryDirectory() as directory:
            path = archive_conversation(Path(directory), conversation)
            content = path.read_text(encoding="utf-8")
        self.assertTrue(path.name.startswith("A-B--conversation"))
        self.assertIn("Archive/2024/2024-01-01", path.as_posix())
        self.assertIn("type: \"chatgpt-conversation\"", content)
        self.assertIn("## User", content)
        self.assertIn("## Assistant", content)
        self.assertIn("\\[\\[literal\\]\\]", content)

    def test_title_change_replaces_the_prior_generated_archive(self):
        conversation = {"id": "conversation-1", "title": "Old title", "created_at": 1_704_067_200, "updated_at": 1_704_067_300, "messages": []}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            old = archive_conversation(output, conversation)
            conversation["title"] = "New title"
            new = archive_conversation(output, conversation, old.relative_to(output).as_posix())
            self.assertFalse(old.exists())
            self.assertTrue(new.exists())

    def test_creates_year_and_date_indexes_for_every_transcript(self):
        conversations = [
            {"id": "one", "title": "First", "created_at": 1_704_067_200, "messages": []},
            {"id": "two", "title": "Second", "created_at": 1_704_153_600, "messages": []},
        ]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            paths = {item["id"]: archive_conversation(output, item).relative_to(output).as_posix() for item in conversations}
            indexes = render_archive_indexes(output, paths)
            date_index = output / "Archive" / "2024" / "2024-01-02" / "2024-01-02 Chat Index.md"
            self.assertIn("Archive/2024/2024-01-01/2024-01-01 Chat Index.md", indexes)
            self.assertTrue(date_index.is_file())
            self.assertIn("[[Archive/2024/2024-01-02/Second--two|Second]]", date_index.read_text(encoding="utf-8"))
            self.assertFalse((output / "Archive" / "README.md").exists())
