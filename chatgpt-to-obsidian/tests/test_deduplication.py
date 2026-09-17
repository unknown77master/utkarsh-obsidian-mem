import unittest

from src.deduplicator import merge_candidate, resolve_current_environment


class DeduplicationTests(unittest.TestCase):
    def test_merges_equivalent_explicit_memory(self):
        memories = [{"statement": "I use React and Vite.", "category": "technical_context", "confidence": .82, "technologies": ["React"], "sources": [{"conversation_id": "one"}]}]
        candidate = {"statement": "I use Vite and React.", "category": "technical_context", "confidence": .9, "technologies": ["Vite"], "sources": [{"conversation_id": "two"}]}
        self.assertTrue(merge_candidate(memories, candidate))
        self.assertEqual(len(memories), 1)
        self.assertEqual(len(memories[0]["sources"]), 2)

    def test_marks_newer_explicit_environment_as_current(self):
        memories = [
            {"statement": "I use Windows 10.", "category": "environment", "sources": [{"timestamp": 1}]},
            {"statement": "I use Windows 11.", "category": "environment", "sources": [{"timestamp": 2}]},
        ]
        resolve_current_environment(memories)
        self.assertEqual(memories[0]["status"], "historical")
        self.assertEqual(memories[1]["status"], "current")
