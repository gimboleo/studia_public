> **Zadanie 4.** W wyniku deasemblacji procedury `«long decode(long x, long y)»` otrzymano kod:
>> ```assembly
>> decode: leaq (%rdi,%rsi), %rax
>>         xorq %rax, %rdi
>>         xorq %rax, %rsi
>>         movq %rdi, %rax
>>         andq %rsi, %rax
>>         shrq $63, %rax
>>         ret
>> ```
> Zgodnie z [System V ABI3](https://software.intel.com/sites/default/files/article/402129/mpx-linux64-abi.pdf) dla architektury `x86-64`, argumenty `«x»` i `«y»` są przekazywane odpowiednio przez rejestry `%rdi` i `%rsi`, a wynik zwracany w rejestrze `%rax`. Napisz funkcję w języku C, która będzie liczyła dokładnie to samo co powyższy kod w asemblerze. Postaraj się, aby była ona jak najbardziej zwięzła.

```c
long decode_step_by_step(long x, long y) {
    long res = x + y;
    x ^= res;
    y ^= res;
    res = x;
    res &= y;
    res >>= 63;     // logical shift
    return res;
}
```

```c
// checking if x + y caused and overflow
long decode(long x, long y) {
    return (((x + y) ^ x) & ((x + y) ^ y) >> 63) & 1;
}
```