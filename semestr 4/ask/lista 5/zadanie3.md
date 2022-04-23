> **Zadanie 3.** Zapisz w języku C funkcję o sygnaturze `«int puzzle(long x, unsigned n)»` której kod w asemblerze podano niżej. Zakładamy, że parametr `«n»` jest niewiększy niż $64$. Przedstaw jednym zdaniem co robi ta procedura.
>> **Uwaga!** Instrukcja zapisująca młodszą połowę $64$-bitowego rejestru ustawia na $0$ jego starszą połowę (brzydota `x86-64`).

```assembly
puzzle: testl %esi, %esi   // ZF = !(n & n) ? 1 : 0
        je .L4             // ZF => jump L4
        xorl %edx, %edx    // i = 0
        xorl %eax, %eax    // res = 0
.L3:    movl %edi, %ecx    // tmp = x
        andl $1, %ecx      // tmp &= 1
        addl %ecx, %eax    // res += tmp
        sarq %rdi          // x >>= 1
        incl %edx          // i += 1
        cmpl %edx, %esi    // cmp(n, i)
        jne .L3            // n != i -> jump L3
        ret                
.L4:    movl %esi, %eax    // res = n
        ret                
```

```c
int puzzle(long x, unsigned n) {
    // if (!n) return n;

    int res = 0;

    for (unsigned i = 0; i < n; i++) {
        res += x & 1;
        x >>= 1;
    }

    return res;
}
```

Funkcja ta zlicza ilość jedynek w $n$ najmłodszych bitach liczby $x$.