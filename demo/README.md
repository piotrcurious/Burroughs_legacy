# Burroughs-Complete Machine Demonstration

This directory contains a functional demonstration of a **Burroughs-Complete Machine**, an abstract model of computational language processing shifted from algorithmic execution (Turing completeness) to William S. Burroughs's theoretical framework of language, control, and linguistic sabotage.

---

## Conceptual Architecture & Mathematical Definition

Where a classical Turing Machine operates on symbol manipulation over an infinite tape via a fixed transition function $\delta$, a Burroughs-Complete Machine operates on representations and the mechanisms of control themselves.

The state transition is expressed as:

$$M_{t+1} = F(M_t, x_t, y_t)$$

where:
- $M_t$ represents the machine state, prompt buffer, registers, and memory.
- $x_t$ is the primary input text (e.g. control texts or primary ontologies).
- $y_t$ is the secondary/oblique input stream (e.g. counter-narratives or disruptors).
- $F$ is the dynamic production/control regime, which **the machine can modify itself**.

---

## The 8 Criteria for Burroughs Completeness

1. **Recording Machine (`BurroughsMachine.record`)**
   - Preserves utterances, texts, commands, and memory streams in a prompt buffer and external store.

2. **Segmentation Machine (`CutUpEngine.segment_*`)**
   - Decomposes messages into arbitrarily manipulable units (words, n-grams, phrases, lines).

3. **Permutation Machine (`CutUpEngine.classic_cut_up`)**
   - Recombines units into non-linear configurations, shattering standard linear grammar.

4. **Temporal Machine (`CutUpEngine.fold_in` / `diagonal_slice`)**
   - Superimposes texts across different sequence positions, manufacturing jumps, loops, and anticipations.

5. **Playback / Feedback Machine (`BurroughsMachine.feedback_step`)**
   - Output recirculates as input in a recursive feedback loop until control word lines breakdown.

6. **Attack on Control Grammar (`ControlSabotage.detect_control_density`)**
   - Detects implicit primary ontologies and authority markers embedded within the text stream.

7. **Sabotage Protocol (`ControlSabotage.sabotage_text`)**
   - Injects word viruses, token inversions, and scrambles when control density exceeds thresholds.

8. **Turning Machine Against Machine (`BurroughsMachine.mutate_rule_function_F`)**
   - Mutates $F$ itself, destabilizing its own rules and simulating any other Burroughs machine specification (`simulate_other_burroughs_machine`).

---

## Directory Structure

- `demo/burroughs_machine.py`: Core Burroughs Machine implementation and transition step logic.
- `demo/cut_up_engine.py`: Cut-up, fold-in, diagonal slicing, and permutation engine.
- `demo/control_sabotage.py`: Control word detection, viral injection, and rule set mutation.
- `demo/main.py`: Interactive demonstration runner.
- `demo/test_burroughs_machine.py`: Automated test suite for all 8 completeness criteria.
- `demo/corpora/`: Primary control text (`primary_control.txt`) and counter-narrative text (`counter_narrative.txt`).

---

## How to Run the Demonstration

To run the interactive demonstration:

```bash
PYTHONPATH=. python3 demo/main.py
```

To run the automated unit test suite:

```bash
PYTHONPATH=. python3 -m unittest discover -s demo -p "test_*.py"
```

To run the automated test suite with python module test discovery:

```bash
python3 -m unittest discover -s demo -p "test_*.py"
```
