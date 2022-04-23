> **Zadanie 1.** Poniższy wydruk otrzymano w wyniku deasemblacji rekurencyjnej procedury zadeklarowanej następująco: `«long pointless(long n, long *p)»`. Zapisz w języku C kod odpowiadający tej procedurze. Następnie opisz zawartość jej **rekordu aktywacji** *(ang. stack frame)*. Wskaż **rejestry zapisane przez funkcję wołaną** *(ang. callee-saved registers)*, zmienne lokalne i adres powrotu. Następnie uzasadnij, że wartość rejestru `%rsp` w wierszu $11$ jest podzielna przez $16$ – zgodnie z [[1](https://raw.githubusercontent.com/wiki/hjl-tools/x86-psABI/x86-64-psABI-1.0.pdf), 3.2.2]. Zastanów się czemu autorzy **ABI** zdecydowali się na taką konwencję.

```assembly
pointless:  pushq %r14              ;callee saving
            pushq %rbx              ;callee saving
            pushq %rax              ;caller saving
            movq %rsi, %r14         ;%r14 <- *p
            movq %rdi, %rbx         ;%rbx <-  n
            testq %rdi, %rdi
            jle .L1                 ;n <= 0 => jump L1
            leaq (%rbx,%rbx), %rdi  
            movq %rsp, %rsi
            callq pointless         ;pointless(2n, res)
            addq (%rsp), %rax       ;res += ^ 
            jmp .L3
.L1:        xorl %eax, %eax         ;res = 0
.L3:        addq %rax, %rbx         ;n += res
            movq %rbx, (%r14)       ;*p = n
            addq $8, %rsp           ;discarding saved %rax
            popq %rbx               ;callee restoring
            popq %r14               ;callee restoring
            retq
```

```c
long pointless(long n, long *p) {
    long res;

    if (n <= 0) res = 0;
    else res += pointless(2 * n, (long *) res);

    n += res;
    *p = n;

    return res;
}
```

|    Wartość    | Rozmiar |
|:-------------:|:-------:|
|    **%rbx**   |    8    |
|    **%r14**   |    8    |
|     *%rax*    |    8    |
| Adres powrotu |    8    |

Legenda:
- **rejestry zapisane przez funkcję wołaną**
- *zmienne lokalne*

Jeżeli wcześniej stos był wyrównany do 16 bajtów, to w momencie wywoływania funkcji rekursywnie nadal jest.

Taka konwencja alignmentu stosu została wprowadzona przez [SSE](https://pl.wikipedia.org/wiki/Streaming_SIMD_Extensions) - niektóre z tych instrukcji wymagają takiego alignmentu i stałe pilnowanie tego porządku jest mniej kosztowne. niż realignment tylko tam, gdzie jest on potrzebny.[$^1$](https://stackoverflow.com/a/49397524)