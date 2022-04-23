> **Zadanie 4.** Napisz wyrażenia w języku C, które dla zmiennych x i y wykonają poniższe obliczenia:

- $x * 2^y$:
  ```c
  a = x << y; // przesunięcie o y bitów w lewo
  ```
- $\lfloor x / 2^y \rfloor$:
  ```c
  b = x >> y; // przesunięcie o y bitów w prawo
  ```
- $x \space mod \space 2^y$:
  ```c
  c = x & ((1 << y) - 1);
  // wyzerowanie wszystkich bitów
  // poza y najmniej znaczącymi
  ```
- $\lceil x / 2^y \rceil$
  ```c
  d = 1 + ((x - 1) >> y);
  ```
  $\lceil \frac {n}{m} \rceil = \lfloor \frac {n+m-1}{m} \rfloor = \lfloor \frac {n-1}{m} \rfloor + 1$
  - [Wikipedia](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions#Quotients)
  - [Miro](https://miro.com/app/board/uXjVOIq4pz4=/)