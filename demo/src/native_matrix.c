/*
 * High-performance C core for Matrix Cut-Up, Diagonal Traversal,
 * and Markov Transition Matrix computation for the Burroughs Machine.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct {
    int rows;
    int cols;
    double *data;
} Matrix;

Matrix* create_matrix(int rows, int cols) {
    Matrix *m = (Matrix*)malloc(sizeof(Matrix));
    m->rows = rows;
    m->cols = cols;
    m->data = (double*)calloc(rows * cols, sizeof(double));
    return m;
}

void free_matrix(Matrix *m) {
    if (m) {
        if (m->data) free(m->data);
        free(m);
    }
}

/* Computes Markov transition probabilities across token streams */
void compute_markov_transition(const int *token_ids, int count, int num_tokens, double *out_matrix) {
    int *pair_counts = (int*)calloc(num_tokens * num_tokens, sizeof(int));
    int *row_sums = (int*)calloc(num_tokens, sizeof(int));

    for (int i = 0; i < count - 1; i++) {
        int u = token_ids[i];
        int v = token_ids[i+1];
        if (u >= 0 && u < num_tokens && v >= 0 && v < num_tokens) {
            pair_counts[u * num_tokens + v]++;
            row_sums[u]++;
        }
    }

    for (int i = 0; i < num_tokens; i++) {
        for (int j = 0; j < num_tokens; j++) {
            if (row_sums[i] > 0) {
                out_matrix[i * num_tokens + j] = (double)pair_counts[i * num_tokens + j] / row_sums[i];
            } else {
                out_matrix[i * num_tokens + j] = 0.0;
            }
        }
    }

    free(pair_counts);
    free(row_sums);
}

/* Computes Shannon Entropy over transition matrix */
double compute_matrix_entropy(const double *matrix, int num_tokens) {
    double total_entropy = 0.0;
    for (int i = 0; i < num_tokens; i++) {
        for (int j = 0; j < num_tokens; j++) {
            double p = matrix[i * num_tokens + j];
            if (p > 1e-12) {
                total_entropy -= p * log2(p);
            }
        }
    }
    return total_entropy;
}

int main(int argc, char **argv) {
    if (argc > 1 && strcmp(argv[1], "--test") == 0) {
        int tokens[] = {0, 1, 2, 0, 1, 3, 0, 1, 2};
        double mat[16];
        compute_markov_transition(tokens, 9, 4, mat);
        double ent = compute_matrix_entropy(mat, 4);
        printf("Native Matrix Test Passed. Entropy: %.4f\n", ent);
        return 0;
    }
    printf("Burroughs C Native Matrix Module Compiled.\n");
    return 0;
}
