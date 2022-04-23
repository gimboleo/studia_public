> **Zadanie 2.** Zaimplementuj funkcję zdefiniowaną poniżej w asemblerze `x86-64`. Taka procedura w języku C miałaby sygnaturę `«long cmp(uint64_t x, uint64_t y)»`.
> $$cmp(x, y) = \left \{ \begin{array}{}
> −1 & gdy & x < y \\
> 1 & gdy & x > y \\
> 0 & gdy & x = y
> \end{array} \right.$$
>> **Wskazówka:** Rozwiązanie wzorcowe ma cztery wiersze (bez `«ret»`). Użyj instrukcji `adc`, `sbb` i `neg`.

# [Instrukcja neg](https://www.felixcloutier.com/x86/neg)

```assembly
cmp:    subq %rsi, %rdi
        sbbq %rax, %rax     ;borrow <=> x < y ? -1 : 0
        negq %rdi           ;CF = (x - y == 0) ? 0 : 1 
        adcq %rax, %rax
        ret
```

$$adcq \ \%rax, \ \%rax = \left \{ \begin{array}{}
−1 - 1 + 1 = -1 & gdy & x < y \\
0 + 0 + 1 = 1 & gdy & x > y \\
0 + 0 + 0 = 0 & gdy & x = y
\end{array} \right.$$