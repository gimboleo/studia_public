> **Zadanie 4.** Poniżej zamieszczono kod procedury o sygnaturze `«long puzzle2(char *s, char *d)»`. Wyznacz bloki podstawowe oraz narysuj graf przepływu sterowania. Przetłumacz tę procedurę na język C, a następnie jednym zdaniem powiedz co ona robi.

```assembly
puzzle2:    movq %rdi, %rax   ;res = s         <<B0>>

.L3:        movb (%rax), %r9b ;s_chr = *res    <<B1>>
            leaq 1(%rax), %r8 ;s_ptr = res + 1
            movq %rsi, %rdx   ;d_ptr = d

.L2:        movb (%rdx), %cl  ;d_chr = *d_ptr  <<B2>>
            incq %rdx         ;d_ptr++
            testb %cl, %cl    ;ZF = !(d_chr & d_chr) ? 1 : 0
            je .L4            ;ZF => jump L4

            cmpb %cl, %r9b ;cmp(s_chr, d_chr)  <<B3>>
            jne .L2        ;s_chr != d_chr => jump L2

            movq %r8, %rax    ;res = s_ptr     <<B4>>
            jmp .L3           ;jump L3

.L4:        subq %rdi, %rax   ;res -= s        <<B5>>
            ret
```

```c
long puzzle2(char *s, char *d) {
    for (int i = 0; true; i++) {
        int j = 0;
        do {
            if (d[j] == '\0') return i;
        } while (s[i] != d[j++]);
    }
}
```

Funkcja ta zwraca długość najdłuższego prefiksu $s$. w którym każda litera występuje również w $d$.

```graphviz
digraph {
    graph [bgcolor=transparent]
    node [fillcolor=black fontcolor=white]
    START -> B0;
    B0 -> B1;
    B1 -> B2;
    B2 -> B3, B5;
    B3 -> B2, B4;
    B4 -> B1
    B5 -> END;
}
```