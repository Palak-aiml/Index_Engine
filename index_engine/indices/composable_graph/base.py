"""
Base class for composable graph indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseComposableGraphIndex(ABC):
    @abstractmethod
    def add_node(self, node_id: str, data: dict):
        pass

    @abstractmethod
    def get_neighbors(self, node_id: str):
        pass
