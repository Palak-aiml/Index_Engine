"""
Base class for tree indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseTreeIndex(ABC):
    @abstractmethod
    def add_node(self, node_id: str, parent_id: str = None):
        pass

    @abstractmethod
    def search(self, query: str):
        pass
