"""
Base class for knowledge graph indices in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseKnowledgeGraphIndex(ABC):
    @abstractmethod
    def add_entity(self, entity: str, attributes: dict):
        pass

    @abstractmethod
    def add_relation(self, entity1: str, entity2: str, relation: str):
        pass

    @abstractmethod
    def query(self, entity: str):
        pass
