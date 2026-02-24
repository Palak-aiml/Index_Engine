"""
Base class for OpenAI tool integrations in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseOpenAITool(ABC):
    @abstractmethod
    def run(self, *args, **kwargs):
        pass
