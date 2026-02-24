"""
Base class for HuggingFace tool integrations in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseHuggingFaceTool(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
