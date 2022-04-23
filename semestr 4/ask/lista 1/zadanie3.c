#include <stdio.h>
#include <stdint.h>

struct A {
    int8_t a;   // 1 bajt
                // 7 bajtów
     void *b;   // 8 bajtów 
     int8_t c;  // 1 bajt
                // 1 bajt
     int16_t d; // 2 bajty
                // 4 bajty
              // = 24 bajty
};

struct A1 {
    int8_t a;  // 1 bajt
    int8_t c;  // 1 bajt
    int16_t d; // 2 bajty
               // 4 bajty
    void *b;   // 8 bajtów 
             // = 16 bajtów
};

struct B {
    uint16_t a; // 2 bajty
                // 6 bajtów
    double b;   // 8 bajtów
    void *c;    // 8 bajtów
             // =  24 bajty
};

int main() {
    struct A a;
    struct A1 a1;
    struct B b;

    printf("%ld %ld %ld %ld %ld\n", sizeof(a.a), sizeof(a.b), sizeof(a.c), sizeof(a.d), sizeof(a));
    printf("%ld %ld %ld %ld %ld\n", sizeof(a1.a), sizeof(a1.b), sizeof(a1.c), sizeof(a1.d), sizeof(a1));
    printf("%ld %ld %ld %ld\n", sizeof(b.a), sizeof(b.b), sizeof(b.c), sizeof(b));

    return 0;
}