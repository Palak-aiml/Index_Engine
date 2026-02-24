"""
in_memory_indexer.py

A simple in-memory indexer for Index Engine.
"""

class InMemoryIndexer:
    def __init__(self):
        self.index = {}

    def add(self, doc_id, content):
        self.index[doc_id] = content

    def get(self, doc_id):
        return self.index.get(doc_id)

    def search(self, query):
        return [doc_id for doc_id, content in self.index.items() if query in content]
