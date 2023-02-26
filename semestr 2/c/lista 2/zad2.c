#include <stdio.h>
#include <stdbool.h>
#include <assert.h>
#define N_MAX 777

struct mem_entry {
    unsigned long value;
    bool valid;
};

struct mem_entry memory[N_MAX][N_MAX];

unsigned long Stirling(unsigned short n, unsigned short k) {
    if (k == 1) return 1;
    if (k == n) return 1;
    if (k == 0)
    {
        if (n == 0) return 1;
        return 0;
    }

    if (n < k) return 0;

    return k * Stirling(n-1, k) + Stirling(n-1, k-1);
}

unsigned long Stirling1(unsigned short n, unsigned short k) {
    if (memory[n][k].value != 0) return memory[n][k].value;
    
    if (k == 1) {
        memory[n][k].value = 1;
        return 1;
    }
    if (k == n) {
        memory[n][k].value = 1;
        return 1;
    }
    if (k == 0)
    {
        if (n == 0) {
            memory[n][k].value = 1;
            return 1;
        }
        return 0;
    }

    if (n < k) return 0;

    unsigned long x = k * Stirling1(n-1, k) + Stirling1(n-1, k-1);
    memory[n][k].value = x;
    return x;
}

int main() {
    assert(Stirling(5,0) == 0);
    assert(Stirling(7,1) == 1);
    assert(Stirling(3,2) == 3);
    assert(Stirling(4,3) == 6);
    assert(Stirling(2,4) == 0);
    assert(Stirling(8,5) == 1050);

    assert(Stirling1(9,7) == 462);
    assert(memory[8][7].value == 28);
    assert(memory[7][7].value == 1);
    assert(memory[7][6].value == 21);
    assert(Stirling1(9,5) == 6951);
    assert(memory[7][3].value == 301);
}