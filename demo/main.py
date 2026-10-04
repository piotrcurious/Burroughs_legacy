"""
Integrated Deep Demonstration Runner for Burroughs-Complete Machine Architecture.

Demonstrates:
1. Multi-Stream Fold-in & C Native Markov Entropy / LSA Vector Space.
2. Hirsch Hermeneutic Gnosis Layer & Word Co-Occurrence Graph Analysis.
3. Prolog DL Reasoner & Description Logic Subsumption Proofs.
4. AST Node Crossover & Evolutionary Autocoder.
5. Secondary Ontology Extender with Mathematical Completeness Metrics (JSON-LD).
6. ASCII Control Visualizer & HTML Dashboard Export.
"""

import sys
import os
import json
from demo.burroughs_machine import BurroughsMachine
from demo.gnosis import GnosisExtractor
from demo.prolog_engine import PrologEngine, Term, DescriptionLogicReasoner
from demo.ast_mutator import ASTAutocoder
from demo.autocoder import Autocoder, SAMPLE_CODE_SNIPPETS
from demo.ontology_extender import SecondaryOntologyExtender
from demo.visualizer import Visualizer

def load_file(path: str) -> str:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return path

def main():
    print("=" * 75)
    print("      BURROUGHS-COMPLETE MACHINE INTEGRATED DEEP DEMONSTRATION")
    print("      'Universality over transformations of the control system itself'")
    print("=" * 75)

    # 1. Load Corpora
    text_control = load_file("demo/corpora/primary_control.txt")
    text_counter = load_file("demo/corpora/counter_narrative.txt")
    text_computer = load_file("demo/corpora/computer_documentation.txt")
    text_philosophical = load_file("demo/corpora/philosophical_texts.txt")
    text_climate = load_file("demo/corpora/climate_ai.txt")

    machine = BurroughsMachine(seed=42)
    gnosis = GnosisExtractor()
    history = []

    # 2. Cycle 1: 4-Stream Multi-Fold-In & C Native Markov Entropy Calculation
    print("\n>>> EXECUTE CYCLE 1: 4-STREAM MULTI-FOLD-IN & C NATIVE MARKOV ENTROPY")
    step1 = machine.step(
        input_x=text_control,
        secondary_y=text_counter,
        additional_streams=[text_computer, text_philosophical]
    )
    gnosis1 = gnosis.analyze_cut_up(step1["sabotaged_output"])
    print(Visualizer.render_ascii_dashboard(step1, gnosis1))
    history.append(step1)

    # 3. Cycle 2: Recirculation & Jump Matrix Permutation
    print("\n>>> EXECUTE CYCLE 2: RECIRCULATION & JUMP MATRIX PERMUTATION")
    step2 = machine.step(
        input_x=step1["sabotaged_output"],
        secondary_y=text_climate
    )
    gnosis2 = gnosis.analyze_cut_up(step2["sabotaged_output"])
    print(Visualizer.render_ascii_dashboard(step2, gnosis2))
    history.append(step2)

    # 4. Hirsch Hermeneutics & Co-Occurrence Graph Analysis
    print("\n" + "=" * 75)
    print("GNOSIS LAYER: HIRSCH HERMENEUTICS & CO-OCCURRENCE GRAPH ANALYSIS")
    print("=" * 75)
    hirsch = gnosis2["hirsch_hermeneutics"]
    print(f"[Verbal Meaning]: {hirsch['verbal_meaning']}")
    print(f"[Contextual Significance]: {hirsch['contextual_significance']}")
    print(f"[Graph Central Hubs]: {', '.join(hirsch['top_graph_hubs'])}")

    # 5. Prolog Engine & Description Logic Subsumption Proof
    print("\n" + "=" * 75)
    print("PROLOG LOGIC ENGINE: DESCRIPTION LOGIC (DL) SUBSUMPTION PROOF")
    print("=" * 75)
    dl = DescriptionLogicReasoner()
    dl.add_subclass("PrimaryControlEntity", "SystemicDominance")
    dl.add_instance("AuthorityProtocol", "PrimaryControlEntity")
    is_subsumed = dl.is_subsumed_by("PrimaryControlEntity", "SystemicDominance")
    print(f"Proof Goal: PrimaryControlEntity ⊑ SystemicDominance")
    print(f"SLD Resolution Proof Result: {is_subsumed}")

    # 6. AST Evolutionary Autocoder
    print("\n" + "=" * 75)
    print("PRACTICAL APPLICATION 1: AST EVOLUTIONARY AUTOCODER")
    print("=" * 75)
    ast_autocoder = ASTAutocoder(seed=42)
    parent1 = SAMPLE_CODE_SNIPPETS[0]
    parent2 = SAMPLE_CODE_SNIPPETS[2]
    crossover_code = ast_autocoder.ast_crossover(parent1, parent2)
    mutated_ast_code = ast_autocoder.mutate_ast(crossover_code)
    print("Mutated AST Code:")
    print("-" * 50)
    print(mutated_ast_code)
    print("-" * 50)
    exec_res = ast_autocoder.execute_ast_autocode(mutated_ast_code, input_val=[1, 2, 3])
    print(f"AST Autocode Execution Result: {exec_res}")

    # 7. Secondary Ontology Completeness Extender
    print("\n" + "=" * 75)
    print("PRACTICAL APPLICATION 2: SECONDARY ONTOLOGY EXTENDER (JSON-LD)")
    print("=" * 75)
    extender = SecondaryOntologyExtender()
    ontology_json = extender.deconstruct_primary_ontology(text_control, text_counter)
    ontology_path = "demo/secondary_ontology.jsonld"
    extender.export_ontology_json(ontology_json, ontology_path)
    print(f"Exported Secondary Ontology to: {ontology_path}")
    print(f"Completeness Metrics: {ontology_json['completeness_metrics']}")

    # 8. HTML Control Dashboard Generation
    Visualizer.generate_html_dashboard(history, "demo/dashboard.html")
    print(f"\nExported HTML Control Dashboard to: demo/dashboard.html")

    print("\n" + "=" * 75)
    print("DEMONSTRATION SUCCESSFULLY COMPLETE.")
    print("=" * 75)

if __name__ == "__main__":
    main()
