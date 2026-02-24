"""
Base class for all tools in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseTool(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
