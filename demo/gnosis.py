"""
Gnosis Layer: Hirsch-Grade Latent Meaning and Pattern Extractor.

Performs latent semantic extraction, "Third Mind" insight synthesis,
and pattern revelation from chaotic, cut-up output streams without requiring
external heavy weights, using symbolic/NLP heuristic algorithms.
"""

import re
import math
from collections import Counter
from typing import Dict, List, Any, Tuple, Set

class GnosisExtractor:
    def __init__(self, key_concept_depth: int = 5):
        self.key_concept_depth = key_concept_depth
        self.stop_words = {
            "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
            "with", "by", "from", "of", "is", "was", "are", "were", "be", "been",
            "being", "have", "has", "had", "this", "that", "these", "those", "it"
        }

    def extract_keywords(self, text: str, top_n: int = 8) -> List[Tuple[str, int]]:
        """Extracts key terms while ignoring common stop words and markup tags."""
        # Clean tags like [PARASITE REVERSED]
        clean_text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
        words = re.findall(r'\b[a-zA-Z]{3,}\b', clean_text.lower())
        words = [w for w in words if w not in self.stop_words]
        counts = Counter(words)
        return counts.most_common(top_n)

    def extract_juxtaposition_pairs(self, text: str) -> List[Tuple[str, str]]:
        """
        Extracts adjacent or juxtaposed noun/concept pairs from chaotic text.
        Identifies collision points between disparate semantic domains.
        """
        clean_text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
        words = re.findall(r'\b[a-zA-Z]{3,}\b', clean_text)
        pairs = []
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if w1.lower() not in self.stop_words and w2.lower() not in self.stop_words:
                if w1.lower() != w2.lower():
                    pairs.append((w1, w2))
        return pairs[:10]

    def synthesize_third_mind_insights(self, text: str) -> List[str]:
        """
        'Third Mind' Synthesis:
        Extracts emergent, latent philosophical insights that arise from the fusion of inputs.
        """
        keywords = [kw for kw, count in self.extract_keywords(text, top_n=6)]
        pairs = self.extract_juxtaposition_pairs(text)

        insights = []

        if len(keywords) >= 2:
            insights.append(
                f"Emergent Synthesis: Collision between '{keywords[0]}' and '{keywords[1]}' "
                f"exposes the latent power structure within the discourse."
            )

        if pairs:
            p1, p2 = pairs[0]
            insights.append(
                f"Juxtaposition Insight: Unsettling alignment of [{p1}] <---> [{p2}] "
                f"shatters normative linear causality and reveals implicit ideological assumptions."
            )

        if any("virus" in text.lower() or "line" in text.lower() for _ in [0]):
            insights.append(
                "Viral Archaeology: The word-lines of established authority are experiencing "
                "destructive feedback and parasitic inversion."
            )

        if len(keywords) >= 4:
            insights.append(
                f"Epistemic Metanoia: Cluster [{', '.join(keywords[2:5])}] indicates "
                f"a structural rupture in the primary ontology."
            )

        return insights

    def analyze_cut_up(self, text: str) -> Dict[str, Any]:
        """Runs full Gnosis extraction analysis on a Burroughs machine text output."""
        keywords = self.extract_keywords(text)
        pairs = self.extract_juxtaposition_pairs(text)
        insights = self.synthesize_third_mind_insights(text)

        return {
            "top_keywords": keywords,
            "juxtaposition_pairs": pairs,
            "third_mind_insights": insights,
            "revelation_score": round(min(1.0, len(keywords) * 0.1 + len(pairs) * 0.05), 3)
        }
