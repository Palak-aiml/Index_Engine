"""
example_usage.py

Example usage of Index Engine.
"""
from index_engine.core import IndexEngine

if __name__ == "__main__":
    engine = IndexEngine()
    engine.add_document('doc1', 'The quick brown fox jumps over the lazy dog.')
    engine.add_document('doc2', 'Hello world!')
    print("Get doc1:", engine.get_document('doc1'))
    print("Search for 'quick':", engine.search('quick'))
    print("Search for 'world':", engine.search('world'))
