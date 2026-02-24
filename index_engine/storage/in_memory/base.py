"""
Base class for in-memory storage in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseInMemoryStorage(ABC):
    @abstractmethod
    def save(self, key: str, value: object):
        pass

    @abstractmethod
    def load(self, key: str):
        pass

    @abstractmethod
    def delete(self, key: str):
        pass
