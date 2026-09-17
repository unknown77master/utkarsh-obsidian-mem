import unittest

from src.normalizer import normalize_conversation


class NormalizerTests(unittest.TestCase):
    def test_removes_empty_and_adjacent_duplicate_messages(self):
        result = normalize_conversation({"id": "1", "title": "  A   title ", "messages": [{"role": "user", "content": "  hello  "}, {"role": "user", "content": "hello"}, {"role": "assistant", "content": ""}]})
        self.assertEqual(result["title"], "A title")
        self.assertEqual(len(result["messages"]), 1)
        self.assertTrue(result["fingerprint"])
