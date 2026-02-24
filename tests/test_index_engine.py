import unittest
from index_engine.core import IndexEngine
from index_engine.in_memory_indexer import InMemoryIndexer

class TestIndexEngine(unittest.TestCase):
    def setUp(self):
        self.engine = IndexEngine()

    def test_add_and_get_document(self):
        self.engine.add_document('1', 'hello world')
        self.assertEqual(self.engine.get_document('1'), 'hello world')

    def test_search(self):
        self.engine.add_document('1', 'hello world')
        self.engine.add_document('2', 'goodbye world')
        results = self.engine.search('hello')
        self.assertIn('1', results)
        self.assertNotIn('2', results)

class TestInMemoryIndexer(unittest.TestCase):
    def setUp(self):
        self.indexer = InMemoryIndexer()

    def test_add_and_get(self):
        self.indexer.add('a', 'foo bar')
        self.assertEqual(self.indexer.get('a'), 'foo bar')

    def test_search(self):
        self.indexer.add('a', 'foo bar')
        self.indexer.add('b', 'baz qux')
        results = self.indexer.search('foo')
        self.assertIn('a', results)
        self.assertNotIn('b', results)

if __name__ == '__main__':
    unittest.main()
