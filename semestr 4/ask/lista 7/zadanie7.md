> **Zadanie 7.** Poniżej widniej kod procedury o sygnaturze `«float puzzle7(struct P *, float)»`. Wyznacz definicję typu `«struct P»`. Przetłumacz tę procedurę na język C i wyjaśnij jednym zdaniem co robi.

# [Instrukcja xorps](https://www.felixcloutier.com/x86/xorps)
# [Instrukcja movss](https://www.felixcloutier.com/x86/movss)
# [Instrukcja vfmadd231ss](https://www.felixcloutier.com/x86/vfmadd132ss:vfmadd213ss:vfmadd231ss)
# [Instrukcja mulss](https://www.felixcloutier.com/x86/mulss)
# [Instrukcja movaps](https://www.felixcloutier.com/x86/movaps)
# [float.exposed](https://float.exposed/0x3f800000)
# [%rip-relative adressing](https://stackoverflow.com/questions/44967075/why-does-this-movss-instruction-use-rip-relative-addressing)

```assembly
puzzle7:    movq (%rdi), %rdx                           ;p.n
            leaq 8(%rdi), %rcx                          ;p.x
            xorl %eax, %eax                             ;i = 0
            vxorps %xmm1, %xmm1, %xmm1                  ;res = 0.0
            vmovss .LC1(%rip), %xmm2                    ;power = 1.0
.L2:        cmpq %rdx, %rax
            jge .L5                                     ;i >= n => jump L5
            vfmadd231ss (%rcx,%rax,4), %xmm2, %xmm1     ;res += P.x[i] * power
            incq %rax                                   ;i++
            vmulss %xmm0, %xmm2, %xmm2                  ;power *= f 
            jmp .L2
.L5:        vmovaps %xmm1, %xmm0
            ret                                         ;return res

.LC1:       .long 0x3f800000                            ;1.0
```

```c
struct P {
    long n;
    float *x;
};

float puzzle7(struct P *p, float f) {
    float res = 0.0;
    float power = 1.0;
    for (long i = 0; i < p->n; i++) {
        res += p->x[i] * power;
        power *= f;
    }
    return res;
}
```

Funkcja ta liczy sumę $\sum_{i=0}^n x_i \cdot f^i$, czyli wartość wielomianu zmiennej $f$ dla danej wartości.