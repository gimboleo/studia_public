> **Zadanie 6.** Przeczytaj definicje struktur `«SA»` i `«SB»`, po czym przeanalizuj kod procedur o sygnaturach `«SB eval(SA s)»` i `«long wrap(long x, long y, long z)»`. Nastepnie zapisz w języku C kod odpowiadający procedurom `«eval»` i `«wrap»`. Narysuj diagram przedstawiający zawartość rekordu aktywacji procedury `«wrap»` w momencie wywołania funkcji `«eval»`.

```c
typedef struct A {
    long u[2];      // 2 * 8 bajtów      
    long *v;        // 8 bajtów
                  // = 24 bajty
} SA;

typedef struct B {
    long p[2];      // 2 * 8 bajtów
    long q;         // 8 bajtów
                  // = 24 bajty
} SB;
```

```assembly
eval:   movq %rdi, %rax         ;%rax = &res
        movq 16(%rsp), %rcx     ;%rcx = s.u[1]     
        movq 24(%rsp), %rdx     ;%rdx = s.v
        movq (%rdx), %rsi       ;%rsi = *(s.v)
        movq %rcx, %rdx
        imulq %rsi, %rdx
        movq %rdx, (%rdi)       ;res.p[0] = s.u[1] * *(s.v)
        movq 8(%rsp), %rdx      ;%rdx = s.u[0]
        movq %rdx, %rdi
        subq %rsi, %rdi
        movq %rdi, 8(%rax)      ;res.p[1] = s.u[0] - *(s.v)
        subq %rcx, %rdx
        movq %rdx, 16(%rax)     ;res.q = s.u[0] - s.u[1]
        ret
    
wrap:   subq $72, %rsp          ;alokacja miejsca na stosie
        movq %rdx, (%rsp)       ;z = *(s.v)
        movq %rsp, %rdx
        leaq 8(%rsp), %rax
        pushq %rdx              ;&z = s.v
        pushq %rsi              ;y = s.u[1]
        pushq %rdi              ;x = s.u[0]
        movq %rax, %rdi         ;%rdi = %original_rsp - 72 + 8
        call eval
        movq 40(%rsp), %rax
        addq 32(%rsp), %rax
        imulq 48(%rsp), %rax    ;return (res.p[1] + res.p[0]) * res.q
        addq $96, %rsp          ;sprzątanie stosu
        ret
```

|    Wartość    | Adres |    Dodatkowe informacje   |
|:-------------:|:-----:|:-------------------------:|
| Adres powrotu |   96  |       Pierwotny %rsp      |
|               |   88  |                           |
|               |   80  |                           |
|               |   72  |                           |
|               |   64  |                           |
|               |   56  |                           |
|               |   48  |      Miejsce na res.q     |
|               |   40  |    Miejsce na res.p[1]    |
|               |   32  | %rdi; Miejsce na res.p[0] |
|       z       |   24  |  *(s.v) dla funkcji eval  |
|       &z      |   16  |    s.v dla funkcji eval   |
|       y       |   8   |  s.u[1] dla funkcji eval  |
|       x       |   0   |  s.u[0] dla funkcji eval  |
| Adres powrotu |   -8  |                           |

```c
SB eval(SA s) {
    SB res;
    res.p[0] = s.u[1] * *(s.v);
    res.p[1] = s.u[0] - *(s.v);
    res.q = s.u[0] - s.u[1];
    return res;
}

long wrap(long x, long y, long z) {
    SA a = {{x, y}, &z};
    SB b = eval(a);
    return (b.p[1] + b.p[0]) * b.q;
}
```