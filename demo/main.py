"""
Main demonstration script and interactive CLI for the Burroughs-Complete Machine.
"""

import sys
import os
import json
from demo.burroughs_machine import BurroughsMachine

def load_file(path: str) -> str:
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    return path

def run_demonstration():
    print("=" * 70)
    print("      BURROUGHS-COMPLETE MACHINE DEMONSTRATION")
    print("      'Universality over transformations of the control system itself'")
    print("=" * 70)

    primary_path = "demo/corpora/primary_control.txt"
    counter_path = "demo/corpora/counter_narrative.txt"

    text_control = load_file(primary_path)
    text_counter = load_file(counter_path)

    print("\n--- [PRIMARY CONTROL CORPUS (x_t)] ---")
    print(text_control)

    print("\n--- [COUNTER-NARRATIVE DISRUPTOR (y_t)] ---")
    print(text_counter)

    machine = BurroughsMachine(seed=123)

    print("\n" + "=" * 70)
    print("EXECUTING BURROUGHS TRANSITION STEPS M_{t+1} = F(M_t, x_t, y_t)...")
    print("=" * 70)

    # Step 1: Interleave / Fold-in Primary Control with Counter Narrative
    step1 = machine.step(text_control, text_counter)
    print(f"\n>>> CYCLE {step1['cycle']} RESULT:")
    print(f"State Register: {step1['registers']}")
    print(f"Control Density Detected: {step1['registers']['control_density']:.3f}")
    print("\nRecombined / Folded-in & Sabotaged Text:")
    print(step1['sabotaged_output'])
    print(f"\nFeedback String Recirculated: {step1['feedback_str']}")

    # Step 2: Recirculate previous output and perform Cut-Up
    print("\n" + "-" * 70)
    step2 = machine.step(step1['sabotaged_output'])
    print(f"\n>>> CYCLE {step2['cycle']} RESULT:")
    print(f"State Register: {step2['registers']}")
    print(f"Mutation Level: {step2['registers']['mutation_level']}")
    print("\nCut-Up Output:")
    print(step2['sabotaged_output'])

    # Step 3: Self-Simulation Guarantee Demonstration
    print("\n" + "=" * 70)
    print("DEMONSTRATING BURROUGHS-COMPLETENESS: SELF-SIMULATION GUARANTEE")
    print("=" * 70)
    other_machine_spec = {
        "name": "Target_Submachine_Alpha",
        "inputs": [
            {"x": "Systematic compliance enforced by authority.", "y": "Viral break in word lines."},
            {"x": "Mandatory market protocols.", "y": "Subvert primary ontologies."}
        ]
    }
    print(f"Simulating Machine Spec: {other_machine_spec['name']}")
    sim_outputs = machine.simulate_other_burroughs_machine(other_machine_spec)
    for i, res in enumerate(sim_outputs, start=1):
        print(f"\n[Simulated Step {i}] Sabotaged Output:")
        print(res['sabotaged_output'])

    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE: Machine modified rule function F and disrupted control grammar.")
    print("=" * 70)

def main():
    run_demonstration()

if __name__ == "__main__":
    main()
