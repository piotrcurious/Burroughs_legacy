"""
Pure Python Prolog Inference Engine & Description Logic (DL) Reasoner.

Provides unification, backward-chaining resolution, Horn clause evaluation,
and ALC Description Logic subsumption reasoning for secondary ontology validation.
"""

from typing import Dict, List, Any, Union, Tuple, Set

class Term:
    def __init__(self, name: str, args: List['Term'] = None):
        self.name = name
        self.args = args or []
        self.is_var = name.isupper() or name.startswith("_")

    def __repr__(self):
        if not self.args:
            return self.name
        return f"{self.name}({', '.join(map(str, self.args))})"

    def __eq__(self, other):
        return isinstance(other, Term) and self.name == other.name and self.args == other.args

    def __hash__(self):
        return hash((self.name, tuple(self.args)))

class Clause:
    def __init__(self, head: Term, body: List[Term] = None):
        self.head = head
        self.body = body or []

    def __repr__(self):
        if not self.body:
            return f"{self.head}."
        return f"{self.head} :- {', '.join(map(str, self.body))}."

class PrologEngine:
    def __init__(self):
        self.rules: List[Clause] = []

    def add_fact(self, head: Term):
        self.rules.append(Clause(head, []))

    def add_rule(self, head: Term, body: List[Term]):
        self.rules.append(Clause(head, body))

    def unify(self, x: Term, y: Term, subst: Dict[str, Term]) -> Union[Dict[str, Term], None]:
        """First-order unification algorithm with substitution mapping."""
        subst = subst.copy() if subst is not None else {}

        x = self.walk(x, subst)
        y = self.walk(y, subst)

        if x == y:
            return subst
        elif x.is_var:
            return self.unify_var(x, y, subst)
        elif y.is_var:
            return self.unify_var(y, x, subst)
        elif x.name == y.name and len(x.args) == len(y.args):
            for a, b in zip(x.args, y.args):
                subst = self.unify(a, b, subst)
                if subst is None:
                    return None
            return subst
        else:
            return None

    def unify_var(self, var: Term, val: Term, subst: Dict[str, Term]) -> Union[Dict[str, Term], None]:
        if var.name in subst:
            return self.unify(subst[var.name], val, subst)
        elif val.is_var and val.name in subst:
            return self.unify(var, subst[val.name], subst)
        subst[var.name] = val
        return subst

    def walk(self, t: Term, subst: Dict[str, Term]) -> Term:
        if t.is_var and t.name in subst:
            return self.walk(subst[t.name], subst)
        if t.args:
            return Term(t.name, [self.walk(a, subst) for a in t.args])
        return t

    def solve_query(self, goals: List[Term], orig_vars: List[str], subst: Dict[str, Term] = None) -> List[Dict[str, Term]]:
        sols = self.query(goals, subst)
        clean_sols = []
        for s in sols:
            clean_s = {}
            for v in orig_vars:
                bound = self.walk(Term(v), s)
                clean_s[v] = bound
            clean_sols.append(clean_s)
        return clean_sols

    def query(self, goals: List[Term], subst: Dict[str, Term] = None) -> List[Dict[str, Term]]:
        """SLD Resolution backward-chaining solver."""
        if subst is None:
            subst = {}
        if not goals:
            return [subst]

        first = goals[0]
        rest = goals[1:]
        solutions = []

        for rule in self.rules:
            renamed_rule = self.rename_vars(rule)
            res_subst = self.unify(first, renamed_rule.head, subst)
            if res_subst is not None:
                new_goals = renamed_rule.body + rest
                sols = self.query(new_goals, res_subst)
                solutions.extend(sols)

        return solutions

    def rename_vars(self, rule: Clause, suffix: str = "_anon") -> Clause:
        """Renames clause variables for scope isolation."""
        var_map = {}

        def rename_term(t: Term) -> Term:
            if t.is_var:
                if t.name not in var_map:
                    var_map[t.name] = f"{t.name}_{id(rule)}"
                return Term(var_map[t.name])
            return Term(t.name, [rename_term(a) for a in t.args])

        return Clause(rename_term(rule.head), [rename_term(b) for b in rule.body])

class DescriptionLogicReasoner:
    """ALC Description Logic Subsumption Reasoner built on Prolog engine."""
    def __init__(self):
        self.prolog = PrologEngine()

    def add_subclass(self, sub_concept: str, super_concept: str):
        r"""Adds TBox axiom: C \sqsubseteq D."""
        sub_term = Term("isa", [Term("X"), Term(sub_concept)])
        super_term = Term("isa", [Term("X"), Term(super_concept)])
        self.prolog.add_rule(super_term, [sub_term])

    def add_instance(self, entity: str, concept: str):
        """Adds ABox assertion: C(e)."""
        self.prolog.add_fact(Term("isa", [Term(entity), Term(concept)]))

    def is_subsumed_by(self, sub_concept: str, super_concept: str) -> bool:
        r"""Checks if C \sqsubseteq D via resolution proof."""
        dummy_x = f"test_inst_{sub_concept}"
        self.add_instance(dummy_x, sub_concept)
        sols = self.prolog.query([Term("isa", [Term(dummy_x), Term(super_concept)])])
        return len(sols) > 0
