> **Zadanie 3.** Na podstawie kodu wynikowego z kompilatora odtwórz zoptymalizowaną wersję funkcji `«foobar»` w języku `C`. Wskaż w poniższym kodzie **niezmienniki pętli** (ang. *loop invariants*), **zmienne indukcyjne** (ang. *induction variable*). Które wyrażenia zostały wyniesione przed pętlę i dlaczego? Które wyrażenia uległy **osłabieniu** (ang. *strength reduction*)?

```c
void foobar(long a[], size_t n, long y, long z) {
    for (int i = 0; i < n; i++) {
        long x = y - z; 
        long j = 7 * i;
        a[i] = j + x * x;
    }
}
```

- Niezmienniki pętli: `x`, `x * x`
- Zmienne indukcyjne: `i`, `j`

[Godbolt](https://godbolt.org/z/PEajWr8zW)

```c
void foobar_opt(long a[], int n, long y, long z) {
    long x = y - z;
    x = x * x;
    for (int i = 0; i < n; i++) {
        a[i] = x;
        x += 7;
    }
}
```

Obliczenie `x` i `x * x` zostało wyniesione poza pętle, ponieważ wyrażenia te są niezmiennikami pętli (ich wartość nie zmienia się miedzy iteracjami).

Następnie osłabione zostało wyrażenie `long j = 7 * i; a[i] = j + x`. Zostało zastąpione dużo prostszym `a[i] = x; x += 7`.