"""
Base class for all indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseIndex(ABC):
    @abstractmethod
    def add_document(self, doc_id: str, content: str) -> None:
        pass

    @abstractmethod
    def search(self, query: str):
        pass
