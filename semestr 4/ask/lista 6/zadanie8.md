> **Zadanie 8 (bonus).** Kompilator `GCC` umożliwia tworzenie funkcji zagnieżdżonych w języku C. Skompiluj poniższy kod z opcją `«-Os -fno-stack-protector»`, po czym zdeasembluj go poleceniem `«objdump»`. Zauważ, że procedura `«accumulate»` korzysta ze zmiennej `«res»` należącej do rekordu aktywacji procedury `«sum»`. Zatem w miejscu wywołania `«accumulate»` (wiersz $3$) musimy dysponować wskaźnikiem na tą procedurę i jej środowisko. Wyjaśnij w jaki sposób kompilator przygotował procedurę `«accumulate»` do wołania w `«for_range_do»` oraz w jaki sposób `«accumulate»` otrzymuje dostęp do zmiennych ze środowiska `«sum»`. Przy pomocy debuggera `GDB` i nakładki [gdb-dashboard4](https://github.com/cyrus-and/gdb-dashboard) zaprezentuj, instrukcja po instrukcji (polecenie `«si»`), co się dzieje w trakcie wywołania funkcji w wierszu $3$.
>> **Uwaga!** Użycie tej konstrukcji wymaga, by stos był wykonywalny, co może ułatwić hakerom przejęcie kontroli nad programem.
> ```c
> __attribute__((noinline))
> void for_range_do(long *cur, long *end, void (*fn)(long x)) {
>     while(cur < end)
>         fn(*cur++);
> }
> 
> long sum(long *a, long n) {
>     long res = 0;
>     
>     void accumulate(long x) {
>         res += x;
>     }
> 
>     for_range_do(a, a + n, accumulate);
>     return res;
> }
> ```

# [Instrukcja endbr64](https://exchangetuts.com/what-does-the-endbr64-instruction-actually-do-1639565284885908)
# [Trampoline](https://en.wikipedia.org/wiki/Trampoline_(computing)#High-level_programming)

|   Wartość   | Adres | Dodatkowe informacje |
|:-----------:|:-----:|:--------------------:|
|    $0x90    |   35  |          nop         |
|     0xe3    |   34  |   <rex.WB jmp r11>   |
|     0xff    |   33  |   <rex.WB jmp r11>   |
|    $0x49    |   32  |   <rex.WB jmp r11>   |
|     %rsp    | 24-31 |  Argument dla movabs |
|    $0xba    |   23  |   <movabs %r10, ??>  |
|    $0x49    |   22  |   <movabs %r10, ??>  |
| *accumulate | 14-21 |  Argument dla movabs |
|    $0xbb    |   13  |   <movabs %r11, ??>  |
|    $0x49    |   12  |   <movabs %r11, ??>  |
|    $0xfa    |   11  |      \<endbr64>      |
|    $0x1e    |   10  |      \<endbr64>      |
|    $0x0f    |   9   |      \<endbr64>      |
|    $0xf3    |   8   |      \<endbr64>      |
|     res     |  0-7  |         %rsp         |

Deasemblacja dokonana za pomocą poniższych poleceń:
```bash
gcc -c -Og -fno-stack-protector zadanie8.c
objdump zadanie8.o -d > zadanie8.txt

gcc -Og -g -fno-stack-protector zadanie8.1.c
objdump a.out -d -S > a.txt

gdb a.out
> b sum
> run
> si
> x/6i $rsp+0x6
> x/6x $rsp
```