import unittest
from index_engine.custom_retriever import CustomRetriever
from index_engine.json_loader import JSONLoader
import os

class TestCustomRetriever(unittest.TestCase):
    def setUp(self):
        self.index = {
            '1': 'Hello World',
            '2': 'hello universe',
            '3': 'Goodbye world'
        }
        self.retriever = CustomRetriever(self.index)

    def test_case_insensitive_search(self):
        results = self.retriever.retrieve('hello')
        self.assertIn('1', results)
        self.assertIn('2', results)

    def test_partial_match(self):
        results = self.retriever.retrieve('world')
        self.assertIn('1', results)
        self.assertIn('3', results)

class TestJSONLoader(unittest.TestCase):
    def setUp(self):
        self.filepath = 'sample_documents.json'
        # Ensure file exists for test
        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write('[{"id": "a", "content": "foo"}, {"id": "b", "content": "bar"}]')
        self.loader = JSONLoader(self.filepath)

    def tearDown(self):
        os.remove(self.filepath)

    def test_load_documents(self):
        docs = self.loader.load_documents()
        self.assertEqual(len(docs), 2)
        self.assertEqual(docs[0], ('a', 'foo'))
        self.assertEqual(docs[1], ('b', 'bar'))

if __name__ == '__main__':
    unittest.main()
