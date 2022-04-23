> #### Dla poniższych zadań należy podać kompletny algorytm, zatem dozwolona jest cała składnia języka C bez ograniczeń z nagłówka listy zadań. Jednakże należy używać wyłącznie operacji na typie `«int32_t»` lub `«uint32_t»`.
> **Zadanie 9.** Uzupełnij ciało poniższej procedury konwertującej binarną reprezentację liczby typu `«float»` umieszczoną w zmiennej `«f»` do wartości typu `«int32_t»`. Wynik należy zaokrąglić w kierunku zera. Jeśli konwersja spowoduje nadmiar lub $f$ ma wartość `NaN`, zwróć wartość `0x80000000` (tj. `MIN_INT`). Kod procedury zaczyna się wyodrębnieniem poszczególnych elementów liczby zmiennopozycyjnej:
>```c
>int32_t float2int(int32_t f) {
>    int32_t s = f >> 31; 
>    /* -1 jeśli znak był ujemny */
>    int32_t e = (f >> 23 & 255) - 127;
>    /* wykładnik po odjęciu bias */
>    uint32_t m = f << 8 | 0x80000000;
>    /* mantysa 1.xxx... dosunięta do lewej */
>
>    /* TODO */
>}
>```
>> **Wskazówka:** Wzorcówka ma dodatkowe cztery linie kodu i używa jednej instrukcji warunkowej!

```c
int32_t float2int(int32_t f) {
    int32_t s = f >> 31; 
    /* -1 jeśli znak był ujemny */
    int32_t e = (f >> 23 & 255) - 127;
    /* wykładnik po odjęciu bias */
    uint32_t m = f << 8 | 0x80000000;
    /* mantysa 1.xxx... dosunięta do lewej */
    
    if (e <= 30 && e >= 0) {
        // Liczba miesci sie w zakresie int  
        m >>= (31 - e); // Pozbycie sie czesci ulamkowej
        return m * (1 | s); // Jesli ujemna, mnozenie przez -1
    }
    return MIN_INT ^ (MIN_INT & e);
    // e >= 30 -> MIN_INT; e < 0 -> 0

    // INT_MAX nie istnieje w float
    // Dla INT_MIN e = 31 -> return INT_MIN
    // Dla NaN e = 128 -> return INT_MIN
}
```