"""
Core Burroughs-Complete Machine Architecture.

Implements all 8 criteria for Burroughs Completeness:
1. Recording Machine (Tape / Memory)
2. Segmentation Machine
3. Permutation Machine
4. Temporal Machine (Fold-In / Jumps)
5. Playback / Feedback Loop
6. Attack on Control Grammar
7. Sabotage Protocol
8. Turning Machine Against Machine & Modifying Rule Set F

Formula: M_{t+1} = F(M_t, x_t, y_t) where F is dynamically mutable by the machine.
"""

import json
import random
from typing import Any, Dict, List, Optional, Tuple, Callable
from demo.cut_up_engine import CutUpEngine
from demo.control_sabotage import ControlSabotage

class BurroughsMachine:
    def __init__(self, seed: int = 42):
        self.cut_up_engine = CutUpEngine(seed=seed)
        self.sabotage_engine = ControlSabotage()

        # 1. Recording Machine State: Prompt/Tape Buffer & Registers
        self.prompt_buffer: List[str] = []
        self.registers: Dict[str, Any] = {
            "state": "INIT",
            "head_pos": 0,
            "cycle_count": 0,
            "control_density": 0.0,
            "mutation_level": 0
        }
        self.external_memory: Dict[str, str] = {}
        self.playback_history: List[str] = []

        # Dynamic Rule Set / Transformation Regime F(M_t, x_t, y_t)
        self.rule_set: Dict[str, str] = {
            "CUT_UP": "apply_classic_cut_up",
            "FOLD_IN": "apply_fold_in",
            "FEEDBACK": "apply_feedback_loop",
            "SABOTAGE": "apply_sabotage",
            "MUTATE_RULES": "apply_rule_mutation"
        }

    # Criterion 1: Recording Machine (Record input utterance/data to memory/buffer)
    def record(self, key: str, value: str) -> None:
        """Preserves utterances, images, texts, sounds, commands into memory/tape."""
        self.external_memory[key] = value
        self.prompt_buffer.append(f"RECORD[{key}]: {value}")
        self.playback_history.append(value)

    # Criterion 2: Segmentation
    def segment(self, text: str, mode: str = "phrases") -> List[str]:
        """Decomposes message into arbitrarily manipulable units."""
        if mode == "words":
            return self.cut_up_engine.segment_words(text)
        elif mode == "phrases":
            return self.cut_up_engine.segment_phrases(text)
        else:
            return self.cut_up_engine.segment_lines(text)

    # Criterion 3: Permutation
    def permute(self, text: str) -> str:
        """Recombines units to shatter linear grammar."""
        return self.cut_up_engine.classic_cut_up(text)

    # Criterion 4: Temporal Machine (Fold-In)
    def fold_in(self, text_a: str, text_b: str) -> str:
        """Superimposes texts across sequence positions manufacturing jumps and loops."""
        return self.cut_up_engine.fold_in(text_a, text_b)

    # Criterion 5: Playback / Feedback Loop
    def feedback_step(self, output_text: str) -> str:
        """
        Feedback operation: Output becomes input again.
        Scrambled recordings are fed back into the prompt buffer.
        """
        self.playback_history.append(output_text)
        # Feed previous output back with current buffer
        feedback_input = f"FEEDBACK_RECIRCULATION({output_text})"
        self.prompt_buffer.append(feedback_input)
        return feedback_input

    # Criterion 6 & 7: Attack Control Grammar & Sabotage
    def attack_and_sabotage(self, text: str) -> Tuple[str, bool]:
        """
        Monitors for control words/grammar and executes sabotage disruption if detected.
        """
        density = self.sabotage_engine.detect_control_density(text)
        self.registers["control_density"] = density
        sabotaged_text, was_sabotaged = self.sabotage_engine.sabotage_text(text)
        if was_sabotaged:
            self.registers["state"] = "CONTROL_SABOTAGED"
            self.prompt_buffer.append(f"SABOTAGE_EVENT: {sabotaged_text}")
        return sabotaged_text, was_sabotaged

    # Criterion 8: Turn Machine Against Machine & Modify Rule Function F
    def mutate_rule_function_F(self) -> None:
        """
        M_{t+1} = F(M_t, x_t, y_t)
        Modifies F itself, destabilizing the machine's own control rules.
        """
        self.registers["mutation_level"] += 1
        level = self.registers["mutation_level"]
        self.rule_set = self.sabotage_engine.mutate_control_grammar_rules(self.rule_set)
        self.prompt_buffer.append(f"MUTATION_LEVEL_{level}: Rule set F mutated!")

    def step(self, input_x: str, secondary_y: Optional[str] = None) -> Dict[str, Any]:
        """
        Executes one full step of the Burroughs transition function.
        M_{t+1} = F(M_t, x_t, y_t)
        """
        self.registers["cycle_count"] += 1
        current_cycle = self.registers["cycle_count"]

        # Step 1: Record inputs
        self.record(f"cycle_{current_cycle}_input_x", input_x)
        if secondary_y:
            self.record(f"cycle_{current_cycle}_input_y", secondary_y)

        # Step 2: Temporal Fold-in / Cut-Up
        if secondary_y:
            recombined = self.fold_in(input_x, secondary_y)
        else:
            recombined = self.permute(input_x)

        # Step 3: Attack Control Grammar & Sabotage
        sabotaged_output, is_sabotaged = self.attack_and_sabotage(recombined)

        # Step 4: Playback Feedback Loop
        feedback_str = self.feedback_step(sabotaged_output)

        # Step 5: Meta-Rule Mutation if control density was high or every 2 cycles
        if is_sabotaged or current_cycle % 2 == 0:
            self.mutate_rule_function_F()

        # Update Head Position & Registers
        self.registers["head_pos"] = len(self.prompt_buffer) - 1

        result = {
            "cycle": current_cycle,
            "registers": self.registers.copy(),
            "raw_recombined": recombined,
            "sabotaged_output": sabotaged_output,
            "feedback_str": feedback_str,
            "active_rule_set": self.rule_set.copy(),
            "prompt_buffer_size": len(self.prompt_buffer)
        }
        return result

    def simulate_other_burroughs_machine(self, other_description: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Burroughs-Completeness Simulation Guarantee:
        Can take the specification/prompt-templates of any other Burroughs Machine
        and simulate its step-by-step operation.
        """
        sim_results = []
        inputs = other_description.get("inputs", [])
        for inp in inputs:
            step_res = self.step(inp.get("x", ""), inp.get("y", None))
            sim_results.append(step_res)
        return sim_results
