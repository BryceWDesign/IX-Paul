"""
IX-Paul Domain-Specific Query Processor

Handles aerospace and advanced physics queries using specialized knowledge modules.
Part of the IX-Gibson AI multi-specialist framework.
"""

from aero_physics_knowledge import AeroPhysicsKnowledge

class IXPaulQueryProcessor:
    def __init__(self):
        self.knowledge = AeroPhysicsKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        if query_lower.startswith("what is "):
            term = query_lower[8:].strip()
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return (
                "I am IX-Paul, aerospace and physics specialist. "
                "Ask me to define or explain concepts like propulsion, thermodynamics, or orbital mechanics."
            )

# Example usage
if __name__ == "__main__":
    processor = IXPaulQueryProcessor()
    print(processor.process_query("What is delta-v?"))
    print(processor.process_query("Define ramjet"))
    print(processor.process_query("Explain composite materials"))
