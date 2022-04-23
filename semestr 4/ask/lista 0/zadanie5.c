#include <stdio.h>

int main() {
    long x;

    scanf("%ld", &x);

    x = ~x + 1;
    // negacja x i dodanie 1

    printf("%ld\n", x);

    return 0;
}