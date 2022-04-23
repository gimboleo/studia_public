> **Zadanie 1.** Zaimplementuj poniższą funkcję w asemblerze `x86-64`. Wartości `«x»` i `«y»` typu `«uint64_t»` są przekazywane przez rejestry `%rdi` i `%rsi`, a wynik zwracany w rejestrze `%rax`. Najpierw rozwiąż zadanie używając instrukcji skoku warunkowego. Potem przepisz je używając instrukcji `«sbb»`.
>$$addu(x, y) = \left \{ \begin{array}{}
> ULONG\_MAX & dla & x + y ≥ ULONG\_MAX \\
> x + y & w.p.p.
> \end{array} \right.$$
>> **Wskazówka!** Rozwiązanie wzorcowe składa się z 3 instrukcji bez `«ret»`.

# [Instrukcja sbb](https://www.felixcloutier.com/x86/sbb)


```assembly
addu:   addq %rsi %rdi
        jnc jump    ;jump if CF = 0 (carry flag)
        movq $ULONG_MAX %rdi
jump:   movq %rdi %rax
        ret
```

```assembly
addu:   addq %rsi %rdi
        sbbq %rax %rax  ;carry ? -1 = ULONG_MAX : 0
        orq %rdi %rax   ;carry ? -1 : %rdi + %rsi
        ret
```