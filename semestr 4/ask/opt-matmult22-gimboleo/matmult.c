/*
 * Matrix multiplication with and without blocking.
 *
 * Intel® Core™ i5-6600 CPU @ 3.30GHz
 *
 * $ ./matmult -n 1024 -v 0
 * Time elapsed: 3.052755 seconds.
 * $ ./matmult -n 1024 -v 1
 * Time elapsed: 0.746337 seconds.
 * $ ./matmult -n 1024 -v 2
 * Time elapsed: 9.882309 seconds.
 * $ ./matmult -n 1024 -v 3
 * Time elapsed: 0.698795 seconds.
 */
#include "matmult.h"

/* Useful macro for accessing row-major 2D arrays of size n×n. */
#define M(a, i, j) a[(i) * n + (j)]

/* ijk (& jik) */
void matmult0(int n, T_p a, T_p b, T_p c) {
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      T sum = 0.0;
      for (int k = 0; k < n; k++) sum += M(a, i, k) * M(b, k, j);
      M(c, i, j) = sum;
    }
  }
}

/* kij (& ikj) */
void matmult1(int n, T_p a, T_p b, T_p c) {
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      T r = M(a, i, k);
      for (int j = 0; j < n; j++) M(c, i, j) += r * M(b, k, j);
    }
  }
}

/* jki (& kji) */
void matmult2(int n, T_p a, T_p b, T_p c) {
  for (int j = 0; j < n; j++) {
    for (int k = 0; k < n; k++) {
      T r = M(b, k, j);
      for (int i = 0; i < n; i++) M(c, i, j) += r * M(a, i, k);
    }
  }
}

/* BLOCK*BLOCK tiled version */
void matmult3(int n, T_p a, T_p b, T_p c) {
  for (int i = 0; i < n; i += BLOCK) {
    for (int j = 0; j < n; j += BLOCK) {
      for (int k = 0; k < n; k += BLOCK) {
        for (int ii = i; ii < i + BLOCK; ii++) {
          for (int jj = j; jj < j + BLOCK; jj++) {
            for (int kk = k; kk < k + BLOCK; kk++) M(c, ii, jj) += M(a, ii, kk) * M(b, kk, jj);
          }
        }
      }
    }
  }
}
