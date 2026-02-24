"""
Base class for SQL indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseSQLIndex(ABC):
    @abstractmethod
    def create_table(self, table_name: str, schema: dict):
        pass

    @abstractmethod
    def insert(self, table_name: str, data: dict):
        pass

    @abstractmethod
    def query(self, sql_query: str):
        pass
