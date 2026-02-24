"""
Base class for all storage backends in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseStorage(ABC):
    @abstractmethod
    def save(self, doc_id: str, content: str) -> None:
        pass

    @abstractmethod
    def load(self, doc_id: str):
        pass
