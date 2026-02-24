"""
Unit tests for the base composable graph index class in Index Engine.
"""
import unittest
from index_engine.indices.composable_graph.base import BaseComposableGraphIndex

class DummyComposableGraphIndex(BaseComposableGraphIndex):
    def add_node(self, node_id, data):
        return True
    def get_neighbors(self, node_id):
        return ["node2", "node3"]

class TestBaseComposableGraphIndex(unittest.TestCase):
    def setUp(self):
        self.index = DummyComposableGraphIndex()

    def test_add_node(self):
        self.assertTrue(self.index.add_node("node1", {}))

    def test_get_neighbors(self):
        results = self.index.get_neighbors("node1")
        self.assertIsInstance(results, list)
        self.assertIn("node2", results)

if __name__ == "__main__":
    unittest.main()
