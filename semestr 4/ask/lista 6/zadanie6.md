> **Zadanie 6.** Poniżej widnieje kod procedury o sygnaturze `«long puzzle6(void)»`. Narysuj rekord aktywacji procedury `«puzzle6»`, podaj jego rozmiar i składowe. Procedura `«readlong»`, która wczytuje ze standardowego wejścia liczbę całkowitą, została zdefiniowana w innej jednostce translacji. Jaka jest jej sygnatura? Przetłumacz procedurę `«puzzle6»` na język C i wytłumacz jednym zdaniem co ona robi.

```assembly
puzzle6:    subq $24, %rsp      ;alokacja miejsca na stosie
            movq %rsp, %rdi     ;+padding
            call readlong       ;%rsp = readlong() = a
            leaq 8(%rsp), %rdi
            call readlong       ;%rsp + 8 = readlong() = b
            movq (%rsp), %rax
            cqto
            idivq 8(%rsp)
            xorl %eax, %eax     ;res = 0
            testq %rdx, %rdx
            sete %al            ;a % b == 0 => res = 1
            addq $24, %rsp      ;sprzątanie stosu
            ret
```

```c
void readlong(long *x);

long puzzle5() {
    long a, b;

    readlong(&a);
    readlong(&b);
    
    return !(a % b);
}
```

Procedura ta wczytuje za pomocą funkcji $readlong$ 2 liczby i zwraca informację, czy pierwsza jest podzielna przez drugą.

|    Wartość    | Rozmiar |
|:-------------:|:-------:|
|               |    8    |
|      $b$      |    8    |
|      $a$      |    8    |
| Adres powrotu |    8    |