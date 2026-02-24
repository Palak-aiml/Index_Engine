import argparse
from index_engine.core import IndexEngine


def main():
    parser = argparse.ArgumentParser(description="Index Engine CLI")
    parser.add_argument('--add', nargs=2, metavar=('DOC_ID', 'CONTENT'), help='Add a document to the index')
    parser.add_argument('--get', metavar='DOC_ID', help='Get a document by ID')
    parser.add_argument('--search', metavar='QUERY', help='Search for documents containing a query string')
    args = parser.parse_args()

    engine = IndexEngine()

    if args.add:
        doc_id, content = args.add
        engine.add_document(doc_id, content)
        print(f"Added document {doc_id}")
    elif args.get:
        doc = engine.get_document(args.get)
        print(doc if doc else "Document not found.")
    elif args.search:
        results = engine.search(args.search)
        print("Found document IDs:", results)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
