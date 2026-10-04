"""
Gnosis Layer: Hirsch-Grade Hermeneutic & Co-Occurrence Graph Meaning Extractor.

Implements E.D. Hirsch's distinction between textual Meaning (verbal intention)
and Significance (contextual relation), paired with word co-occurrence graph analysis
(degree centrality, PageRank, and community hub detection).
"""

import re
import math
from collections import Counter
from typing import Dict, List, Any, Tuple, Set

class CoOccurrenceGraph:
    """Pure Python Word Co-Occurrence Graph Analytics."""
    def __init__(self, window_size: int = 4):
        self.window_size = window_size
        self.nodes: Set[str] = set()
        self.edges: Dict[Tuple[str, str], int] = {}
        self.adjacency: Dict[str, Set[str]] = {}

    def build_graph(self, words: List[str]) -> None:
        """Constructs undirected weighted co-occurrence graph from word tokens."""
        self.nodes = set(words)
        self.edges = {}
        self.adjacency = {w: set() for w in self.nodes}

        for i in range(len(words)):
            w1 = words[i]
            for j in range(i + 1, min(i + self.window_size, len(words))):
                w2 = words[j]
                if w1 != w2:
                    pair = tuple(sorted([w1, w2]))
                    self.edges[pair] = self.edges.get(pair, 0) + 1
                    self.adjacency[w1].add(w2)
                    self.adjacency[w2].add(w1)

    def calculate_degree_centrality(self) -> Dict[str, float]:
        """Calculates degree centrality for each node."""
        if not self.nodes:
            return {}
        n = len(self.nodes) - 1 or 1
        return {node: len(neighbors) / n for node, neighbors in self.adjacency.items()}

    def calculate_pagerank(self, damping: float = 0.85, max_iter: int = 20) -> Dict[str, float]:
        """Calculates PageRank over co-occurrence graph."""
        if not self.nodes:
            return {}
        num_nodes = len(self.nodes)
        pr = {node: 1.0 / num_nodes for node in self.nodes}

        for _ in range(max_iter):
            new_pr = {}
            for node in self.nodes:
                rank_sum = 0.0
                for neighbor in self.adjacency[node]:
                    out_deg = len(self.adjacency[neighbor]) or 1
                    rank_sum += pr[neighbor] / out_deg
                new_pr[node] = (1.0 - damping) / num_nodes + damping * rank_sum
            pr = new_pr

        return pr

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
        clean_text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
        words = re.findall(r'\b[a-zA-Z]{3,}\b', clean_text.lower())
        words = [w for w in words if w not in self.stop_words]
        counts = Counter(words)
        return counts.most_common(top_n)

    def extract_juxtaposition_pairs(self, text: str) -> List[Tuple[str, str]]:
        """Extracts adjacent or juxtaposed noun/concept pairs from chaotic text."""
        clean_text = re.sub(r'\[.*?\]|\(.*?\)', '', text)
        words = re.findall(r'\b[a-zA-Z]{3,}\b', clean_text)
        pairs = []
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if w1.lower() not in self.stop_words and w2.lower() not in self.stop_words:
                if w1.lower() != w2.lower():
                    pairs.append((w1, w2))
        return pairs[:10]

    def hirsch_hermeneutic_analysis(self, text: str, context_topic: str = "Control System") -> Dict[str, Any]:
        """
        Applies E.D. Hirsch's Hermeneutic Framework:
        - Verbal Meaning: Fixed, intrinsic semantic relation of cut-up tokens.
        - Significance: Dynamic, contextual relationship to target domain.
        """
        clean_words = [w.lower() for w in re.findall(r'\b[a-zA-Z]{3,}\b', text) if w.lower() not in self.stop_words]
        graph = CoOccurrenceGraph()
        graph.build_graph(clean_words)

        pr_scores = graph.calculate_pagerank()
        sorted_pr = sorted(pr_scores.items(), key=lambda x: x[1], reverse=True)

        top_hubs = [node for node, score in sorted_pr[:5]]

        # Meaning vs Significance
        verbal_meaning = f"Literal textual output generated from cut-up token stream [{', '.join(clean_words[:6])}]."
        significance = (
            f"Contextual Significance relative to '{context_topic}': "
            f"Central structural hub [{', '.join(top_hubs[:3])}] destabilizes normative signifiers "
            f"and exposes the contingent nature of power discourse."
        )

        return {
            "verbal_meaning": verbal_meaning,
            "contextual_significance": significance,
            "top_graph_hubs": top_hubs,
            "graph_node_count": len(graph.nodes)
        }

    def synthesize_third_mind_insights(self, text: str) -> List[str]:
        """'Third Mind' Synthesis."""
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
        hirsch = self.hirsch_hermeneutic_analysis(text)

        return {
            "top_keywords": keywords,
            "juxtaposition_pairs": pairs,
            "third_mind_insights": insights,
            "hirsch_hermeneutics": hirsch,
            "revelation_score": round(min(1.0, len(keywords) * 0.1 + len(pairs) * 0.05), 3)
        }
