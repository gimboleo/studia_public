> **Zadanie 9.** Uzupełnij ciało funkcji zadeklarowanej poniżej.
> ```c
> /* Kiedy x zawiera nieparzystą liczbę jedynek zwróć 1, w p.p. 0 */
> int32_t odd_ones(uint32_t x);
> ```
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §5.2 książki „Uczta programistów”.

```c
/* Kiedy x zawiera nieparzystą liczbę jedynek zwróć 1, w p.p. 0 */
int32_t odd_ones(uint32_t x) {
    x = x ^ (x >> 1);
    x = x ^ (x >> 2);
    x = x ^ (x >> 4);
    x = x ^ (x >> 8);
    x = x ^ (x >> 16);
    return x & 1;
}
```

Pomysł jest identyczny, co w zadaniu $1.2$. Tym razem jednak obchodzi nas jedynie parzystość liczby bitów, więc zamiast dokładnego liczenia ich ilości skorzystamy z $XOR$'a.