"""
Base class for vector store storage in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseVectorStoreStorage(ABC):
    @abstractmethod
    def save(self, vector_id: str, vector: list):
        pass

    @abstractmethod
    def load(self, vector_id: str):
        pass

    @abstractmethod
    def delete(self, vector_id: str):
        pass
