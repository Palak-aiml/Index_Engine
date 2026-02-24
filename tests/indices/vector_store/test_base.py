"""
Unit tests for the base vector store index class in Index Engine.
"""
import unittest
from index_engine.indices.vector_store.base import BaseVectorStoreIndex

class DummyVectorStoreIndex(BaseVectorStoreIndex):
    def add_vector(self, vector, doc_id):
        return True
    def search(self, vector):
        return ["doc1", "doc2"]

class TestBaseVectorStoreIndex(unittest.TestCase):
    def setUp(self):
        self.index = DummyVectorStoreIndex()

    def test_add_vector(self):
        self.assertTrue(self.index.add_vector([0.1, 0.2], "doc1"))

    def test_search(self):
        results = self.index.search([0.1, 0.2])
        self.assertIsInstance(results, list)
        self.assertIn("doc1", results)

if __name__ == "__main__":
    unittest.main()
