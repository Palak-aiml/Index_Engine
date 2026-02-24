"""
Base class for OpenAI embeddings in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseOpenAIEmbedding(ABC):
    @abstractmethod
    def embed(self, text: str):
        pass
