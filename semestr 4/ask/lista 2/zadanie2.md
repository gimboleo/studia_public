> **Zadanie 2.** Napisz ciąg instrukcji, który bez użycia dodatkowych zmiennych zamieni miejscami zawartość zmiennych `«x»` i `«y»`.
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §2.19 książki „Uczta programistów”.

> ```c
> x = x ^ y;
> y = x ^ y;
> x = x ^ y;
> ```

1. $x \leftarrow x \veebar y; \space y \leftarrow y$
2. $x \leftarrow x \veebar y; \space y \leftarrow (x \veebar y) \veebar y = x \veebar (y \veebar y) = x \veebar 0 = x$
3. $x \leftarrow x \veebar (x \veebar y) = y; \space y \leftarrow x$