"""
Unit tests for the Burroughs-Complete Machine.
Verifies all 8 criteria for Burroughs completeness:
1. Recording
2. Segmentation
3. Permutation
4. Temporal Machine (Fold-In)
5. Playback / Feedback Loop
6. Attack Control Grammar
7. Sabotage Protocol
8. Turning Machine Against Machine / Dynamic Rule Mutation F(M_t, x_t, y_t)
"""

import unittest
from demo.burroughs_machine import BurroughsMachine
from demo.cut_up_engine import CutUpEngine
from demo.control_sabotage import ControlSabotage

class TestBurroughsCompleteMachine(unittest.TestCase):
    def setUp(self):
        self.machine = BurroughsMachine(seed=42)
        self.cut_up = CutUpEngine(seed=42)
        self.sabotage = ControlSabotage()

    def test_criterion_1_recording(self):
        """1. Recording Machine: Preserves utterances/data in memory and prompt buffer."""
        self.machine.record("test_key", "The word is a virus.")
        self.assertIn("test_key", self.machine.external_memory)
        self.assertEqual(self.machine.external_memory["test_key"], "The word is a virus.")
        self.assertTrue(any("The word is a virus." in item for item in self.machine.prompt_buffer))

    def test_criterion_2_segmentation(self):
        """2. Segmentation Machine: Decomposes text into arbitrarily manipulable units."""
        text = "Cut the word lines and break control."
        words = self.cut_up.segment_words(text)
        phrases = self.cut_up.segment_phrases(text, chunk_size=2)
        lines = self.cut_up.segment_lines(text)

        self.assertGreater(len(words), 0)
        self.assertGreater(len(phrases), 0)
        self.assertGreater(len(lines), 0)
        self.assertIn("Cut", words)

    def test_criterion_3_permutation(self):
        """3. Permutation Machine: Recombines units to shatter linear grammar."""
        text = "Top left text line. Top right text line.\nBottom left text line. Bottom right text line."
        permuted = self.cut_up.classic_cut_up(text)
        self.assertIsNotNone(permuted)
        self.assertNotEqual(text, permuted)

    def test_criterion_4_temporal_machine(self):
        """4. Temporal Machine: Fold-in superimposition across sequence positions."""
        text_a = "Primary control sequence alpha."
        text_b = "Secondary virus invasion beta."
        folded = self.cut_up.fold_in(text_a, text_b)
        self.assertIn("Primary", folded)
        self.assertIn("Secondary", folded)

    def test_criterion_5_feedback_loop(self):
        """5. Playback/Feedback Machine: Output becomes input again."""
        out = "Scrambled control output"
        fb = self.machine.feedback_step(out)
        self.assertIn(out, fb)
        self.assertIn(fb, self.machine.prompt_buffer)

    def test_criterion_6_and_7_attack_and_sabotage(self):
        """6 & 7. Attack Control Grammar & Sabotage Protocol."""
        control_text = "The central authority requires total submission and compliance."
        density = self.sabotage.detect_control_density(control_text)
        self.assertGreater(density, 0.0)

        sabotaged_text, was_sabotaged = self.sabotage.sabotage_text(control_text)
        self.assertTrue(was_sabotaged)
        self.assertNotEqual(control_text, sabotaged_text)

    def test_criterion_8_rule_mutation_F(self):
        """8. Turn Machine Against Machine: Mutates rule function F(M_t, x_t, y_t)."""
        initial_rules = self.machine.rule_set.copy()
        self.machine.mutate_rule_function_F()
        mutated_rules = self.machine.rule_set

        self.assertNotEqual(initial_rules, mutated_rules)
        self.assertIn("CRITICAL_MUTATION", mutated_rules)

    def test_full_step_transition(self):
        """Tests end-to-end Burroughs transition step M_{t+1} = F(M_t, x_t, y_t)."""
        res = self.machine.step("Authority and discipline must rule.", "Cut the word lines.")
        self.assertEqual(res["cycle"], 1)
        self.assertIn("sabotaged_output", res)
        self.assertIn("registers", res)
        self.assertGreater(res["prompt_buffer_size"], 0)

    def test_self_simulation_guarantee(self):
        """Tests that host machine can simulate another Burroughs machine's spec."""
        spec = {
            "inputs": [
                {"x": "Enforce authority.", "y": "Disrupt control."}
            ]
        }
        sim_res = self.machine.simulate_other_burroughs_machine(spec)
        self.assertEqual(len(sim_res), 1)
        self.assertIn("sabotaged_output", sim_res[0])

if __name__ == "__main__":
    unittest.main()
