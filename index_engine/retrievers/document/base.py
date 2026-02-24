"""
Base class for document retrievers in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseDocumentRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str):
        pass
