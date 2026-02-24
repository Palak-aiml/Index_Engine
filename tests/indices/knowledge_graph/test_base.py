"""
Unit tests for the base knowledge graph index class in Index Engine.
"""
import unittest
from index_engine.indices.knowledge_graph.base import BaseKnowledgeGraphIndex

class DummyKnowledgeGraphIndex(BaseKnowledgeGraphIndex):
    def add_entity(self, entity, attributes):
        return True
    def add_relation(self, entity1, entity2, relation):
        return True
    def query(self, entity):
        return ["entity1", "entity2"]

class TestBaseKnowledgeGraphIndex(unittest.TestCase):
    def setUp(self):
        self.index = DummyKnowledgeGraphIndex()

    def test_add_entity(self):
        self.assertTrue(self.index.add_entity("entity1", {}))

    def test_add_relation(self):
        self.assertTrue(self.index.add_relation("entity1", "entity2", "related_to"))

    def test_query(self):
        results = self.index.query("entity1")
        self.assertIsInstance(results, list)
        self.assertIn("entity1", results)

if __name__ == "__main__":
    unittest.main()
