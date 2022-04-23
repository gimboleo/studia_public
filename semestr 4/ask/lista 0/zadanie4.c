#include <stdio.h>

int main() {
    unsigned long x, y, a, b, c, d;

    scanf("%lu %lu", &x, &y);

    a = x << y;
    // przesunięcie o y bitów w lewo

    b = x >> y;
    // przesunięcie o y bitów w prawo

    c = x & ((1 << y) - 1);
    // wyzerowanie wszystkich bitów
    // poza y najmniej znaczącymi

    d = 1 + ((x - 1) >> y);
    // https://en.wikipedia.org/wiki/Floor_and_ceiling_functions#Quotients

    printf("%lu\n%lu\n%lu\n%lu\n", a, b, c, d);

    return 0;
}