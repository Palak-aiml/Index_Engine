"""
custom_retriever.py

A custom retriever for Index Engine that supports case-insensitive search and partial matches.
"""

from typing import Dict, List

class CustomRetriever:
    """
    Custom retriever that supports case-insensitive and partial string search.
    """
    def __init__(self, index: Dict[str, str]):
        # Reference to the index (doc_id -> content)
        self.index = index

    def retrieve(self, query: str) -> List[str]:
        """
        Retrieve document IDs where the content contains the query string (case-insensitive).
        Args:
            query (str): Query string to search for.
        Returns:
            List[str]: List of matching document IDs.
        """
        query_lower = query.lower()
        return [doc_id for doc_id, content in self.index.items() if query_lower in content.lower()]
