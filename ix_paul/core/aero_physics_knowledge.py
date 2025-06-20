"""
IX-Paul Core Aerospace and Physics Knowledge Module

Contains essential definitions and reference knowledge covering:
- Aerospace systems
- Thermodynamics
- Materials science
- Space propulsion
- Orbital mechanics

Part of the IX-Gibson sibling AI network.
"""

class AeroPhysicsKnowledge:
    def __init__(self):
        self.facts = {
            "orbital velocity": "The minimum velocity an object must have to stay in orbit around a celestial body without propulsion.",
            "specific impulse": "A measure of how efficiently a rocket uses propellant; higher values indicate better performance.",
            "ramjet": "An air-breathing jet engine that uses forward motion to compress incoming air without turbines.",
            "delta-v": "The change in velocity required for a maneuver in spaceflight; a key metric in orbital transfers.",
            "thermal expansion": "The increase in a material's volume in response to temperature rise, critical in aerospace design.",
            "composite materials": "Engineered materials made from two or more constituent materials with significantly different properties.",
            "aerodynamic drag": "A force opposing an object's motion through air, dependent on shape, velocity, and air density.",
            "reentry heat shield": "A protective barrier designed to absorb and dissipate the intense heat during atmospheric reentry."
        }

    def get_fact(self, term: str) -> str:
        term_lower = term.lower().strip()
        return self.facts.get(term_lower, f"Sorry, I don't yet have information on '{term}'.")

# Example test
if __name__ == "__main__":
    ak = AeroPhysicsKnowledge()
    print(ak.get_fact("delta-v"))
    print(ak.get_fact("ramjet"))
    print(ak.get_fact("dark matter"))
