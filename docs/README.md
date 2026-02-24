# Index Engine Documentation

Welcome to the Index Engine documentation!

## Overview
Index Engine is a modular, extensible framework for building and querying data indexes.

## Getting Started
- Installation instructions
- Basic usage examples


## Modules
- Core Engine
- CLI
- In-Memory Indexer
- Custom Retriever
- JSON Loader

## Testing
Run all tests with:
```bash
python -m unittest discover tests
```

## Data Integration
You can load documents from a JSON file using the JSONLoader module:
```python
from index_engine.json_loader import JSONLoader
loader = JSONLoader('sample_documents.json')
docs = loader.load_documents()
```

## Contributing
Guidelines for contributing to Index Engine.

---

© 2026 Index Engine. MIT License.
