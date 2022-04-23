#include <stdio.h>

long puzzle2(char *s, char *d) {
    for (int i = 0; 1; i++) {
        int j = 0;
        do {if (d[j] == '\0') return i;} while (s[i] != d[j++]);
    }
}

int main() {
    char s[] = "abcdef";
    char d[] = "acbdef";

    printf("%ld\n", puzzle2(s, d));

    return 0;   
}