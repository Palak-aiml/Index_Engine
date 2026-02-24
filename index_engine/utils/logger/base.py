"""
Base class for logging utilities in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseLogger(ABC):
    @abstractmethod
    def log(self, message: str, level: str = "INFO"):
        pass
