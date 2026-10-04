"""
Burroughs Evolutionary AST Autocoder & Structural Node Mutator.

Uses Python's ast.NodeTransformer to execute structural code cut-ups,
node crossover, function fold-ins, and AST level mutations.
"""

import ast
import random
import copy
from typing import Dict, List, Any, Optional

class ASTCutUpTransformer(ast.NodeTransformer):
    """AST Node Transformer that mutates Python code trees."""
    def __init__(self, seed: int = 42):
        super().__init__()
        random.seed(seed)

    def visit_BinOp(self, node: ast.BinOp) -> ast.AST:
        """Mutates arithmetic binary operators (e.g., + -> *, - -> /)."""
        self.generic_visit(node)
        ops = [ast.Add(), ast.Sub(), ast.Mult(), ast.BitXor()]
        node.op = random.choice(ops)
        return node

    def visit_Compare(self, node: ast.Compare) -> ast.AST:
        """Mutates comparison operators (e.g., > -> <=)."""
        self.generic_visit(node)
        cmps = [ast.Eq(), ast.NotEq(), ast.Lt(), ast.GtE()]
        node.ops = [random.choice(cmps) for _ in node.ops]
        return node

    def visit_Assign(self, node: ast.Assign) -> ast.AST:
        """Injects feedback registry tracking into assignments."""
        self.generic_visit(node)
        # Annotate variable name if Name target
        if node.targets and isinstance(node.targets[0], ast.Name):
            target_name = node.targets[0].id
            if target_name != "registers":
                # Create registers['last_assign'] = target_name
                reg_assign = ast.Assign(
                    targets=[ast.Subscript(
                        value=ast.Name(id='registers', ctx=ast.Load()),
                        slice=ast.Constant(value='last_assign'),
                        ctx=ast.Store()
                    )],
                    value=ast.Constant(value=target_name)
                )
                return [node, reg_assign]
        return node

class ASTAutocoder:
    def __init__(self, seed: int = 42):
        self.seed = seed

    def mutate_ast(self, code_str: str) -> str:
        """Parses code to AST, applies ASTCutUpTransformer, and unparses to code."""
        try:
            tree = ast.parse(code_str)
            transformer = ASTCutUpTransformer(seed=self.seed)
            mutated_tree = transformer.visit(tree)
            ast.fix_missing_locations(mutated_tree)
            return ast.unparse(mutated_tree)
        except Exception:
            return code_str

    def ast_crossover(self, parent_a_code: str, parent_b_code: str) -> str:
        """Performs AST node crossover between two parent function trees."""
        try:
            tree_a = ast.parse(parent_a_code)
            tree_b = ast.parse(parent_b_code)

            stmts_a = tree_a.body
            stmts_b = tree_b.body

            # Interleave top-level statements
            crossover_body = []
            max_len = max(len(stmts_a), len(stmts_b))
            for i in range(max_len):
                if i < len(stmts_a):
                    crossover_body.append(copy.deepcopy(stmts_a[i]))
                if i < len(stmts_b):
                    crossover_body.append(copy.deepcopy(stmts_b[i]))

            child_tree = ast.Module(body=crossover_body, type_ignores=[])
            ast.fix_missing_locations(child_tree)
            return ast.unparse(child_tree)
        except Exception:
            return parent_a_code

    def execute_ast_autocode(self, code_str: str, input_val: Any) -> Dict[str, Any]:
        """Validates AST and executes safely."""
        try:
            ast.parse(code_str)
        except SyntaxError as e:
            return {"error": f"AST SyntaxError: {e}"}

        local_scope = {}
        try:
            exec(code_str, {}, local_scope)
            funcs = [v for k, v in local_scope.items() if callable(v)]
            if funcs:
                res = funcs[0](input_val)
                return {"status": "SUCCESS", "result": res}
            return {"status": "EXECUTED", "scope": list(local_scope.keys())}
        except Exception as ex:
            return {"status": "RUNTIME_DISRUPTION", "exception": str(ex)}
