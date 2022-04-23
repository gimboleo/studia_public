#include <stdio.h>

int main() {
    unsigned long x, y, aux;

    scanf("%lu %lu", &x, &y);

    aux = y & 0xFF;
    y = (y & ~0xFF) ^ (x & 0xFF);
    x = (x & ~0xFF) ^ aux;

    printf("%lu\n%lu\n", x, y);

    return 0;
}