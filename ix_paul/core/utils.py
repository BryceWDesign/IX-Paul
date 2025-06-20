"""
IX-Paul Utilities Module

Helper functions for cleaning and validating aerospace-related queries.
Ensures clarity and processing consistency within the domain-specific framework.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize the query: strip whitespace, condense spaces, and remove unwanted symbols.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\+\=\(\)\[\]\.:]+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Validates that the query is meaningful enough to process.
    """
    return bool(query and len(query) > 3 and any(c.isalpha() for c in query))

# Example usage
if __name__ == "__main__":
    sample_queries = [
        "   What is orbital velocity?   ",
        "???",
        "Delta-V",
        "Explain ramjet!"
    ]

    for q in sample_queries:
        cleaned = clean_query(q)
        valid = is_valid_query(cleaned)
        print(f"Original: '{q}' → Cleaned: '{cleaned}' | Valid: {valid}")
