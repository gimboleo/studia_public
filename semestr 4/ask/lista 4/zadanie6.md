> **Zadanie 6.** Zaimplementuj w asemblerze `x86-64` funkcję liczącą wyrażenie `«x + y»`. Argumenty i wynik funkcji są $128$-bitowymi liczbami całkowitymi **ze znakiem** i nie mieszczą się w rejestrach maszynowych. Zatem `«x»` jest przekazywany przez rejestry `%rdi` (starsze $64$ bity) i `%rsi` (młodsze $64$ bity), analogicznie argument `«y»` jest przekazywany przez `%rdx` i `%rcx`, a wynik jest zwracany w rejestrach `%rdx` i `%rax`.
>> **Wskazówka!** Użyj instrukcji `«adc»`. Rozwiązanie wzorcowe składa się z $3$ instrukcji bez `«ret»`.

# [Instrukcja adc](https://www.felixcloutier.com/x86/adc)

```assembly
add:    addq %rsi, %rcx
        adcq %rdi, %rdx
        movq %rcx, %rax
        ret
```

Jeśli nastąpi przeniesienie bitu przy wykonaniu instrukcji `addq`, ustawiona zostanie flaga `CF`, która zostanie uwzględniona przy dodawaniu w instrukcji `adcq`.

```
potencjalne przeniesienie
    ↓
    c
 BBBB BBBB
+BBBB BBBB
----------
xBBBB BBBB

    c
 %rdi %rsi
+%rdx %rcx
----------
x%rdx %rcx
```