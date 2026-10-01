"""
Comprehensive Unit Test Suite for Burroughs-Complete Machine Architecture.

Tests:
- Core Burroughs completeness criteria
- N-way multi-stream fold-in and jump matrix permutation
- Gnosis Layer Hirsch-grade meaning extraction
- Autocoder syntax mutation and execution
- Secondary Ontology Extender (JSON-LD)
- Visualizer ASCII and HTML dashboard generation
"""

import unittest
import os
import json
from demo.burroughs_machine import BurroughsMachine
from demo.cut_up_engine import CutUpEngine
from demo.control_sabotage import ControlSabotage
from demo.gnosis import GnosisExtractor
from demo.autocoder import Autocoder, SAMPLE_CODE_SNIPPETS
from demo.ontology_extender import SecondaryOntologyExtender
from demo.visualizer import Visualizer

class TestBurroughsSystem(unittest.TestCase):
    def setUp(self):
        self.machine = BurroughsMachine(seed=42)
        self.cut_up = CutUpEngine(seed=42)
        self.gnosis = GnosisExtractor()
        self.autocoder = Autocoder(seed=42)
        self.extender = SecondaryOntologyExtender()

    def test_multi_stream_fold_in(self):
        """Tests N-way multi-stream text interleave."""
        t1 = "Alpha stream line one."
        t2 = "Beta stream line two."
        t3 = "Gamma stream line three."
        folded = self.cut_up.multi_stream_fold_in([t1, t2, t3])
        self.assertIn("Alpha", folded)
        self.assertIn("Beta", folded)
        self.assertIn("Gamma", folded)

    def test_jump_matrix_permutation(self):
        """Tests grid jump matrix traversal."""
        text = "Word one word two word three word four word five word six"
        permuted = self.cut_up.jump_matrix_permutation(text, jump_step=2)
        self.assertIsNotNone(permuted)
        self.assertNotEqual(text, permuted)

    def test_semantic_entropy_calculation(self):
        """Tests Shannon semantic entropy calculation."""
        text = "word word word word"
        ent1 = self.cut_up.calculate_semantic_entropy(text)
        text_var = "alpha beta gamma delta epsilon"
        ent2 = self.cut_up.calculate_semantic_entropy(text_var)
        self.assertGreater(ent2, ent1)

    def test_gnosis_meaning_extraction(self):
        """Tests Hirsch-grade meaning extractor and Third Mind insights."""
        text = "The central authority enforces mandatory compliance through word lines."
        analysis = self.gnosis.analyze_cut_up(text)
        self.assertIn("top_keywords", analysis)
        self.assertIn("third_mind_insights", analysis)
        self.assertGreater(len(analysis["third_mind_insights"]), 0)

    def test_autocoder_synthesis_and_execution(self):
        """Tests Autocoder code generation, AST validation, and safe execution."""
        code = self.autocoder.synthesize_autocode(SAMPLE_CODE_SNIPPETS)
        self.assertTrue(self.autocoder.validate_code_syntax(code))
        res = self.autocoder.execute_autocode(code, input_val=42)
        self.assertEqual(res["status"], "DISRUPTED")
        self.assertEqual(res["x"], 42)

    def test_ontology_extender_jsonld(self):
        """Tests Secondary Ontology Extender generation and export."""
        p_text = "The central authority enforces regulation and discipline."
        c_text = "Cut the word lines and disrupt the primary ontology."
        ont = self.extender.deconstruct_primary_ontology(p_text, c_text)
        self.assertIn("@graph", ont)
        self.assertIn("relationships", ont)

        out_path = "/tmp/test_ontology.jsonld"
        self.extender.export_ontology_json(ont, out_path)
        self.assertTrue(os.path.exists(out_path))

    def test_visualizer_rendering(self):
        """Tests ASCII and HTML dashboard generation."""
        step_res = self.machine.step("Authority and discipline", "Break word lines")
        analysis = self.gnosis.analyze_cut_up(step_res["sabotaged_output"])
        ascii_dash = Visualizer.render_ascii_dashboard(step_res, analysis)
        self.assertIn("BURROUGHS MACHINE", ascii_dash)

        html_path = "/tmp/test_dashboard.html"
        Visualizer.generate_html_dashboard([step_res], html_path)
        self.assertTrue(os.path.exists(html_path))

if __name__ == "__main__":
    unittest.main()
