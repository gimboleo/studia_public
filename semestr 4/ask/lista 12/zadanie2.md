> **Zadanie 2.** Ile razy zostanie zawołana funkcja `«my_strlen»` w funkcji `«my_index»` i dlaczego? Dodaj [atrybut](https://gcc.gnu.org/onlinedocs/gcc/Common-Function-Attributes.html) `«pure»` do funkcji `«my_strlen»`. Czemu tym razem kompilator był w stanie lepiej zoptymalizować funkcję `«my_index»`? Czym charakteryzują się **czyste funkcje**? Następnie uzupełnij ciało funkcji `«my_strlen»` tak, by wykonywała to samo co `«strlen»`. Następnie usuń atrybut `«pure»` i dodając słowo kluczowe `«static»` zawęź zakres widoczności funkcji do bieżącej jednostki translacji. Co się stało w wyniku przeprowadzenia **inliningu**? Czy kompilatorowi udało się samemu wywnioskować, że funkcja jest czysta?
>> ```c
>> __attribute__((leaf))
>>     size_t my_strlen(const char *s);
>>
>> const char *my_index(const char *s, char v) {
>>     for (size_t i = 0; i < my_strlen(s); i++)
>>         if (s[i] == v)
>>             return &s[i];
>>     return 0;
>> }
>> ```
>> [Godbolt](https://godbolt.org/z/5ns7caeMn)

Funkcja `«my_index»` zostanie wywołana $O(n)$ razy, gdzie $n$ to długość słowa $s$ (za każdym sprawdzeniem warunku). Kompilator nie może tego zoptymalizować, ponieważ nie wie, czy funkcja nie wprowadza zmian w wskaźniku `s` - potencjalnie jej wynik może się zmieniać między wywołaniami.

```c
__attribute__((leaf, pure))
    size_t my_strlen(const char *s);

const char *my_index(const char *s, char v) {
    for (size_t i = 0; i < my_strlen(s); i++)
        if (s[i] == v)
            return &s[i];
    return 0;
}
```
[Godbolt](https://godbolt.org/z/hqbY8jsnW)

Dodanie `«pure»` spowoduje, że po optymalizacji funkcja zostanie wywołana tylko raz. Atrybut ten sygnalizuje kompilatorowi, że procedura ta jest funkcją czystą - nie powoduje efektów ubocznych (nie modyfikuje stanu programu poza zwróceniem odpowiedniej wartości) oraz jej wynik jest determenistyczny względem podanych jej argumentów oraz zmiennych globalnych. Dzięki tej informacji kompilator wie, że funkcje można bezpiecznie wywołać tylko raz.

```c
static size_t my_strlen(const char *s) {
    size_t i = 0;
    while (*s++)
        i++;
    return i;
}

const char *my_index(const char *s, char v) {
    for (size_t i = 0; i < my_strlen(s); i++)
        if (s[i] == v)
            return &s[i];
    return 0;
}
```
[Godbolt](https://godbolt.org/z/q8EYzrEhb)

W wyniku dodania słowa kluczowego `«static»` doszło do zinlinowania funkcji `«my_strlen»` (która co ciekawe została zoptymalizowana do wywołania funkcji `«strlen»`; dodatkowo kompilator zorientował się, że funkcja ta jest czysta i wywołał ją tylko raz).