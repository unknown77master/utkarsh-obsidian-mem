import unittest

from src.obsidian import render_vault
from src.projects import _project_names


class ObsidianTests(unittest.TestCase):
    def test_writes_index_and_only_valid_technology_links(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            created = render_vault(target, [{"statement": "I use Python.", "category": "technical_context", "confidence": .82, "technologies": ["Python"], "sources": [{"conversation_id": "one", "title": "Source"}]}], {})
            self.assertIn(target / "00 - Index.md", created)
            self.assertTrue((target / "Technologies" / "Python.md").is_file())
            self.assertIn("[[Technologies/Python]]", (target / "04 - Programming & Tech.md").read_text(encoding="utf-8"))
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / "00 - Agent Memory.md").is_file())
            self.assertTrue((target / "Projects" / "Projects Index.md").is_file())
            self.assertTrue((target / "Raw" / "Raw Export Mirror.md").is_file())
            self.assertFalse((target / "Projects" / "README.md").exists())
            index = (target / "00 - Index.md").read_text(encoding="utf-8")
            self.assertIn("## Chats", index)
            self.assertIn("## Resources", index)
            self.assertIn("[[Projects/Projects Index]]", index)

    def test_projects_have_indexes_chats_and_resources(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            archive = target / "Archive" / "2026" / "2026-01-09"
            archive.mkdir(parents=True)
            (archive / "Audora--one.md").write_text("# Audora\n\n## Resources\n", encoding="utf-8")
            memories = [
                {"statement": "My project Audora uses Python.", "category": "project", "confidence": .82, "technologies": ["Python"], "sources": [{"conversation_id": "one", "title": "Audora planning"}]},
                {"statement": "I want to write down the problem statement for my project.", "category": "project", "confidence": .82, "technologies": [], "sources": [{"conversation_id": "two", "title": "Project planning"}]},
            ]
            render_vault(target, memories, {}, {"one": "Archive/2026/2026-01-09/Audora--one.md"})
            root = (target / "Projects" / "Projects Index.md").read_text(encoding="utf-8")
            audora = (target / "Projects" / "Audora Project Index.md").read_text(encoding="utf-8")
            unclassified = (target / "Projects" / "Unclassified Project Discussions Project Index.md").read_text(encoding="utf-8")
            self.assertIn("[[Projects/Audora Project Index|Audora]]", root)
            self.assertIn("[[Archive/2026/2026-01-09/Audora--one|Audora planning]]", audora)
            self.assertIn("[[Archive/2026/2026-01-09/Audora--one#Resources|Audora planning resources]]", audora)
            self.assertIn("invented project name", unclassified)

    def test_project_name_detection_stays_conservative(self):
        self.assertEqual(_project_names("My project Audora uses Python."), ["Audora"])
        self.assertEqual(_project_names("I am coding this OCR GST project."), ["OCR GST"])
        self.assertEqual(_project_names("Craft a resume and add my project."), [])

    def test_stale_generated_project_indexes_are_removed(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            audora = [{"statement": "My project Audora uses Python.", "category": "project", "confidence": .82, "technologies": [], "sources": []}]
            aideo = [{"statement": "My project Aideo uses Python.", "category": "project", "confidence": .82, "technologies": [], "sources": []}]
            render_vault(target, audora, {})
            self.assertTrue((target / "Projects" / "Audora Project Index.md").exists())
            render_vault(target, aideo, {})
            self.assertFalse((target / "Projects" / "Audora Project Index.md").exists())
            self.assertTrue((target / "Projects" / "Aideo Project Index.md").exists())
