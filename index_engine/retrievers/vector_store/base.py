"""
Base class for vector store retrievers in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseVectorStoreRetriever(ABC):
    @abstractmethod
    def retrieve(self, vector: list):
        pass
