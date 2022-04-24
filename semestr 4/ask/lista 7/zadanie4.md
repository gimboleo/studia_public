> **Zadanie 4.** Przeczytaj poniższy kod w języku C i odpowiadający mu kod w asemblerze, a następnie wywnioskuj jaka jest wartość stałej `«CNT»` i jak wygląda definicja struktury `«a_struct»`.
>> ```c
>> typedef struct {
>>     int first;
>>     a_struct a[CNT];
>>     int last;
>> } b_struct;
>>
>> void test (long i, b_struct *bp) {
>>     int n = bp->first + bp->last;
>>     a_struct *ap = &bp->a[i];
>>     ap->x[ap->idx] = n;
>> }
>
>> ```assembly
>> test:   movl 0x120(%rsi),%ecx
>>         addl (%rsi),%ecx
>>         leaq (%rdi,%rdi,4),%rax
>>         leaq (%rsi,%rax,8), %rax
>>         movq 0x8(%rax),%rdx
>>         movslq %ecx,%rcx
>>         movq %rcx,0x10(%rax,%rdx,8)
>>         retq
>> ```

- `movl 0x120(%rsi),%ecx` $\equiv$ `offsetof(struct b_struct, last)` $= 288$
- `leaq (%rdi,%rdi,4),%rax`, `leaq (%rsi,%rax,8), %rax`, `movq 0x8(%rax),%rdx` $\equiv *ap = *(bp + 40i + 8) \implies$ `sizeof(a_struct)` $= 40$
- $\frac{288 - 4}{40} = 7 + \frac{4}{40} \implies CNT = 7; \ total\_offset = 4$
- Offset znajduje się między `first` i `a`, ponieważ na innych pozycjach jest on zbędny $\implies$ `alignof(a_struct)` $= 8$
- `movslq %ecx,%rcx` $\implies$ `ap->x` to tablica liczb `long`
- `movq %rcx,0x10(%rax,%rdx,8)` $\equiv *(bp + 40i + 8(*ap) + 16) = *(ap + 8(ap \rightarrow idx) + 8) = n \implies$ Pierwszym elementem struktury `a_struct` jest `long idx`
- `sizeof(x)` $= 40 - 8 = 32$
- $\frac{32}{8} = 4 \implies$ `x` to tablica $4$-elementowa

```c
typedef struct {
    long idx;
    long x[4];
} a struct;
```