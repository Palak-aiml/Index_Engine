#!/usr/bin/env python3
"""
load_and_index_json.py

Utility script to load documents from a JSON file and index them using Index Engine.
"""
from index_engine.core import IndexEngine
from index_engine.json_loader import JSONLoader
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/load_and_index_json.py <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    loader = JSONLoader(json_file)
    docs = loader.load_documents()
    engine = IndexEngine()
    for doc_id, content in docs:
        engine.add_document(doc_id, content)
    print(f"Indexed {len(docs)} documents from {json_file}.")
