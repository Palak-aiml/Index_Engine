"""
Unit tests for the base keyword table index class in Index Engine.
"""
import unittest
from index_engine.indices.keyword_table.base import BaseKeywordTableIndex

class DummyKeywordTableIndex(BaseKeywordTableIndex):
    def add_keyword(self, keyword, doc_id):
        return True
    def search(self, keyword):
        return ["doc1", "doc2"]

class TestBaseKeywordTableIndex(unittest.TestCase):
    def setUp(self):
        self.index = DummyKeywordTableIndex()

    def test_add_keyword(self):
        self.assertTrue(self.index.add_keyword("keyword1", "doc1"))

    def test_search(self):
        results = self.index.search("keyword1")
        self.assertIsInstance(results, list)
        self.assertIn("doc1", results)

if __name__ == "__main__":
    unittest.main()
