> **Zadanie 3.** Przeczytaj poniższy kod w języku C i odpowiadający mu kod w asemblerze, a następnie wywnioskuj jakie są wartości stałych `«R»`, `«S»` i `«T»`.
>> ```c
>> long A[R][S][T];
>> 
>> long store_elem(long i, long j, long k, long *dest) {
>>     *dest = A[i][j][k];
>>     return sizeof(A);
>> }
>> ```
>
>> ```assembly
>> store_elem: leaq (%rsi,%rsi,2),%rax
>>             leaq (%rsi,%rax,4),%rax
>>             movq %rdi,%rsi
>>             salq $6,%rsi
>>             addq %rsi,%rdi
>>             addq %rax,%rdi
>>             addq %rdi,%rdx
>>             movq A(,%rdx,8),%rax
>>             movq %rax,(%rcx)
>>             movq $3640,%rax
>>             ret
>> ```   

- `movq $3640,%rax` $\implies sizeof(A) = 3640 \implies R \cdot S \cdot T = 3640 / 8 = 455 = 5 \cdot 7 \cdot 13$
- `leaq (%rsi,%rsi,2),%rax`, `leaq (%rsi,%rax,4),%rax` $\equiv j \cdot 13$
- `movq %rdi,%rsi`, `salq $6,%rsi`, `addq %rsi,%rdi` $\equiv i \cdot 65$
- `addq %rax,%rdi`, `addq %rdi,%rdx`, `movq A(,%rdx,8),%rax` $\equiv *dest = A + 8(65i + 13j + k)$
- $(65i + 13j + k) = (iST + jT + k) \implies R = 7; S = 5; T = 13$