"""
Enhanced Core Burroughs-Complete Machine Architecture.

Implements all 8 criteria for Burroughs Completeness with state persistence,
multi-stream folding, semantic entropy registers, and dynamic F mutation.
"""

import json
import random
import os
from typing import Any, Dict, List, Optional, Tuple
from demo.cut_up_engine import CutUpEngine
from demo.control_sabotage import ControlSabotage

class BurroughsMachine:
    def __init__(self, seed: Optional[int] = 42):
        self.cut_up_engine = CutUpEngine(seed=seed)
        self.sabotage_engine = ControlSabotage()

        # Tape Buffer & Registers
        self.prompt_buffer: List[str] = []
        self.registers: Dict[str, Any] = {
            "state": "INIT",
            "head_pos": 0,
            "cycle_count": 0,
            "control_density": 0.0,
            "entropy_bits": 0.0,
            "mutation_level": 0
        }
        self.external_memory: Dict[str, str] = {}
        self.playback_history: List[str] = []

        # Dynamic Transformation Ruleset F(M_t, x_t, y_t, ...)
        self.rule_set: Dict[str, str] = {
            "CUT_UP": "classic_cut_up",
            "FOLD_IN": "multi_stream_fold_in",
            "JUMP_MATRIX": "jump_matrix_permutation",
            "FEEDBACK": "recirculate_playback",
            "SABOTAGE": "sabotage_control_words",
            "MUTATE_RULES": "mutate_grammar_rules"
        }

    def record(self, key: str, value: str) -> None:
        """Preserves utterances, texts, commands into memory/tape."""
        self.external_memory[key] = value
        self.prompt_buffer.append(f"RECORD[{key}]: {value}")
        self.playback_history.append(value)

    def segment(self, text: str, mode: str = "phrases") -> List[str]:
        """Decomposes message into manipulable units."""
        if mode == "words":
            return self.cut_up_engine.segment_words(text)
        elif mode == "phrases":
            return self.cut_up_engine.segment_phrases(text)
        else:
            return self.cut_up_engine.segment_lines(text)

    def permute(self, text: str, mode: str = "cut_up") -> str:
        """Recombines units via cut-up or jump-matrix."""
        if mode == "jump_matrix":
            return self.cut_up_engine.jump_matrix_permutation(text)
        return self.cut_up_engine.classic_cut_up(text)

    def fold_in(self, text_a: str, text_b: str) -> str:
        """2-way fold-in superimposition."""
        return self.cut_up_engine.fold_in(text_a, text_b)

    def multi_fold_in(self, texts: List[str]) -> str:
        """N-way multi-stream fold-in superimposition."""
        return self.cut_up_engine.multi_stream_fold_in(texts)

    def feedback_step(self, output_text: str) -> str:
        """
        Feedback operation: Output recirculates into prompt buffer.
        Scrambled recordings feed back into the control machine.
        """
        self.playback_history.append(output_text)
        feedback_input = f"FEEDBACK_RECIRCULATION({output_text})"
        self.prompt_buffer.append(feedback_input)
        return feedback_input

    def attack_and_sabotage(self, text: str) -> Tuple[str, bool]:
        """Monitors control density and sabotages word lines if detected."""
        density = self.sabotage_engine.detect_control_density(text)
        self.registers["control_density"] = round(density, 4)
        sabotaged_text, was_sabotaged = self.sabotage_engine.sabotage_text(text)
        if was_sabotaged:
            self.registers["state"] = "CONTROL_SABOTAGED"
            self.prompt_buffer.append(f"SABOTAGE_EVENT: {sabotaged_text}")
        return sabotaged_text, was_sabotaged

    def mutate_rule_function_F(self) -> None:
        """Mutates rule function F, destabilizing production constraints."""
        self.registers["mutation_level"] += 1
        level = self.registers["mutation_level"]
        self.rule_set = self.sabotage_engine.mutate_control_grammar_rules(self.rule_set)
        self.prompt_buffer.append(f"MUTATION_LEVEL_{level}: Rule set F mutated!")

    def step(self, input_x: str, secondary_y: Optional[str] = None, additional_streams: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Executes one transition step of Burroughs Machine:
        M_{t+1} = F(M_t, x_t, y_t, ...)
        """
        self.registers["cycle_count"] += 1
        current_cycle = self.registers["cycle_count"]

        # 1. Record inputs
        self.record(f"cycle_{current_cycle}_input_x", input_x)
        streams = [input_x]
        if secondary_y:
            self.record(f"cycle_{current_cycle}_input_y", secondary_y)
            streams.append(secondary_y)
        if additional_streams:
            for idx, st in enumerate(additional_streams, start=1):
                self.record(f"cycle_{current_cycle}_stream_{idx}", st)
                streams.append(st)

        # 2. Recombine / Fold-in / Jump Matrix
        if len(streams) > 1:
            recombined = self.multi_fold_in(streams)
        else:
            recombined = self.permute(input_x, mode="jump_matrix" if current_cycle % 2 == 0 else "cut_up")

        # 3. Calculate Entropy
        entropy = self.cut_up_engine.calculate_semantic_entropy(recombined)
        self.registers["entropy_bits"] = entropy

        # 4. Attack Control Grammar & Sabotage
        sabotaged_output, is_sabotaged = self.attack_and_sabotage(recombined)

        # 5. Feedback Loop
        feedback_str = self.feedback_step(sabotaged_output)

        # 6. Mutate F if sabotaged or periodic
        if is_sabotaged or current_cycle % 2 == 0:
            self.mutate_rule_function_F()

        self.registers["head_pos"] = len(self.prompt_buffer) - 1

        return {
            "cycle": current_cycle,
            "registers": self.registers.copy(),
            "raw_recombined": recombined,
            "sabotaged_output": sabotaged_output,
            "feedback_str": feedback_str,
            "active_rule_set": self.rule_set.copy(),
            "prompt_buffer_size": len(self.prompt_buffer)
        }

    def save_state(self, filepath: str) -> None:
        """Persists state registers and tape buffer to JSON."""
        data = {
            "registers": self.registers,
            "external_memory": self.external_memory,
            "playback_history": self.playback_history,
            "prompt_buffer": self.prompt_buffer,
            "rule_set": self.rule_set
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def load_state(self, filepath: str) -> None:
        """Loads machine state from JSON."""
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.registers = data.get("registers", self.registers)
            self.external_memory = data.get("external_memory", self.external_memory)
            self.playback_history = data.get("playback_history", self.playback_history)
            self.prompt_buffer = data.get("prompt_buffer", self.prompt_buffer)
            self.rule_set = data.get("rule_set", self.rule_set)

    def simulate_other_burroughs_machine(self, other_description: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Self-simulation guarantee."""
        sim_results = []
        inputs = other_description.get("inputs", [])
        for inp in inputs:
            step_res = self.step(inp.get("x", ""), inp.get("y", None), inp.get("streams", None))
            sim_results.append(step_res)
        return sim_results
