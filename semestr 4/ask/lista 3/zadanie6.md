> **Zadanie 6.** Reprezentacje binarne liczb zmiennoprzecinkowych $f$ i $g$ typu `«float»` zostały załadowane odpowiednio do zmiennych `«x»` i `«y»` typu `«uint32_t»`. Podaj wyrażenie, które:
>> Pamiętaj, że dla liczb zmiennopozycyjnych w standardzie `IEEE 754` zachodzi $−0 ≡ +0$. Można pominąć rozważanie wartości `NaN`.
>
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §15.2 książki „Uczta programistów”.

- zmieni znak liczby `«f»`  
`x ^= 0x80000000` - przełączenie ostatniego bitu.

- obliczy wartość $\lfloor log2|f| \rfloor$ typu `«int»` dla $f$ w postaci znormalizowanej  
`((x >> 23) & 0x000000FF) - 127`  
Liczba $f$ jest postaci $(-1)^s \cdot 2^{exp - bias} \cdot M$, gdzie $M < 2$, zatem $floor(log_2(f)) = exp - bias + floor(log_2(M)) = exp - bias$.

- zwróci wartość logiczną operacji `«f == g»`  
`x == y | (x | y) == 0x8000000`  
Prawa część OR'a odpowiada za przypadek  $−0 ≡ +0$.

- zwróci wartość logiczną operacji `«f < g»`  
`(((x & ~y) >> 31) & ((x | y) & 0x7FFFFFFF != 0) |`  
$f \leq 0 \land g \geq 0 \land f \neq g \neq \pm 0$  
`((~(x & y) & (x - y)) >> 31) |`  
$f \geq 0 \land g \geq 0 \land f - g < 0$  
`((x & y & (y - x)) >> 31)) & 1`  
$f \leq 0 \land g \leq 0 \land g - f > 0$
