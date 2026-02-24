"""
Unit tests for the base tree index class in Index Engine.
"""
import unittest
from index_engine.indices.tree.base import BaseTreeIndex

class DummyTreeIndex(BaseTreeIndex):
    def add_node(self, node, parent=None):
        return True
    def search(self, query):
        return ["node1", "node2"]

class TestBaseTreeIndex(unittest.TestCase):
    def setUp(self):
        self.index = DummyTreeIndex()

    def test_add_node(self):
        self.assertTrue(self.index.add_node("node1"))

    def test_search(self):
        results = self.index.search("node1")
        self.assertIsInstance(results, list)
        self.assertIn("node1", results)

if __name__ == "__main__":
    unittest.main()
