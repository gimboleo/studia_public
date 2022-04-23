>**Zadanie 1.** Czy poniższe wyrażenia zawsze obliczą się do prawdy dla dwóch dowolnych wartości zmiennych `«x»` i `«y»` typu `«int32_t»`? Jeśli nie to podaj wartości, które prowadzą do obliczenia fałszu.

- `(x > 0) || (x - 1 < 0)`  
$x = 100...00_2 = -2147483648$  
$x-1 = 100...00_2 - 1 = 0111...11_2 = 2147483647$   
`x > 0` $= 0$  
`(x - 1 < 0)` $= 0$  
`(x > 0) || (x - 1 < 0)` $= 0$

- `(x & 7) != 7 || (x << 29 < 0)` $= 1$  
`(x & 7) != 7` $= 0 \implies x = b_{31} b_{30} \dots b_3 111_2$   
$(x << 29) = 11100 \dots 000_2 < 0$  
`(x & 7) != 7` $= 0 \implies$ `(x << 29 < 0)` $= 1$  

- `(x * x) >= 0`  
$x=2^{16}+2^{14}$  
$x^2 = 2^{32}+2\cdot2^{30}+2^{28}=2^{32}+2^{31}+2^{28} = (1)100100...00_2 = 100100..00_2 < 0$  
`(x * x) >= 0` $= 0$

- `x < 0 || -x <= 0` $ = 1$  
(Każda liczba dodania ma swoją reprezentowalną liczbę przeciwną)

- `x > 0 || -x >= 0`  
$x = 100...00_2 = -2147483648$  
$-x = 011...11_2 + 1 = 100...00_2 < 0$  
`x > 0 || -x >= 0` $= 0$

- `(x | -x) >> 31 == -1`  
$x = 00...00_2 = 0$  
$-x = 11...11_2 + 1 = 00...00_2 = 0$  
`(x | -x)` $= 0$  
`(x | -x) >> 31` $= 0$  
`(x | -x) >> 31 == -1` $= 0$

- `x + y == (uint32_t)y + (uint32_t)x` $= 1$  
`(uint32_t)(x) + (uint32_t)(y) == (uint32_t)y + (uint32_t)x`   
(Operacje dodawnia i mnożenia nie zmieniają działania dla liczb unsigned/signed, zmienia się tylko interpretacja wyniku)

- `x * ~y + (uint32_t)y * (uint32_t)x == -x` $= 1$  
`(uint32_t)x * (uint32_t)(~y) + (uint32_t)y * (uint32_t)x == (uint32_t)(-x)`  
`(uint32_t)x * ((uint32_t)(~y) + (uint32_t)y) == (uint32_t)(-x)`  
`(uint32_t)x * UINT32_MAX == (uint32_t)(-x)`  
`(uint32_t)(~x) + 1 == (uint32_t)(-x)`  
`(uint32_t)(-x) == (uint32_t)(-x)`