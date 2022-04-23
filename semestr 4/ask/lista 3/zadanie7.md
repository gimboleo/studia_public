> #### Dla poniższych zadań należy podać kompletny algorytm, zatem dozwolona jest cała składnia języka C bez ograniczeń z nagłówka listy zadań. Jednakże należy używać wyłącznie operacji na typie `«int32_t»` lub `«uint32_t»`.
> **Zadanie 7.** Binarna reprezentacja liczby zmiennoprzecinkowej $f$ typu `«float»` została załadowana do zmiennej `«x»` typu `«uint32_t»`. Podaj algorytm obliczający $f \cdot 2^i$ wykonujący obliczenia na zmiennej `«x»` używając wyłącznie operacji na liczbach całkowitych. Osobno rozważ $i ≥ 0$ i $i < 0$. Zakładamy, że liczba $f$ jest znormalizowana, ale wynik operacji może dać wartość $±∞$, $±0$ lub liczbę zdenormalizowaną.
>> **Uwaga!** Dla uproszczenia należy założyć, że wynik zaokrąglamy w kierunku zera.

```c
uint32_t f(uint32_t x, int32_t i) {
    int32_t exp = ((x & 0x7f800000) >> 23) + i;

    if (exp >= 255) return x & 0x80000000 | 0x7f800000; // +-inf
    else if (exp > 0) return x & 0x807FFFFF | (exp << 23);
    else if (exp <= -23) return x & 0x80000000; // +-0
    else { // denormalizacja
        uint32_t m = (x & 0x007FFFFF >> 1) | 0x00400000;
        return x & 0x80000000 | (m >> -exp);
    }
}
```