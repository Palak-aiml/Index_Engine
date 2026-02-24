"""
json_loader.py

Loads documents from a JSON file for Index Engine.
"""
import json

class JSONLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_documents(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Expects a list of dicts with 'id' and 'content' keys
        return [(doc['id'], doc['content']) for doc in data]
