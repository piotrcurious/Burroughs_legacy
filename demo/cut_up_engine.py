"""
Enhanced Cut-Up, Multi-Stream Fold-In, and Jump Matrix Engine.
Supports N-way text interleave, non-linear jump matrices, diagonal slicing,
and semantic fragment permutation.
"""

import random
import re
import math
from typing import List, Dict, Tuple, Optional

class CutUpEngine:
    def __init__(self, seed: Optional[int] = None):
        if seed is not None:
            random.seed(seed)

    def segment_words(self, text: str) -> List[str]:
        """Decompose text into individual word tokens and punctuation."""
        return re.findall(r'\b\w+\b|[^\w\s]', text)

    def segment_phrases(self, text: str, chunk_size: int = 3) -> List[str]:
        """Decompose text into n-gram word chunks or phrase blocks."""
        words = text.split()
        chunks = []
        for i in range(0, len(words), chunk_size):
            chunks.append(" ".join(words[i:i + chunk_size]))
        return chunks

    def segment_lines(self, text: str) -> List[str]:
        """Decompose text into lines or sentence fragments."""
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        if not lines:
            lines = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]
        return lines

    def classic_cut_up(self, text: str, grid_size: int = 2) -> str:
        """
        4-quadrant or N-grid Burroughs cut-up technique:
        Divides text into a grid and rearranges quadrant blocks.
        """
        lines = self.segment_lines(text)
        if len(lines) < grid_size:
            words = text.split()
            mid = len(words) // 2
            q1, q2 = words[:mid], words[mid:]
            random.shuffle(q1)
            random.shuffle(q2)
            return " ".join(q1 + q2)

        mid_line = len(lines) // 2
        top_half = lines[:mid_line]
        bottom_half = lines[mid_line:]

        q1, q2, q3, q4 = [], [], [], []
        for line in top_half:
            words = line.split()
            m = len(words) // 2
            q1.append(" ".join(words[:m]))
            q2.append(" ".join(words[m:]))
        for line in bottom_half:
            words = line.split()
            m = len(words) // 2
            q3.append(" ".join(words[:m]))
            q4.append(" ".join(words[m:]))

        quadrants = [q4, q1, q3, q2]
        recombined = []
        max_rows = max(len(q) for q in quadrants)
        for r in range(max_rows):
            row_str = " ".join(q[r] for q in quadrants if r < len(q))
            recombined.append(row_str)

        return "\n".join(recombined)

    def fold_in(self, text_a: str, text_b: str, step: int = 2) -> str:
        """
        2-way Fold-in technique:
        Superimposes two streams phrase-by-phrase.
        """
        return self.multi_stream_fold_in([text_a, text_b], chunk_size=step)

    def multi_stream_fold_in(self, texts: List[str], chunk_size: int = 2) -> str:
        """
        N-way Fold-in technique:
        Superimposes N arbitrary text streams simultaneously, creating multi-stream
        temporal interference patterns and narrative bleeding.
        """
        if not texts:
            return ""
        if len(texts) == 1:
            return texts[0]

        phrase_streams = [self.segment_phrases(t, chunk_size=chunk_size) for t in texts]
        max_len = max(len(stream) for stream in phrase_streams)

        interleaved = []
        for i in range(max_len):
            for stream in phrase_streams:
                if i < len(stream):
                    interleaved.append(stream[i])

        return " ".join(interleaved)

    def jump_matrix_permutation(self, text: str, jump_step: int = 3) -> str:
        """
        Non-linear Jump Matrix:
        Arranges words in an N x M grid and traverses non-linearly using stride steps,
        simulating temporal jumps, anticipations, and déjà vu.
        """
        words = text.split()
        if len(words) < 4:
            return text

        cols = int(math.sqrt(len(words))) or 2
        grid = [words[i:i + cols] for i in range(0, len(words), cols)]

        traversed = []
        rows = len(grid)
        curr_r, curr_c = 0, 0

        visited = set()
        total_cells = sum(len(r) for r in grid)
        max_iterations = total_cells * 4
        iterations = 0

        while len(traversed) < total_cells and iterations < max_iterations:
            iterations += 1
            if (curr_r, curr_c) not in visited and curr_r < rows and curr_c < len(grid[curr_r]):
                traversed.append(grid[curr_r][curr_c])
                visited.add((curr_r, curr_c))

            curr_r = (curr_r + jump_step) % rows
            curr_c = (curr_c + 1) % cols

        # Append any unvisited cells deterministically
        for r in range(rows):
            for c in range(len(grid[r])):
                if (r, c) not in visited:
                    traversed.append(grid[r][c])

        return " ".join(traversed)

    def calculate_semantic_entropy(self, text: str) -> float:
        """Calculates Shannon entropy over word tokens."""
        words = re.findall(r'\b\w+\b', text.lower())
        if not words:
            return 0.0
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        total = len(words)
        entropy = -sum((cnt / total) * math.log2(cnt / total) for cnt in counts.values())
        return round(entropy, 4)
