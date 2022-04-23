>**Zadanie 6.** Napisz ciąg instrukcji w języku C, który zmieni miejscami najmniej znaczące 8 bitów zmiennych x i y. Możesz wprowadzić jedną zmienną tymczasową

```c
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
```

Liczba $0xFF$ posłużyła nam jako maska, jej postać binarna to $0000 \space 0000 \space 0000 \space 0000 \space 0000 \space 0000 \space 1111 \space 1111$.

Za pomocą maski i operacji AND wyzerowaliśmy określone segmenty liczb, a następnie uzupełniliśmy wyzerowane bity za pomocą negacji maski i XOR'a.