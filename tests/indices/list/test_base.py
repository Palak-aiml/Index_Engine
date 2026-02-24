"""
Unit tests for the base list index class in Index Engine.
"""
import unittest
from index_engine.indices.list.base import BaseListIndex

class DummyListIndex(BaseListIndex):
    def add_item(self, item):
        return True
    def search(self, query):
        return ["item1", "item2"]

class TestBaseListIndex(unittest.TestCase):
    def setUp(self):
        self.index = DummyListIndex()

    def test_add_item(self):
        self.assertTrue(self.index.add_item("item1"))

    def test_search(self):
        results = self.index.search("item1")
        self.assertIsInstance(results, list)
        self.assertIn("item1", results)

if __name__ == "__main__":
    unittest.main()
