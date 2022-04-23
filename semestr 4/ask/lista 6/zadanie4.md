> **Zadanie 4.** Poniżej widnieje kod wzajemnie rekurencyjnych procedur `«M»` i `«F»` typu `«long (*)(long)»`. Programista, który je napisał, nie pamiętał wszystkich zasad **konwencji wołania procedur**. Wskaż co najmniej dwa różne problemy w poniższym kodzie i napraw je! Następnie przetłumacz kod do języka C.

```assembly
M:      pushq %rdi
        testq %rdi, %rdi
        je .L2                  ;!n => jump L2
        leaq -1(%rdi), %rdi
        call M                  ;M(n - 1)
        movq %rax, %rdi
        call F                  ;F(M(n - 1))
        movq (%rsp), %rdi
        subq %rax, %rdi         ;n -= F(M(n - 1))
.L2:    movq %rdi, %rax         ;res = n
+       addq $8, %rsp
        ret

F:      testq %rdi, %rdi
        je .L3                  ;!n => jump L3
+       pushq %r12
        movq %rdi, %r12
        leaq -1(%rdi), %rdi
        call F                  ;F(n - 1)
        movq %rax, %rdi
        call M                  ;M(F(n - 1))
        subq %rax, %r12         ;n -= M(F(n - 1))
        movq %r12, %rax         ;res = n
+       popq %r12
        ret
.L3:    movl $1, %eax 
        ret                     ;return 1
```

W kodzie były następujące błędy:
- %rdi nie zdjęte ze stosu przed wyjściem z funkcji $M$.
- nadpisanie *callee-saved* rejestru %r12 w funkcji $F$.
- nieodpowiednio wyrównany w wywołaniach funkcji w $F$.

```c
long M(long n) {
    if (!n) return 0;
    return n - F(M(n - 1));
}

long F(long n) {
    if (!n) return 1;
    return n - M(F(n - 1));
}
```

[Hofstadter Female and Male sequences](https://en.wikipedia.org/wiki/Hofstadter_sequence#Hofstadter_Female_and_Male_sequences)