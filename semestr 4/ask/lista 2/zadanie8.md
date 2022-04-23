> **Zadanie 8.** Podaj fragment kodu, który oblicza funkcję:
$sign(x) = \left \{ \begin{array}{} 
-1 & dla & x < 0  \\ 
0 & dla & x = 0 \\
1 & dla & x > 0
\end{array} \right.$
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §2.7 książki „Uczta programistów”.

```c
int abs(int x) {
    // Dla x < 0: -1 | (0 / 1 dla minimalnego x) == -1
    // Dla x == 0: 0 | 0 == 0
    // Dla x > 0: 0 | 1 == 1
    return (x >> N - 1) | (~x + 1 >> N - 1 & 1);
}
```