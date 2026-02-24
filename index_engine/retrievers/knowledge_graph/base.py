"""
Base class for knowledge graph retrievers in Index Engine.
"""
from abc import ABC, abstractmethod

class BaseKnowledgeGraphRetriever(ABC):
    @abstractmethod
    def retrieve_entity(self, entity: str):
        pass

    @abstractmethod
    def retrieve_relation(self, entity1: str, entity2: str):
        pass
