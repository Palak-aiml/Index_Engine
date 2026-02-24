"""
Base class for file system storage in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseFileSystemStorage(ABC):
    @abstractmethod
    def save(self, file_path: str, data: bytes):
        pass

    @abstractmethod
    def load(self, file_path: str):
        pass

    @abstractmethod
    def delete(self, file_path: str):
        pass
