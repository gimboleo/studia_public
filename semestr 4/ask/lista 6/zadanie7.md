> **Zadanie 7 (2).** Procedurę ze zmienną liczbą parametrów używającą pliku nagłówkowego [stdarg.h3](https://en.wikipedia.org/wiki/Stdarg.h) skompilowano z opcjami `«-Og -mno-sse»`. Po jej deasemblacji otrzymano następujący wydruk. Przetłumacz procedurę `«puzzle7»` na język C i wytłumacz jednym zdaniem co ona robi. Narysuj rekord aktywacji procedury, a następnie podaj jego rozmiar i składowe. Prezentację zacznij od przedstawienia definicji struktury `«va_list»` na podstawie [[1](https://raw.githubusercontent.com/wiki/hjl-tools/x86-psABI/x86-64-psABI-1.0.pdf), 3.5.7].

# [flaga -mno-sse](https://stackoverflow.com/a/3691352)
# [va-list](https://en.cppreference.com/w/c/variadic/va_list)

```c
typedef struct {
    // offset od *reg_save_area do następnego argumentu (general purpose)
    unsigned int gp_offset;
    // jak wyżej, ale dla liczb floating point
    unsigned int fp_offset;
    // wskazuje miejsce na stosie, gdzie zachowane będą argumenty nadmiarowe (ze stosu)
    void *overflow_arg_area;
    // wskazuje miejsce na stosie, gdzie zachowane będą argumenty z rejestrów
    void *reg_save_area;
} va_list[1];
```

```assembly
puzzle7:    movq %rsi, -40(%rsp)    ;inicjalizacja va_list
            movq %rdx, -32(%rsp)
            movq %rcx, -24(%rsp)
            movq %r8, -16(%rsp)
            movq %r9, -8(%rsp)
            movl $8, -72(%rsp)
            leaq 8(%rsp), %rax
            movq %rax, -64(%rsp)
            leaq -48(%rsp), %rax
            movq %rax, -56(%rsp)    ;koniec inicjalizacji
            movl $0, %eax           ;res = 0
            jmp .L2
.L3:        movq -64(%rsp), %rdx    ;obsługa argumentów pochodzących ze stosu funkcji wołającej
            leaq 8(%rdx), %rcx      ;^ %rdx <= adres następnego argumentu
            movq %rcx, -64(%rsp)    ;*overflow_arg_area += 8
.L4:        addq (%rdx), %rax       ;res += arg
.L2:        subq $1, %rdi           ;n--;
            js .L6                  ;n < 0 => return res
            cmpl $47, -72(%rsp)
            ja .L3
            movl -72(%rsp), %edx    ;można czytać argumenty pochodzące z rejestrów
            addq -56(%rsp), %rdx    ;%rdx <= adres następnego argumentu
            addl $8, -72(%rsp)      ;gp_offest += 8
            jmp .L4
.L6:        ret
```

|    Wartość    | Adres | Dodatkowe informacje |
|:-------------:|:-----:|:--------------------:|
|      ...      |  ...  |          ...         |
|     arg_7?    |   8   |   overflow_arg_area  |
| Adres powrotu |   0   |         %rsp         |
|      %r9      |   -8  |     reg_save_area    |
|      %r8      |  -16  |     reg_save_area    |
|      %rcx     |  -24  |     reg_save_area    |
|      %rdx     |  -32  |     reg_save_area    |
|      %rsi     |  -40  |     reg_save_area    |
|               |  -48  |     reg_save_area    |
|   %rsp - 48   |  -56  |    *reg_save_area    |
|    %rsp + 8   |  -64  |  *overflow_arg_area  |
|       8       |  -72  |       gp_offset      |

```c
#include <stdarg.h>


long puzzle7(long n, ...) {
    va_list args;
    va_start(args, n);

    long res = 0;

    for(; n >= 0; --n) res += va_arg(args, long);

    va_end(args);
    return res;
}
```

Procedura ta sumuje $n$ argumentów.