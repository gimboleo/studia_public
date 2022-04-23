> **Zadanie 5 (2).** Poniżej widnieje kod funkcji o sygnaturze `«uint32_t puzzle3(uint32_t n, uint32_t d)»`. Wyznacz bloki podstawowe oraz narysuj graf przepływu sterowania, po czym przetłumacz tę funkcję na język C. Na podstawie ustępu *„Mixing C and Assembly Language”* strony [GNU Assembler Examples](https://cs.lmu.edu/~ray/notes/gasexamples/) napisz i **zaprezentuj** działanie programu, który pomógł Ci odpowiedzieć na pytanie co ta funkcja robi.

```assembly
puzzle3:    movl %edi, %edi             ;<<B0>>
            salq $32, %rsi
            movl $32, %edx
            movl $0x80000000, %ecx
            xorl %eax, %eax

.L3:        addq %rdi, %rdi             ;<<B1>>
            movq %rdi, %r8
            subq %rsi, %r8
            js .L2

            orl %ecx, %eax              ;<<B2>>
            movq %r8, %rdi

.L2:        shrl %ecx                   ;<<B3>>
            decl %edx
            jne .L3

            ret                         ;<<B4>>
```

```assembly
puzzle3:    movl %edi, %edi         ;m = 0:n
            salq $32, %rsi          ;s = d:0
            movl $32, %edx          ;i = 32
            movl $0x80000000, %ecx  ;mask = 10..0_2
            xorl %eax, %eax         ;res = 0

.L3:        addq %rdi, %rdi         ;m *= 2
            movq %rdi, %r8
            subq %rsi, %r8          ;temp = m - s
            js .L2                  ;temp < 0 => jump L2

            orl %ecx, %eax          ;res |= mask
            movq %r8, %rdi          m = temp

.L2:        shrl %ecx               ;mask >>= 1
            decl %edx               ;i--
            jne .L3                 ;i != 0 => jump L3

            ret
```

```c
uint32_t puzzle3(uint32_t n, uint32_t d)
{   
    uint32_t mask = 0x80000000;
    uint32_t res = 0;

    uint64_t m = n;
    uint64_t s = d;
    s <<= 32;

    for(int i = 32; i > 0; i--) {    
        m <<= 1;
        if (m >= s) {
            res |= mask;
            m -= s;
        }
        mask = mask >> 1;
    }

    return res;
}
```

Funkcja ta zwraca wartość $\lfloor \frac{n}{d} \rfloor$ obliczoną w sposób podobny do [dzielenia pisemnego](https://www.exploringbinary.com/binary-division/).

```graphviz
digraph {
    graph [bgcolor=transparent]
    node [fillcolor=black fontcolor=white]
    START -> B0;
    B0 -> B1;
    B1 -> B2, B3;
    B2 -> B3;
    B3 -> B1, B4;
    B4 -> END;
}
```