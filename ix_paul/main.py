"""
IX-Paul CLI Entry Point

Enables terminal-based aerospace and physics queries via the command line.
Outputs knowledge directly for engineers, students, or AI collaborators.
"""

import sys
from core.query_processor import IXPaulQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your aerospace or physics question here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXPaulQueryProcessor()
    response = processor.process_query(query)

    print("\n🚀 IX-Paul Response 🚀")
    print(response)

if __name__ == "__main__":
    main()
