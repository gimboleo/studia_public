> #### Dla poniższych zadań należy podać kompletny algorytm, zatem dozwolona jest cała składnia języka C bez ograniczeń z nagłówka listy zadań. Jednakże należy używać wyłącznie operacji na typie `«int32_t»` lub `«uint32_t»`.
> **Zadanie 8.** Napisz ciało procedury o sygnaturze `«int32_t int2float(int32_t i)»` konwertującej wartość całkowitoliczbową do binarnej reprezentacji liczby typu `«float»`. Wynik należy zaokrąglić do najbliższej liczby parzystej – w tym celu wyznacz wartość bitów **guard**, **round** i **sticky**. Do wyznaczenia pozycji wiodącej jedynki można użyć funkcji `«__builtin_clz»`, tj. [instrukcji wbudowanej](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html) w kompilator `gcc`.
>> **Wskazówka:** Rozwiązanie jest łatwiejsze do zrozumienia, jeśli mantysę zapisze się na najbardziej znaczących bitach.

```c
int32_t int2float(int32_t i) {
    if (i == 0) return 0;
    if (i == INT32_MIN) return 0xCF000000;
    // -1 * 2^(31) * 1; 31 + 127 = 158

    int32_t sign = i & 0x80000000;
    if (sign) i *= -1;

    uint32_t sig = 32 - __builtin_clz(i);
    uint32_t exp = sig - 1 + 127;
    uint32_t shifted;

    if (sig <= 24) shifted = (i & ~(1 << sig - 1)) << (24 - sig);
    // Nie trzeba zaokraglac
    else {
        // Trzeba zaokraglac
        uint32_t guard = (i >> (sig - 24)) & 1;
        uint32_t round = (i >> (sig - 25)) & 1;
        uint32_t sticky = (i << (32 - (sig - 25))) != 0;

        shifted = i >> (sig - 24);
        if (round && (sticky || guard)) {
            shifted++;
            // Mozliwe zapalenie dodatkowego bitu przy zaokragleniu
            if (32 - __builtin_clz(shifted) > 24) {
                i >> 1;
                exp += 1;
            }
        }
        shifted &= ~(1 << 24);
    }

    return sign || (exp << 23) | shifted;
}
```