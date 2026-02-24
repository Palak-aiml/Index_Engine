"""
Base class for SQL retrievers in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseSQLRetriever(ABC):
    @abstractmethod
    def retrieve(self, sql_query: str):
        pass
