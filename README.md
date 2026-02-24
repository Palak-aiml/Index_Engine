
# Index Engine

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)


Index Engine is a modular, extensible framework for building, querying, and managing data indexes. Designed for flexibility and performance, it supports a variety of data sources and retrieval strategies.

## Features
- Modular index architecture
- Pluggable data sources
- Efficient querying
- Extensible with custom modules


## Installation
Clone the repository and install with pip:
```bash
git clone https://github.com/Palak-aiml/Index_Engine.git
cd Index_Engine
pip install .
```

## Usage
Add and search documents programmatically:
```python
from index_engine.core import IndexEngine
engine = IndexEngine()
engine.add_document('doc1', 'Hello world!')
print(engine.search('Hello'))
```

Or use the CLI:
```bash
python -m index_engine.cli --add doc1 "Hello world!"
python -m index_engine.cli --search Hello
```

## Documentation
See [docs/README.md](docs/README.md) for full documentation, modules, and testing instructions.

---

© 2026 Index Engine. MIT License.
