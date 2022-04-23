> **Zadanie 1.** Zmienne $i, k$ spełniają warunek $0 ≤ i, k ≤ 31$. Napisz ciąg instrukcji w języku C, który skopiuje $i$-ty bit zmiennej $x$ na pozycję $k$-tą. Najpierw pokaż rozwiązanie pośrednie używające instrukcji warunkowej.
>> **Uwaga!** Musisz rozpatrzyć trzy przypadki: $i < k, i > k$ oraz $i = k$.

```c
#include <stdio.h>

int main() {
    unsigned long x, i, k, aux;

    scanf("%lu %lu $lu", &x, &i, &k);

    aux = x & (1 << i);
    // zerujemy wszystki bity poza i-tym
    aux = k >= i ? aux << (k - i) : aux >> (i - k)
    // przesuwamy ten bit na odpowiednie miejsce
    x = (x & ~(1<<k)) | aux;
    // zerujemy k-ty bit w x
    // po czym ustawiamy go na wartość aux

    printf("%lu\n", x);

    return 0;
}
```

```c
#include <stdio.h>

int main() {
    unsigned long x, i, k, aux;

    scanf("%lu %lu $lu", &x, &i, &k);

    aux = (x >> i) & 1;
    // wyciągamy i-ty bit do zmiennej
    x = (x & ~(1<<k)) | (aux << k);
    // zerujemy k-ty bit w x
    // po czym ustawiamy go na wartość aux

    printf("%lu\n", x);

    return 0;
}
```