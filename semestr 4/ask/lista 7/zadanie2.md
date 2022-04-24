> **Zadanie 2.** Przeczytaj poniższy kod w języku C i odpowiadający mu kod w asemblerze, a następnie wywnioskuj jakie są wartości stałych `«A»` i `«B»`.
>> ```c
>> typedef struct {
>>     int x[A][B];
>>     long y;
>> } str1;
>> 
>> typedef struct {
>>     char array[B];
>>     int t;
>>     short s[A];
>>     long u;
>> } str2;
>> 
>> void set_val(str1 *p, str2 *q) {
>>     long v1 = q->t;
>>     long v2 = q->u;
>>     p->y = v1 + v2;
>> }
>> ```
>
>> ```assembly
>> set_val:    movslq 8(%rsi),%rax
>>             addq 32(%rsi),%rax
>>             movq %rax,184(%rdi)
>>             ret
>> ```

- `movslq 8(%rsi),%rax` $\implies 4 < B \leq 8$
- `addq 32(%rsi),%rax` $\implies 24 < 8 + 4 + 2A \leq 32 \equiv 6 < A \leq 10$
- `movq %rax,184(%rdi)` $\implies 176 < 4AB \leq 184 \equiv 44 < AB \leq 46$
- $AB = 45 \vee AB = 46$:
  - $AB = 46 = 23 \cdot 2$ - niemożliwe.
  - $AB = 45 = 3 \cdot 3 \cdot 5$ - spełnione dla $A = 9; B = 5$.