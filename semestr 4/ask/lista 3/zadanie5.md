> **Zadanie 5.** Mamy zmienne `«x»`, `«y»` i `«z»` typu `«int32_t»` ustawione na wybrane przez nas wartości Konwertujemy je do liczb typu `«double»` zapisanych w zmiennych `«dx»`, `«dy»` i `«dz»`. Rozważmy poniższe wyrażenia z języka C. Wskaż, które z nich mogą obliczyć się do fałszu. Podaj kontrprzykład – konkretne wartości naszych zmiennych całkowitoliczbowych.
>> **Wskazówka:** Zasady niejawnego rzutowania są wyjaśnione w §6.3.1.4, §6.3.1.5 i §6.3.1.8.

[Floating-Point Converter](https://babbage.cs.qc.cuny.edu/ieee-754.old/decimal.html)

- `(float)x == (float)dx` $= 1$  
Rzutowanie `int` na `double` nie powoduje utraty precyzji, rzutowanie na `float` w obu przypadkach da ten sam rezultat.

- `dx - dy == (double)(x - y)`  
$x = INT\_MIN = -2147483648; y = 1$  
$x - y = -2147483649 \rightarrow 2147483647 = INT\_MAX$  
$dx - dy = -2147483649 \rightarrow -1 \cdot 2^{31} \cdot (1 + \frac{1}{2^{31}})$  
`dx - dy == (double)(x - y)` $= 0$

- `(dx + dy) + dz == dx + (dy + dz)` $= 1$  
Rzutowanie `int` na `double` nie powoduje utraty precyzji. Dodatkowo `double` jest w stanie dokładnie przedstawić wszystkie liczby całkowite z przedziału $<-2^{53}, 2^{53}>$, więc w szczególności takżę sumę jakichkolwiek $3$ liczb $32$-bitowych. 

- `(dx * dy) * dz == dx * (dy * dz)`  
$x = 3; y = 2^{23} + 3; z = 2^{30} + 1$  
$dx \cdot dy = 50 \ 331 \ 666_{10} = 50 \ 331 \ 666_{double}$[*](https://www.binaryconvert.com/result_double.html?decimal=053048051051049054054054)  
$(dx \cdot dy) \cdot dz = 54 \ 043 \ 214 \ 906 \ 130 \ 450_{10} = 54 \ 043 \ 214 \ 906 \ 130 \ 448_{double}$[*](https://www.binaryconvert.com/result_double.html?decimal=053052048052051050049052057048054049051048052053048)  
$dy \cdot dz = 9 \ 007 \ 202 \ 484 \ 355 \ 075_{10} = 9 \ 007 \ 202 \ 484 \ 355 \ 076_{double}$[*](https://www.binaryconvert.com/result_double.html?decimal=057048048055050048050052056052051053053048055053)  
$dx \cdot (dy \cdot dz) = 54 \ 043 \ 214 \ 906 \ 130 \ 456_{10} = 54 \ 043 \ 214 \ 906 \ 130 \ 456_{double}$[*](https://www.binaryconvert.com/result_double.html?decimal=053052048052051050049052057048054049051048052053054)  
`(dx * dy) * dz == dx * (dy * dz)` $= 0$

- `dx / dx == dz / dz`  
$x = 0; z = 1$  
$dx / dx = NaN; dz / dz = 1$  
`dx / dx == dz / dz` $= 0$