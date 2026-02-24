"""
core.py

Core indexing engine logic for Index Engine.
"""

class IndexEngine:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, content):
        """Add a document to the index."""
        self.index[doc_id] = content

    def get_document(self, doc_id):
        """Retrieve a document by its ID."""
        return self.index.get(doc_id)

    def search(self, query):
        """Basic search: returns doc_ids containing the query string."""
        return [doc_id for doc_id, content in self.index.items() if query in content]
