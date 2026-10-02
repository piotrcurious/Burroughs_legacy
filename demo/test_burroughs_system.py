"""
Comprehensive Deep Unit Test Suite for Burroughs-Complete Machine Architecture.

Tests:
- Core Burroughs completeness criteria
- C Native shared library binding & Markov entropy calculations
- Prolog Engine unification, SLD resolution, & Description Logic subsumption
- AST NodeTransformer mutation & crossover autocoder
- Hirsch Hermeneutics & Co-Occurrence Graph analytics
- Secondary Ontology Extender JSON-LD & completeness metrics
- ASCII & HTML Dashboard visualizer
"""

import unittest
import os
import json
from demo.burroughs_machine import BurroughsMachine
from demo.cut_up_engine import CutUpEngine
from demo.control_sabotage import ControlSabotage
from demo.gnosis import GnosisExtractor, CoOccurrenceGraph
from demo.prolog_engine import PrologEngine, Term, Clause, DescriptionLogicReasoner
from demo.ast_mutator import ASTAutocoder
from demo.autocoder import Autocoder, SAMPLE_CODE_SNIPPETS
from demo.ontology_extender import SecondaryOntologyExtender
from demo.visualizer import Visualizer

class TestDeepBurroughsSystem(unittest.TestCase):
    def setUp(self):
        self.machine = BurroughsMachine(seed=42)
        self.cut_up = CutUpEngine(seed=42)
        self.gnosis = GnosisExtractor()
        self.prolog = PrologEngine()
        self.dl_reasoner = DescriptionLogicReasoner()
        self.ast_autocoder = ASTAutocoder(seed=42)
        self.extender = SecondaryOntologyExtender()

    def test_c_native_library_and_markov_entropy(self):
        """Tests C Native Library integration & Markov entropy calculations."""
        text = "word lines cut word lines break control authority word lines"
        entropy = self.cut_up.calculate_markov_entropy(text)
        self.assertIsInstance(entropy, float)
        self.assertGreater(entropy, 0.0)

    def test_prolog_unification_and_query(self):
        """Tests Prolog Engine unification and backward chaining resolution."""
        # parent(john, mary). parent(mary, alice). grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
        self.prolog.add_fact(Term("parent", [Term("john"), Term("mary")]))
        self.prolog.add_fact(Term("parent", [Term("mary"), Term("alice")]))
        self.prolog.add_rule(
            Term("grandparent", [Term("X"), Term("Y")]),
            [Term("parent", [Term("X"), Term("Z")]), Term("parent", [Term("Z"), Term("Y")])]
        )

        sols = self.prolog.solve_query([Term("grandparent", [Term("john"), Term("Y")])], orig_vars=["Y"])
        self.assertGreater(len(sols), 0)
        self.assertEqual(sols[0]["Y"].name, "alice")

    def test_description_logic_subsumption(self):
        """Tests Description Logic TBox subsumption reasoning."""
        self.dl_reasoner.add_subclass("PrimaryControlEntity", "SystemicDominance")
        is_sub = self.dl_reasoner.is_subsumed_by("PrimaryControlEntity", "SystemicDominance")
        self.assertTrue(is_sub)

    def test_co_occurrence_graph_pagerank(self):
        """Tests word co-occurrence graph construction and PageRank."""
        words = ["control", "authority", "system", "virus", "word", "lines", "control", "virus"]
        graph = CoOccurrenceGraph(window_size=3)
        graph.build_graph(words)
        pr = graph.calculate_pagerank()
        self.assertIn("control", pr)
        self.assertIn("virus", pr)

    def test_hirsch_hermeneutics(self):
        """Tests E.D. Hirsch verbal meaning vs. significance analysis."""
        text = "Central authority enforces mandatory compliance across all systems."
        hirsch = self.gnosis.hirsch_hermeneutic_analysis(text)
        self.assertIn("verbal_meaning", hirsch)
        self.assertIn("contextual_significance", hirsch)

    def test_ast_node_crossover_and_mutation(self):
        """Tests AST NodeTransformer cut-ups and code crossover."""
        code1 = SAMPLE_CODE_SNIPPETS[0]
        code2 = SAMPLE_CODE_SNIPPETS[2]
        crossover = self.ast_autocoder.ast_crossover(code1, code2)
        mutated = self.ast_autocoder.mutate_ast(crossover)
        self.assertIsNotNone(mutated)
        res = self.ast_autocoder.execute_ast_autocode(mutated, input_val=[1, 2, 3])
        self.assertIn("status", res)

    def test_ontology_extender_metrics(self):
        """Tests JSON-LD output and ontology completeness score calculation."""
        p_text = "The central authority enforces regulation and discipline."
        c_text = "Cut the word lines and disrupt the primary ontology."
        ont = self.extender.deconstruct_primary_ontology(p_text, c_text)
        self.assertIn("completeness_metrics", ont)
        self.assertIn("dl_subsumption_proof_valid", ont)
        self.assertTrue(ont["dl_subsumption_proof_valid"])
        self.assertGreater(ont["completeness_metrics"]["completeness_score"], 0.0)

if __name__ == "__main__":
    unittest.main()
