"""
Cut-Up and Fold-In Engine for the Burroughs Machine.

Provides text segmentation, permutation, diagonal slicing, and fold-in operators.
"""

import random
import re
from typing import List, Tuple

class CutUpEngine:
    def __init__(self, seed: int = None):
        if seed is not None:
            random.seed(seed)

    def segment_words(self, text: str) -> List[str]:
        """Decompose text into individual word tokens."""
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

    def classic_cut_up(self, text: str, num_cuts: int = 4) -> str:
        """
        Classic Burroughs 4-quadrant cut-up technique:
        Divides text into a grid and rearranges quadrant blocks.
        """
        lines = self.segment_lines(text)
        if len(lines) < 2:
            words = text.split()
            mid = len(words) // 2
            q1, q2 = words[:mid], words[mid:]
            random.shuffle(q1)
            random.shuffle(q2)
            return " ".join(q1 + q2)

        mid_line = len(lines) // 2
        top_half = lines[:mid_line]
        bottom_half = lines[mid_line:]

        # Split left and right
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

        # Permute quadrants: 4-1-3-2 or random
        quadrants = [q4, q1, q3, q2]
        recombined = []
        max_rows = max(len(q) for q in quadrants)
        for r in range(max_rows):
            row_str = " ".join(q[r] for q in quadrants if r < len(q))
            recombined.append(row_str)

        return "\n".join(recombined)

    def fold_in(self, text_a: str, text_b: str, step: int = 2) -> str:
        """
        Fold-in technique:
        Folds Text A across Text B line-by-line or phrase-by-phrase,
        creating an interwoven, temporal interference pattern.
        """
        phrases_a = self.segment_phrases(text_a, chunk_size=step)
        phrases_b = self.segment_phrases(text_b, chunk_size=step)

        folded = []
        len_a, len_b = len(phrases_a), len(phrases_b)
        max_len = max(len_a, len_b)

        for i in range(max_len):
            if i < len_a:
                folded.append(phrases_a[i])
            if i < len_b:
                folded.append(phrases_b[i])

        return " ".join(folded)

    def diagonal_slice(self, text: str) -> str:
        """
        Reads a grid of text diagonally across lines, disrupting standard left-to-right reading.
        """
        lines = [line.split() for line in self.segment_lines(text)]
        if not lines:
            return text

        words_diag = []
        max_cols = max(len(l) for l in lines)
        num_rows = len(lines)

        for d in range(num_rows + max_cols - 1):
            for r in range(num_rows):
                c = d - r
                if 0 <= c < len(lines[r]):
                    words_diag.append(lines[r][c])

        return " ".join(words_diag)
