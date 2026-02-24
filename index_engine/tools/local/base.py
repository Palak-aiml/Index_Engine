"""
Base class for local tool integrations in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseLocalTool(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
