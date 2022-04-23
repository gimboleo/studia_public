#include <stdio.h>

int main() {
    unsigned long x;

    scanf("%lu", &x);

    x = ((x == 0) || (x & (x - 1)));

    printf("%lu\n", x);

    return 0;
}