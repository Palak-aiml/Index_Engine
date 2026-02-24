"""
Base class for local embeddings in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseLocalEmbedding(ABC):
    @abstractmethod
    def embed(self, text: str):
        pass
