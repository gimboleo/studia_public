> **Zadanie 5.** Na podstawie kodu wynikowego z kompilatora odtwórz zoptymalizowaną wersję funkcji `«neigh»` w języku `C`. Kompilator zastosował optymalizację **eliminacji wspólnych podwyrażeń** (ang. *common subexpression elimination*). Wskaż w poniższym kodzie, które podwyrażenia policzył tylko raz. Pokaż, że jesteś w stanie zoptymalizować funkcję lepiej niż kompilator – przepisz jej kod tak, by generował mniej instrukcji.

```c
long neigh(long a[], long n, long i, long j) {
    long ul = a[(i-1)*n + (j-1)];
    long ur = a[(i-1)*n + (j+1)];
    long dl = a[(i+1)*n - (j-1)];
    long dr = a[(i+1)*n - (j+1)];
    return ul + ur + dl + dr;
}
```
[Godbolt](https://godbolt.org/z/WPGPEb8M5)

Wyrażenia policzone tylko raz: `j - 1`, `j + 1`, `(i - 1) * n`, `(i + 1) * n`.

```c
long neigh(long a[], long n, long i, long j) {
    long l = j + 1;
    long r = j - 1;
    long d = (i + 1) * n;
    long u = d - 2 * n;
    return a[u + r] + a[u + l] + a[d - r] + a[d - l];
}
```

Możemy jeszcze bardziej zoptymalizować funkcję licząc tylko raz wyrażenia `(i - 1) * n + j` oraz `(i + 1) * n - j`:
```c
long neigh(long a[], long n, long i, long j) {
    long u = (i - 1) * n + j;
    long d = (i + 1) * n - j;
    return a[u - 1] + a[u + 1] + a[d - 1] + a[d + 1];
}
```
[Godbolt](https://godbolt.org/z/ocxxaM9fn)