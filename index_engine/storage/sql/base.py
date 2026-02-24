"""
Base class for SQL storage in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseSQLStorage(ABC):
    @abstractmethod
    def save(self, table: str, data: dict):
        pass

    @abstractmethod
    def load(self, table: str, query: str):
        pass

    @abstractmethod
    def delete(self, table: str, condition: str):
        pass
