"""
Base class for configuration utilities in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseConfig(ABC):
    @abstractmethod
    def load_config(self, config_path: str):
        pass

    @abstractmethod
    def save_config(self, config_path: str, config: dict):
        pass
