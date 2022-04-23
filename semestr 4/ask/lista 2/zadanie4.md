> **Zadanie 4.** Zmienne `«x»` i `«y»` o typie `«uint32_t»` przechowują czteroelementowe wektory typu `«uint8_t»`. Tj. wektor $\{x_3, x_2, x_1, x_0\}$ reprezentujemy w zmiennej `«x»` przypisując jej wartość $\sum\limits_{i = 0}^3 x_i \cdot 2^{8i}$. Jak szybko obliczyć zmienną `«z»` przechowującą wektor ${z_3, z_2, z_1, z_0}$, gdzie $z_i = x_i ⊕ y_i$, gdy:
> - ⊕ jest operacją dodawania,
> - ⊕ jest operacją odejmowania.
> 
> Obliczając wynik należy zapobiec wystąpieniu **przeniesienia** (ang. carry) lub **pożyczki** (ang. borrow) propagujących się do bardziej znaczącego bajtu.
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §2.17 książki „Uczta programistów”.

```c
uint32_t zadanie4_plus(uint32_t x, uint32_t y) {
    uint32_t s = (x & 0x7F7F7F7F) + (y & 0x7F7F7F7F);
    // 01111111 01111111 01111111 01111111 
    s ^= (x ^ y) & 0x80808080
    // 10000000 10000000 10000000 10000000
    return s;
}
```
Najpierw liczymy wszystkie bity w bajtach poza ostatnimi, żeby zapobiec nielegalnemu przeniesieniu, a potem 'ręcznie' wyliczamy wartości ostatnich bitów ignorując ich przeniesienie.

```c
uint32_t zadanie4_minus(uint32_t x, uint32_t y) {
    uint32_t s = (x | 0x80808080) - (y & 0x7F7F7F7F);    
    s ^= ~(x ^ y | 0x7F7F7F7F);
    return s;
}
```

Najpierw liczymy wszystkie bity w bajtach poza ostatnimi. Źeby zapobiec nielegalnej pożyczce, ostatni bit `x` ustawiamy na $1$, a `y` na $0$ (teraz bity, które liczymy zawsze mają 'z czego pożyczać'). Następnie 'ręcznie' wyliczamy wartości ostatnich bitów ignorując ich pożyczkę oraz biorąc pod uwagę, czy zawarta w nich $1$ została pożyczona.