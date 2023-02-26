/*
 * Binary search with linearly placed tree levels.
 *
 * Intel® Core™ i5-6600 CPU @ 3.30GHz
 *
 * $ ./binsearch -S 0x5bab3de5da7882ff -n 23 -t 24 -v 0
 * Time elapsed: 7.616777 seconds.
 * $ ./binsearch -S 0x5bab3de5da7882ff -n 23 -t 24 -v 1
 * Time elapsed: 2.884369 seconds.
 */
#include "binsearch.h"

bool binsearch0(T *arr, long size, T x) {
  do {
    size >>= 1;
    T y = arr[size];
    if (y == x)
      return true;
    if (y < x)
      arr += size + 1;
  } while (size > 0);
  return false;
}

void linearize(T *dst, T *src, long size) {
  long i = 0;
  long j;
  long bucket_size = size;
  while (i < size) {
    j = bucket_size >> 1;
    while (i < size && j < size) {
      dst[i++] = src[j++];
      j += bucket_size;
    }
    bucket_size >>= 1;
  }
}

bool binsearch1(T *arr, long size, T x) {
  long i = 0;
  while (i < size) {
    T y = arr[i];
    if (y == x)
      return true;
    i = (i << 1) + 1;
    i += (y < x);
  }
  return false;
}
