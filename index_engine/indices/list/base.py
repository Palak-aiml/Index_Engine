"""
Base class for list indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseListIndex(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def search(self, query: str):
        pass
