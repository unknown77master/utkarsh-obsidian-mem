import json
import unittest

from src.parser import iter_json_array, parse_conversation


class ParserTests(unittest.TestCase):
    def test_parses_mapping_active_branch(self):
        payload = [{"id": "c1", "title": "Test", "current_node": "b", "mapping": {"a": {"id": "a", "parent": None, "message": {"id": "m1", "author": {"role": "user"}, "content": {"parts": ["I use Python."]}, "create_time": 1}}, "b": {"id": "b", "parent": "a", "message": {"id": "m2", "author": {"role": "assistant"}, "content": {"parts": ["Okay"]}, "create_time": 2}}}}]
        with self.subTest("stream"):
            import tempfile
            from pathlib import Path
            with tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "conversations-000.json"
                path.write_text(json.dumps(payload), encoding="utf-8")
                conversation = parse_conversation(next(iter_json_array(path)), path.name)
        self.assertEqual(conversation["id"], "c1")
        self.assertEqual([message["role"] for message in conversation["messages"]], ["user", "assistant"])
