#include <stdio.h>
#include <stdint.h>
#include <stdalign.h>
#include <stddef.h>

struct node {
    char id[2];                     // 1 * 2 bajty
                                    // 6 bajtów
    int (*hashfn)(char *);          // 8 bajtów
    short flags;                    // 2 bajty
                                    // 2 bajty
    union {
        struct {
            short n_key;                    // 2 bajty
                                            // 2 bajty
            int n_data[2];                  // 2 * 4 bajtów
            unsigned char n_type;           // 1 bajt
                                            // 3 bajty
        } s;                            // 16 bajtów
        unsigned l_value[2];            // 2 * 4 bajtów
    } u;                            // 16 bajtów
                                    // 4 bajty
                                  // = 40 bajtów
};

struct node1 {
    union {
        struct {
            int n_data[2];                  // 2 * 4 bajtów
            short n_key;                    // 2 bajty
            unsigned char n_type;           // 1 bajt
                                            // 1 bajt
        } s;                            // 12 bajtów                            
        unsigned l_value[2];            // 2 * 4 bajtów
    } u;                            // 12 bajtów     
    short flags;                    // 2 bajty
    char id[2];                     // 1 * 2 bajty             
    int (*hashfn)(char *);          // 8 bajtów
                                  // = 24 bajty
};

int main() {
    struct node n;
    struct node1 n1;

    printf("%ld %ld %ld %ld %ld\n", sizeof(n.id), sizeof(n.hashfn), sizeof(n.flags), sizeof(n.u), sizeof(n));
    printf("%ld %ld %ld %ld %ld\n", alignof(n.id), alignof(n.hashfn), alignof(n.flags), alignof(n.u), alignof(n));
    printf("%ld %ld %ld %ld\n", offsetof(struct node, id), offsetof(struct node, hashfn), offsetof(struct node, flags), offsetof(struct node, u));
    printf("\n");

    printf("%ld %ld %ld %ld %ld\n", sizeof(n1.id), sizeof(n1.hashfn), sizeof(n1.flags), sizeof(n1.u), sizeof(n1));
    printf("%ld %ld %ld %ld %ld\n", alignof(n1.id), alignof(n1.hashfn), alignof(n1.flags), alignof(n1.u), alignof(n1));
    printf("%ld %ld %ld %ld\n", offsetof(struct node1, id), offsetof(struct node1, hashfn), offsetof(struct node1, flags), offsetof(struct node1, u));

    return 0;
}