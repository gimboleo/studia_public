> **Zadanie 3.** Zaimplementuj w języku C poniższy algorytm wygładzania wykładniczego *(ang. exponential smoothing)* szeregu $\{x_i\}$ wartości fizycznych (np. temperatury otoczenia) na 32-bitowym procesorze, który **nie implementuje** przetwarzania liczb zmiennopozycyjnych².
> $$s_0 = x_0 \\
> s_i = α \cdot x_i + (1 − α) \cdot s_{i − 1}, \ \ \ i > 0$$
> Wartości $x_i$ i $s_i$ są przechowywane jako **liczby stałoprzecinkowe** *(ang. fixed point)* w formacie `Q10.6` ze znakiem, tj. z dziesięcioma bitami na część całkowitą i sześcioma na część ułamkową. Dla dokładności stałą $α ∈ (0, 1)$ zapisano w formacie `Q16`. Podaj fragment kodu obliczający $α$ typu `uint16_t` z liczby typu `float` w trakcie kompilacji oraz $s_i$ typu `int16_t` w trakcie uruchomienia programu.
>> ²Dobrym przykładem są popularne mikrokontrolery `ARM Cortex-M4` na płytkach rozwojowych [Nucleo](https://www.st.com/en/evaluation-tools/stm32-nucleo-boards.html).

Zauważmy, że trzymanie liczby $x$ w formacie $Q_{m, n}$ w zmiennej typu `int` odpowiada trzymaniu liczby $x \cdot 2^n$, więc tak naprawdę nasze dane wejściowe są postaci $a \cdot 2^{16}$ oraz $x \cdot 2^6$. Mnożąc te liczby przez siebie otrzymamy $ax \cdot 2^{22}$, zatem żeby wynik był w formacie $Q_{10, 6}$ musimy wykonać dzielenie przez $2^{16}$. Wynik pośredni będziemy trzymać w `uint32_t`, w którym na pewno się zmieści.

```c
float f;
const uint16_t a = f * 0x10000; // a = f * 2^16 = f << 16
const uint16_t b = 0x10000 - a;

s[0] = x[0];
for (int i = 1; i < N; i++) {
    s[i] = ((uint32_t)a * x[i] + (uint32_t)b * s[i - 1]) >> 16;
}
```