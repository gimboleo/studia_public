> **Zadanie 7.** Zaimplementuj w asemblerze `x86-64` funkcję liczącą wyrażenie `«x * y»`. Argumenty i wynik funkcji są $128$-bitowymi liczbami całkowitymi **bez znaku**. Argumenty i wynik są przypisane do tych samych rejestrów co w poprzednim zadaniu. Instrukcja `«mul»` wykonuje co najwyżej mnożenie dwóch $64$-bitowych liczb i zwraca $128$-bitowy wynik. Wiedząc, że $n = n_{127...64} \cdot 2^{64} + n_{63...0}$, zaprezentuj metodę obliczenia iloczynu, a dopiero potem przetłumacz algorytm na asembler.
>> **UWAGA!** Zapoznaj się z dokumentacją instrukcji `«mul»` ze względu na niejawne użycie rejestrów `%rax` i `%rdx`.
>
>> `«x»` jest przekazywany przez rejestry `%rdi` (starsze $64$ bity) i `%rsi` (młodsze $64$ bity), analogicznie argument `«y»` jest przekazywany przez `%rdx` i `%rcx`, a wynik jest zwracany w rejestrach `%rdx` i `%rax`.

# [Instrukcja imul](https://www.felixcloutier.com/x86/imul)

$x = x_1 \cdot 2^{64} + x_0 \ \ \ \ \ y = y_1 \cdot 2^{64} + y_0$  

$x*y = (x_1 \cdot 2^{64} + x_0)\cdot (y_1 * 2^{64} + y_0) = x_1\cdot y_1\cdot 2^{128} + (x_1\cdot y_0 + x_0\cdot y_1)\cdot 2^{64} + x_0\cdot y_0 ≈_{128 \ bit \ chop} (x_1 \cdot y_0 + x_0 \cdot y_1) \cdot 2^{64} + x_0 \cdot y_0$

Musimy zatem wykonać 3 mnożenia i odpowiednio je zsumować. Zauważmy, że nie interesują nas starsze $64$ bity dwóch z tych mnożeń, bo przemnożenie ich wyników przez $2^{64}$ wyniesie je poza reprezentowalny zakres.

```assembly
mul:    imulq %rcx, %rdi  ;%rdi <- (x1y0)0
        imulq %rsi, %rdx  ;%rdx <- (x0y1)0
        addq %rdx, %rdi   ;%rdi <- (x1y0)0 + (x0y1)0
        movq %rsi, %rax   ;%rax <- x0
        mulq %rcx         ;%rax <- (x0y0)0, %rdx <- (x1y1)1 
        addq %rdi, %rdx   ;%rdx <- (x1y1)1 + (x1y0)0 + (x0y1)0
        ret
```