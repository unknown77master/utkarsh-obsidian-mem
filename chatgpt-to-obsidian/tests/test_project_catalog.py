import tempfile
import unittest
from pathlib import Path

from src.project_catalog import discover_local_projects, replace_catalog_source
from src.projects import render_project_indexes


class ProjectCatalogTests(unittest.TestCase):
    def test_discovers_git_projects_but_skips_dependencies(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            project = root / "EchoQuery-RAG-based-STT"
            (project / ".git").mkdir(parents=True)
            (project / ".git" / "config").write_text('[remote "origin"]\n\turl = git@github.com:utkarsh-wadalkar/EchoQuery-RAG-based-STT.git\n', encoding="utf-8")
            (root / "node_modules" / "not-a-project" / ".git").mkdir(parents=True)
            projects = discover_local_projects([root])
            self.assertEqual(len(projects), 1)
            self.assertEqual(projects[0]["name"], "EchoQuery-RAG-based-STT")
            self.assertEqual(projects[0]["github_url"], "https://github.com/utkarsh-wadalkar/EchoQuery-RAG-based-STT")

    def test_replacing_one_source_retains_other_catalog_sources(self):
        existing = [
            {"catalog_source": "local", "catalog_root": "D:/Projects", "name": "Old"},
            {"catalog_source": "github", "github_user": "utkarsh-wadalkar", "name": "Remote"},
        ]
        result = replace_catalog_source(existing, [{"catalog_source": "local", "catalog_root": "D:/Projects", "name": "New"}], "local", "D:/Projects")
        self.assertEqual([item["name"] for item in result], ["Remote", "New"])

    def test_project_index_combines_catalog_and_chat_context(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            catalog = [{"catalog_source": "local", "catalog_root": "D:/ALL Programming", "name": "Aideo", "path": "D:/ALL Programming/aideo", "marker": ".git", "remotes": [], "github_url": None}]
            memories = [{"statement": "My project Aideo uses Python.", "category": "project", "confidence": .82, "technologies": [], "sources": []}]
            render_project_indexes(output, memories, {}, catalog)
            note = (output / "Projects" / "Aideo Project Index.md").read_text(encoding="utf-8")
            self.assertIn("## Local repositories", note)
            self.assertIn("D:/ALL Programming/aideo", note)
            self.assertIn("## Durable context", note)
