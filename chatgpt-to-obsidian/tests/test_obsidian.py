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
            self.assertIn("[Python](<Technologies/Python.md>)", (target / "04 - Programming & Tech.md").read_text(encoding="utf-8"))
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / "00 - Agent Memory.md").is_file())
            self.assertTrue((target / "Projects" / "Projects Index.md").is_file())
            self.assertTrue((target / "Raw" / "Raw Export Mirror.md").is_file())
            self.assertFalse((target / "Projects" / "README.md").exists())
            index = (target / "00 - Index.md").read_text(encoding="utf-8")
            self.assertIn("## Chats and resources", index)
            self.assertIn("[Projects Index](<Projects/Projects Index.md>)", index)

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
            self.assertIn("[Audora](<Audora Project Index.md>)", root)
            self.assertIn("[Audora planning](<../Archive/2026/2026-01-09/Audora--one.md>)", audora)
            self.assertIn("[Audora planning resources](<../Archive/2026/2026-01-09/Audora--one.md#Resources>)", audora)
            self.assertIn("invented project name", unclassified)

    def test_project_name_detection_stays_conservative(self):
        self.assertEqual(_project_names("My project Audora uses Python."), ["Audora"])
        self.assertEqual(_project_names("I am coding this OCR GST project."), ["OCR GST"])
        self.assertEqual(_project_names("Craft a resume and add my project."), [])

    def test_maintained_project_home_is_visible_despite_zero_extracted_context(self):
        import tempfile
        from pathlib import Path
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            home = target / "Projects" / "KaushalVaani" / "Project Home.md"
            home.parent.mkdir(parents=True)
            home.write_text("# KaushalVaani\n", encoding="utf-8")
            catalog = [{"name": "KaushalVaani", "github_url": "https://github.com/example/KaushalVaani"}]
            render_vault(target, [], {}, {}, catalog)
            root = (target / "Projects" / "Projects Index.md").read_text(encoding="utf-8")
            project = (target / "Projects" / "KaushalVaani Project Index.md").read_text(encoding="utf-8")
            self.assertIn("[KaushalVaani](<KaushalVaani/Project Home.md>)", root)
            self.assertIn("[KaushalVaani Project Home](<KaushalVaani/Project Home.md>)", project)
            self.assertIn("No statements were automatically assigned", project)

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
