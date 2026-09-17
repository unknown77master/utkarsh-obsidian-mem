import tempfile
import unittest
from pathlib import Path

from src.archive import archive_conversation
from src.resources import AssetCatalog


class ResourceTests(unittest.TestCase):
    def test_transcript_links_local_and_external_resources_and_marks_unresolved(self):
        conversation = {
            "id": "resources-1", "title": "Resource chat", "created_at": 1_704_067_200, "messages": [{
                "role": "user", "content": "Please inspect these.", "metadata": {
                    "attachments": [{"id": "file-photo", "name": "Photo.png"}, {"id": "file-missing", "name": "Missing.pdf"}],
                    "content_references": [{"title": "Reference site", "url": "https://example.com/reference"}],
                },
            }],
        }
        with tempfile.TemporaryDirectory() as directory:
            path = archive_conversation(Path(directory), conversation, catalog=AssetCatalog({"file-photo.dat": "Photo.png"}))
            content = path.read_text(encoding="utf-8")
        self.assertIn("## Resources", content)
        self.assertIn("[Photo.png](../../../Raw/Export/file-photo.dat)", content)
        self.assertIn("[Reference site](https://example.com/reference)", content)
        self.assertIn("`file-missing`", content)
