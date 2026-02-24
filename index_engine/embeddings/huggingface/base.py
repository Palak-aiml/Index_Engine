"""
Base class for HuggingFace embeddings in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseHuggingFaceEmbedding(ABC):
    @abstractmethod
    def embed(self, text: str):
        pass
