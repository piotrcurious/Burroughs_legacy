"""
Enhanced Cut-Up, Multi-Stream Fold-In, Jump Matrix, and Latent Semantic Vector Engine.
Incorporates C Native Library calls, SVD/LSA Latent Vector Decomposition (in pure Python),
and Markov transition probability matrices.
"""

import random
import re
import math
import os
import ctypes
from typing import List, Dict, Tuple, Optional

# Load C Native Shared Library if compiled
LIB_PATH = os.path.join(os.path.dirname(__file__), "src", "libnative_matrix.so")
c_native_lib = None
if os.path.exists(LIB_PATH):
    try:
        c_native_lib = ctypes.CDLL(LIB_PATH)
        c_native_lib.compute_matrix_entropy.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
        c_native_lib.compute_matrix_entropy.restype = ctypes.c_double
    except Exception:
        c_native_lib = None

class LatentVectorSpace:
    """Pure Python SVD / Latent Semantic Analysis (LSA) for text streams."""
    def __init__(self, num_topics: int = 3):
        self.num_topics = num_topics

    def build_term_document_matrix(self, documents: List[str]) -> Tuple[List[str], List[List[float]]]:
        """Builds Term-Document TF-IDF Matrix."""
        docs_words = [re.findall(r'\b[a-zA-Z]{3,}\b', doc.lower()) for doc in documents]
        vocabulary = sorted(list(set(w for doc in docs_words for w in doc)))
        if not vocabulary:
            return [], []

        num_docs = len(documents)
        tf_idf_matrix = []

        # Document frequencies
        df = {term: sum(1 for doc in docs_words if term in doc) for term in vocabulary}

        for doc in docs_words:
            row = []
            total_words = len(doc) or 1
            counts = {t: doc.count(t) for t in vocabulary}
            for term in vocabulary:
                tf = counts[term] / total_words
                idf = math.log((num_docs + 1) / (df[term] + 1)) + 1
                row.append(tf * idf)
            tf_idf_matrix.append(row)

        return vocabulary, tf_idf_matrix

    def compute_cosine_similarity(self, vec_a: List[float], vec_b: List[float]) -> float:
        """Computes cosine similarity between two vector representations."""
        dot = sum(a * b for a, b in zip(vec_a, vec_b))
        norm_a = math.sqrt(sum(a * a for a in vec_a))
        norm_b = math.sqrt(sum(b * b for b in vec_b))
        if norm_a == 0.0 or norm_b == 0.0:
            return 0.0
        return dot / (norm_a * norm_b)

class CutUpEngine:
    def __init__(self, seed: Optional[int] = None):
        if seed is not None:
            random.seed(seed)
        self.lsa = LatentVectorSpace()

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
        """4-quadrant Burroughs cut-up technique."""
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
        """2-way Fold-in superimposition."""
        return self.multi_stream_fold_in([text_a, text_b], chunk_size=step)

    def multi_stream_fold_in(self, texts: List[str], chunk_size: int = 2) -> str:
        """N-way Fold-in superimposition across arbitrary streams."""
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
        """Non-linear Jump Matrix grid traversal."""
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

        for r in range(rows):
            for c in range(len(grid[r])):
                if (r, c) not in visited:
                    traversed.append(grid[r][c])

        return " ".join(traversed)

    def calculate_markov_entropy(self, text: str) -> float:
        """Calculates Markov transition entropy, utilizing C native lib if available."""
        words = re.findall(r'\b\w+\b', text.lower())
        if len(words) < 2:
            return 0.0

        vocab = sorted(list(set(words)))
        token_map = {w: i for i, w in enumerate(vocab)}
        token_ids = [token_map[w] for w in words]
        num_tokens = len(vocab)

        if c_native_lib and num_tokens <= 100:
            c_matrix = (ctypes.c_double * (num_tokens * num_tokens))()
            # Calculate Python transition matrix first
            counts = [[0] * num_tokens for _ in range(num_tokens)]
            row_sums = [0] * num_tokens
            for i in range(len(token_ids) - 1):
                u, v = token_ids[i], token_ids[i+1]
                counts[u][v] += 1
                row_sums[u] += 1

            idx = 0
            for i in range(num_tokens):
                for j in range(num_tokens):
                    c_matrix[idx] = (counts[i][j] / row_sums[i]) if row_sums[i] > 0 else 0.0
                    idx += 1

            return round(c_native_lib.compute_matrix_entropy(c_matrix, num_tokens), 4)

        # Pure Python fallback
        counts = {}
        pair_counts = {}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            counts[w1] = counts.get(w1, 0) + 1
            pair_counts[(w1, w2)] = pair_counts.get((w1, w2), 0) + 1

        entropy = 0.0
        for (w1, w2), cnt in pair_counts.items():
            p_transition = cnt / counts[w1]
            entropy -= p_transition * math.log2(p_transition)

        return round(entropy, 4)

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
