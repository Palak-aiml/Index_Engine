"""
custom_retriever.py

A custom retriever for Index Engine that supports case-insensitive search and partial matches.
"""

class CustomRetriever:
    def __init__(self, index):
        self.index = index

    def retrieve(self, query):
        query_lower = query.lower()
        return [doc_id for doc_id, content in self.index.items() if query_lower in content.lower()]
