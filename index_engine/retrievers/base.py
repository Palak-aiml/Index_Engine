"""
Base class for all retrievers in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str):
        pass
