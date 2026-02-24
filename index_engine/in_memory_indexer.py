"""
in_memory_indexer.py

A simple in-memory indexer for Index Engine.
"""

from typing import Dict, List, Optional

class InMemoryIndexer:
    """
    Simple in-memory indexer for storing and searching documents.
    """
    def __init__(self):
        # Internal index: maps doc_id to content
        self.index: Dict[str, str] = {}

    def add(self, doc_id: str, content: str) -> None:
        """
        Add a document to the index.
        Args:
            doc_id (str): Unique identifier for the document.
            content (str): The content of the document.
        """
        self.index[doc_id] = content

    def get(self, doc_id: str) -> Optional[str]:
        """
        Retrieve a document by its ID.
        Args:
            doc_id (str): Unique identifier for the document.
        Returns:
            Optional[str]: The document content if found, else None.
        """
        return self.index.get(doc_id)

    def search(self, query: str) -> List[str]:
        """
        Search for documents containing the query string.
        Args:
            query (str): Query string to search for.
        Returns:
            List[str]: List of document IDs containing the query.
        """
        return [doc_id for doc_id, content in self.index.items() if query in content]
