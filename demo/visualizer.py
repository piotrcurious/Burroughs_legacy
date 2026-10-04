"""
Visualization & Web Control Dashboard for the Burroughs-Complete Machine.

Renders ASCII terminal control visualizers, SVG co-occurrence graph visualizations,
and exports standalone HTML/JS dashboards.
"""

import os
import json
from typing import Dict, List, Any

class Visualizer:
    @staticmethod
    def render_ascii_dashboard(step_result: Dict[str, Any], gnosis_analysis: Dict[str, Any]) -> str:
        """Renders an ASCII visualization of machine registers, entropy, and gnosis insights."""
        reg = step_result["registers"]
        lines = []
        lines.append("+" + "=" * 70 + "+")
        lines.append("|            BURROUGHS MACHINE REAL-TIME CONTROL DASHBOARD            |")
        lines.append("+" + "=" * 70 + "+")
        lines.append(f"| Cycle: {reg['cycle_count']:<5} | State: {reg['state']:<18} | Head Pos: {reg['head_pos']:<5} |")
        lines.append(f"| Control Density: {reg['control_density']:<6.3f} | Entropy: {reg['entropy_bits']:<5.3f} bits | Mut Level: {reg['mutation_level']:<3} |")
        lines.append("+" + "-" * 70 + "+")
        lines.append("| OUTPUT STREAM:")
        out_snippet = step_result['sabotaged_output'][:150] + "..." if len(step_result['sabotaged_output']) > 150 else step_result['sabotaged_output']
        lines.append(f"| {out_snippet}")
        lines.append("+" + "-" * 70 + "+")
        lines.append("| HIRSCH HERMENEUTICS & GNOSIS INSIGHTS:")
        hirsch = gnosis_analysis.get("hirsch_hermeneutics", {})
        if hirsch.get("verbal_meaning"):
            lines.append(f"|  * {hirsch['verbal_meaning']}")
        for ins in gnosis_analysis.get("third_mind_insights", [])[:2]:
            lines.append(f"|  * {ins}")
        lines.append("+" + "=" * 70 + "+")
        return "\n".join(lines)

    @staticmethod
    def generate_html_dashboard(history: List[Dict[str, Any]], output_filepath: str = "demo/dashboard.html") -> None:
        """Generates an interactive HTML/JS dashboard with SVG graph representations."""
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Burroughs Machine Visualizer</title>
    <style>
        body {{ background-color: #0d1117; color: #c9d1d9; font-family: monospace; padding: 20px; }}
        h1 {{ color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 10px; }}
        .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 15px; margin-bottom: 20px; }}
        .metric {{ display: inline-block; margin-right: 20px; font-weight: bold; color: #79c0ff; }}
        .sabotaged {{ color: #ff7b72; background: #220000; padding: 10px; border-left: 3px solid #f85149; }}
        .insight {{ color: #d2a8ff; font-style: italic; }}
        svg {{ background: #010409; border: 1px solid #30363d; margin-top: 10px; }}
    </style>
</head>
<body>
    <h1>Burroughs-Complete Machine Real-Time Control Dashboard</h1>
    <p>Universality over transformations of the representational & control system itself: M_{{t+1}} = F(M_t, x_t, y_t).</p>
"""
        for step in history:
            reg = step["registers"]
            html_content += f"""
    <div class="card">
        <h2>Cycle {reg['cycle_count']} - State: {reg['state']}</h2>
        <div>
            <span class="metric">Control Density: {reg['control_density']}</span>
            <span class="metric">Markov Entropy: {reg['entropy_bits']} bits</span>
            <span class="metric">Mutation Level: {reg['mutation_level']}</span>
        </div>
        <h3>Sabotaged Output Stream:</h3>
        <div class="sabotaged">{step['sabotaged_output']}</div>
    </div>
"""
        html_content += "</body>\n</html>"

        with open(output_filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
