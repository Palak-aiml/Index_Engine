"""
Base class for all embedding models in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseEmbedding(ABC):
    @abstractmethod
    def embed(self, text: str):
        pass
