"""
Base class for vector store indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseVectorStoreIndex(ABC):
    @abstractmethod
    def add_vector(self, doc_id: str, vector):
        pass

    @abstractmethod
    def search(self, query_vector, top_k: int = 5):
        pass
