"""
Base class for keyword table indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseKeywordTableIndex(ABC):
    @abstractmethod
    def add_keyword(self, keyword: str, doc_id: str):
        pass

    @abstractmethod
    def search(self, keyword: str):
        pass
