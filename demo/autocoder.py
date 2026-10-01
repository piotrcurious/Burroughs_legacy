"""
Burroughs Autocoder:
Uses cut-up, fold-in, and feedback loops to mutate, synthesize,
and auto-generate executable Python code and scripts.
"""

import re
import random
import ast
from typing import Dict, List, Any, Tuple
from demo.cut_up_engine import CutUpEngine

SAMPLE_CODE_SNIPPETS = [
    "def process_signal(data):\n    return [x * 2 for x in data if x > 0]",
    "def execute_kernel_trap(syscall_id):\n    if syscall_id == 0:\n        raise SystemError('Kernel interrupt')",
    "def mutate_state(registers, input_val):\n    registers['state'] = 'MUTATED'\n    registers['value'] = input_val",
    "def disrupt_control_loop(feedback_signal):\n    return f'SABOTAGE({feedback_signal})'"
]

class Autocoder:
    def __init__(self, seed: int = 42):
        self.cut_up_engine = CutUpEngine(seed=seed)

    def fragment_code(self, code_str: str) -> List[str]:
        """Fragments code string into syntactically manipulable statement lines."""
        lines = [line.strip() for line in code_str.split('\n') if line.strip()]
        return lines

    def synthesize_autocode(self, code_sources: List[str]) -> str:
        """
        Uses multi-stream fold-in to interleave code lines from different functions,
        constructing novel algorithmic structures.
        """
        all_lines = []
        for src in code_sources:
            for line in self.fragment_code(src):
                # Clean block headers and return statements to maintain standalone validity
                clean = line
                if clean.startswith("def "):
                    clean = f"# Mutation def: {clean}"
                elif clean.startswith("if "):
                    clean = f"# Mutation cond: {clean}"
                elif clean.startswith("raise "):
                    clean = f"# Mutation raise: {clean}"
                elif clean.startswith("return "):
                    clean = f"result_signal = {clean[7:]}"
                all_lines.append(clean)

        random.seed(42)
        random.shuffle(all_lines)

        func_name = f"burroughs_autocode_{random.randint(1000, 9999)}"
        code_lines = [
            f"def {func_name}(x_input, registers=None):",
            "    registers = registers or {}",
            "    input_val = x_input",
            "    syscall_id = 0",
            "    result_signal = 'INIT'"
        ]

        for idx, line in enumerate(all_lines[:6], start=1):
            code_lines.append(f"    {line}")

        code_lines.append("    registers['autocode_executed'] = True")
        code_lines.append("    return {'status': 'DISRUPTED', 'x': x_input, 'registers': registers, 'signal': result_signal}")

        generated_code = "\n".join(code_lines)
        return generated_code

    def validate_code_syntax(self, code_str: str) -> bool:
        """Verifies if the generated autocode is valid Python AST."""
        try:
            ast.parse(code_str)
            return True
        except SyntaxError:
            return False

    def execute_autocode(self, code_str: str, input_val: Any) -> Dict[str, Any]:
        """Safely executes generated autocode in an isolated local scope."""
        if not self.validate_code_syntax(code_str):
            return {"error": "SyntaxError in generated autocode"}

        local_scope = {}
        exec(code_str, {}, local_scope)

        func_name = [k for k in local_scope.keys() if k.startswith("burroughs_autocode_")][0]
        func = local_scope[func_name]

        result = func(input_val)
        return result
