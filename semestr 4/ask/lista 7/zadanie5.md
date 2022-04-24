> **Zadanie 5.** Przeczytaj definicję unii `«elem»` i wyznacz jej rozmiar w bajtach. Następnie przepisz procedurę `«proc»` na kod w języku C.

```c
union elem {
    struct {
        long *p;                // 8 bajtów
        long y;                 // 8 bajtów
    } e1;                   // 16 bajtów
    struct {
        long x;                 // 8 bajtów
        union elem *next;       // 8 bajtów
    } e2;                   // 16 bajtów
                          // = 16 bajtów
};
```

```assembly
proc:   movq 8(%rdi),%rax   ;*tmp = e->e2.next
        movq (%rax),%rdx    ;*tmp2 = tmp->e1.p
        movq (%rdx),%rdx    ;tmp3 = *tmp2
        subq 8(%rax),%rdx   ;tmp3 -= tmp->e1.y
        movq %rdx,(%rdi)    ;e->e2.x = tmp3
        ret
```

```c
void proc(union elem *e) {
    union elem *tmp = e->e2.next;
    e->e2.x = *(tmp->e1.p) - tmp->e1.y;
}
```