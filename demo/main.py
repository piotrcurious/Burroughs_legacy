"""
Comprehensive Demonstration Runner for Burroughs-Complete Machine Architecture.

Runs:
1. Multi-stream Fold-in & Cut-up transitions across 4 diverse corpora.
2. Gnosis Layer Hirsch-grade meaning extraction and Third Mind synthesis.
3. Burroughs Autocoder code mutation and execution.
4. Secondary Ontology Extender generation (JSON-LD).
5. Visualizer ASCII Dashboard and HTML Dashboard export.
"""

import sys
import os
import json
from demo.burroughs_machine import BurroughsMachine
from demo.gnosis import GnosisExtractor
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
    print("      BURROUGHS-COMPLETE MACHINE INTEGRATED DEMONSTRATION")
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

    # 2. Step 1: Multi-Stream Fold-In (4 streams)
    print("\n>>> EXECUTE CYCLE 1: 4-STREAM MULTI-FOLD-IN")
    step1 = machine.step(
        input_x=text_control,
        secondary_y=text_counter,
        additional_streams=[text_computer, text_philosophical]
    )
    gnosis1 = gnosis.analyze_cut_up(step1["sabotaged_output"])
    print(Visualizer.render_ascii_dashboard(step1, gnosis1))
    history.append(step1)

    # 3. Step 2: Jump Matrix Permutation & Recirculation
    print("\n>>> EXECUTE CYCLE 2: RECIRCULATION & JUMP MATRIX PERMUTATION")
    step2 = machine.step(
        input_x=step1["sabotaged_output"],
        secondary_y=text_climate
    )
    gnosis2 = gnosis.analyze_cut_up(step2["sabotaged_output"])
    print(Visualizer.render_ascii_dashboard(step2, gnosis2))
    history.append(step2)

    # 4. Gnosis Meaning Extraction Output
    print("\n" + "=" * 75)
    print("GNOSIS LAYER: HIRSCH-GRADE MEANING EXTRACTION & THIRD MIND SYNTHESIS")
    print("=" * 75)
    for idx, insight in enumerate(gnosis2["third_mind_insights"], start=1):
        print(f"[{idx}] {insight}")

    # 5. Autocoder Practical Application
    print("\n" + "=" * 75)
    print("PRACTICAL APPLICATION 1: BURROUGHS AUTOCODER")
    print("=" * 75)
    autocoder = Autocoder(seed=42)
    generated_code = autocoder.synthesize_autocode(SAMPLE_CODE_SNIPPETS)
    print("Generated Autocode:")
    print("-" * 50)
    print(generated_code)
    print("-" * 50)
    is_valid = autocoder.validate_code_syntax(generated_code)
    print(f"AST Syntax Valid: {is_valid}")
    if is_valid:
        exec_res = autocoder.execute_autocode(generated_code, input_val=100)
        print(f"Autocode Execution Result: {exec_res}")

    # 6. Secondary Ontology Completeness Extender
    print("\n" + "=" * 75)
    print("PRACTICAL APPLICATION 2: SECONDARY ONTOLOGY EXTENDER (JSON-LD)")
    print("=" * 75)
    extender = SecondaryOntologyExtender()
    ontology_json = extender.deconstruct_primary_ontology(text_control, text_counter)
    ontology_path = "demo/secondary_ontology.jsonld"
    extender.export_ontology_json(ontology_json, ontology_path)
    print(f"Exported Secondary Ontology to: {ontology_path}")
    print(f"Graph Entities Count: {len(ontology_json['@graph'])}")
    print(f"Discovered Relationships Count: {len(ontology_json['relationships'])}")

    # 7. HTML Dashboard Generation
    Visualizer.generate_html_dashboard(history, "demo/dashboard.html")
    print(f"\nExported HTML Control Dashboard to: demo/dashboard.html")

    print("\n" + "=" * 75)
    print("DEMONSTRATION SUCCESSFULLY COMPLETE.")
    print("=" * 75)

if __name__ == "__main__":
    main()
