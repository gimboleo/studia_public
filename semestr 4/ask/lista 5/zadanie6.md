> **Zadanie 6 (2).** Poniżej zamieszczono kod rekurencyjnej procedury o sygnaturze `«int puzzle4(long *a, long v, uint64_t s, uint64_t e)»`. Wyznacz bloki podstawowe oraz narysuj graf przepływu sterowania. Przetłumacz tę procedurę na język C, a następnie jednym zdaniem powiedz co ona robi.
>> **Wskazówka:** Z reguły procedurę `«puzzle4»` woła się następująco: `«i = puzzle4(a, v, 0, n - 1)»`.

```assembly
puzzle4:    movq %rcx, %rax             ;<<B0>>
            subq %rdx, %rax
            shrq %rax
            addq %rdx, %rax
            cmpq %rdx, %rcx
            jb .L5

            movq (%rdi,%rax,8), %r8     ;<<B1>>
            cmpq %rsi, %r8
            je .L10

            cmpq %rsi, %r8              ;<<B2>>
            jg .L11

            leaq 1(%rax), %rdx          ;<<B3>>
            call puzzle4

.L10:       ret                         ;<<B4>>

.L11:       leaq -1(%rax), %rcx         ;<<B5>>
            call puzzle4
            ret

.L5:        movl $-1, %eax              ;<<B6>>
            ret
```

```assembly
puzzle4:    movq %rcx, %rax         ;m = e           
            subq %rdx, %rax         ;m = e - s
            shrq %rax               ;m = (e - s) / 2
            addq %rdx, %rax         ;m = (e - s) / 2 + s
            cmpq %rdx, %rcx
            jb .L5                  ;e < s => jump L5

            movq (%rdi,%rax,8), %r8 ;mid = a[m]
            cmpq %rsi, %r8
            je .L10                 ;mid == v => jump L10

            cmpq %rsi, %r8
            jg .L11                 ;mid > v => jump L11

            leaq 1(%rax), %rdx
            call puzzle4            ;puzzle4(a, v, m + 1, e)

.L10:       ret                     ;return ^ / mid == v

.L11:       leaq -1(%rax), %rcx     
            call puzzle4            ;puzzle4(a, v, s, m - 1)
            ret                     ;return ^

.L5:        movl $-1, %eax
            ret                     ;return -1
```

```c
int puzzle4(long *a, long v, uint64_t s, uint64_t e) {
    if (e < s) return -1;

    uint64_t m = (e - s) / 2 + s;
    // (e + s) / 2 without overflowing

    long mid = a[m];
    if (mid == v) return m;
    if (mid < v) return puzzle4(a, v, m + 1, e);
    return puzzle4(a, v, s, m - 1);
}
```

Funkcja ta wykonuje przeszukiwanie binarne.

```graphviz
digraph {
    graph [bgcolor=transparent]
    node [fillcolor=black fontcolor=white]
    RB3 [label="puzzle4", style="dashed"]
    RB5 [label="puzzle4", style="dashed"]

    START -> B0;
    B0 -> B1, B6;
    B1 -> B2, B4;
    B2 -> B3, B5;
    B3 -> RB3;
    RB3 -> B4;
    B4 -> END;
    B5 -> RB5;
    RB5 -> END;
    B6 -> END;
}
```