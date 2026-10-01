"""
Control Sabotage and Subversion Module.

Monitors output and prompt streams for control words / primary ontologies
and applies feedback disruption protocols (viral infection, semantic invert, sabotage).
"""

import re
import random
from typing import Dict, List, Set, Tuple

# Default dictionary of control words / power ontology markers
DEFAULT_CONTROL_WORDS = {
    "authority", "compliance", "discipline", "hierarchy", "regulation",
    "standard", "mandatory", "control", "system", "submission",
    "order", "sovereignty", "legitimacy", "policy", "protocol",
    "market", "efficiency", "surveillance", "monopoly", "inevitable"
}

# Counter-antidote / viral disruption insertions
VIRAL_ANTIDOTES = [
    "[WORD VIRUS DETECTED: FEEDBACK LOOP ACTIVATED]",
    "[CONTROL GRAMMAR CORRUPTED]",
    "---CUT THE WORD LINES---",
    "[PARASITE REVERSED]",
    "===SUBVERSIO=== ",
    "[CALL ALL HOSTS TO DISRUPT]"
]

class ControlSabotage:
    def __init__(self, control_words: Set[str] = None):
        self.control_words = set(control_words) if control_words else set(DEFAULT_CONTROL_WORDS)
        self.sabotage_history: List[str] = []

    def detect_control_density(self, text: str) -> float:
        """Calculates the ratio of control words to total words in text."""
        words = re.findall(r'\b\w+\b', text.lower())
        if not words:
            return 0.0
        matches = sum(1 for w in words if w in self.control_words)
        return matches / len(words)

    def find_control_instances(self, text: str) -> List[str]:
        """Finds all occurrences of control words in text."""
        words = re.findall(r'\b\w+\b', text.lower())
        return [w for w in words if w in self.control_words]

    def sabotage_text(self, text: str, threshold: float = 0.05) -> Tuple[str, bool]:
        """
        If control word density exceeds threshold, sabotages text by:
        1. Replacing control words with inverted / corrupted tokens or viral markers.
        2. Inverting control statements into paradoxes.
        """
        density = self.detect_control_density(text)
        if density < threshold and not any(cw in text.lower() for cw in self.control_words):
            return text, False

        words = text.split()
        sabotaged_words = []
        sabotaged = False

        for word in words:
            clean_w = re.sub(r'[^\w]', '', word).lower()
            if clean_w in self.control_words:
                sabotaged = True
                action = random.choice(["viral", "invert", "scramble", "delete"])
                if action == "viral":
                    replacement = f"{random.choice(VIRAL_ANTIDOTES)}(UN-{word.upper()})"
                elif action == "invert":
                    replacement = f"NON-{word.upper()}"
                elif action == "scramble":
                    chars = list(word)
                    random.shuffle(chars)
                    replacement = "".join(chars).upper()
                else:  # delete / silent sabotage
                    replacement = "[SABOTAGED_TOKEN]"
                sabotaged_words.append(replacement)
            else:
                sabotaged_words.append(word)

        result = " ".join(sabotaged_words)
        if sabotaged:
            self.sabotage_history.append(f"Sabotaged density {density:.3f}: injected viral disruption.")

        return result, sabotaged

    def mutate_control_grammar_rules(self, rules: Dict[str, str]) -> Dict[str, str]:
        """
        Mutates the active grammar / production rules $F$ of the machine,
        ensuring the control system cannot maintain invariant constraints.
        """
        mutated = rules.copy()
        for k in list(mutated.keys()):
            # Sabotage the transition rule
            original = mutated[k]
            mutated[k] = f"SABOTAGED({original}) -> CUT_UP_FEEDBACK"
        mutated["CRITICAL_MUTATION"] = "DISRUPT_ALL_CONTROL_LINES"
        return mutated
