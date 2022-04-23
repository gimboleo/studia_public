> **Zadanie 3.** Napisz instrukcje w języku C, które dla zmiennych x i k wykonają poniższe obliczenia:

- Wyzeruj $k$-ty bit zmiennej $x$:
  ```c
  x &= ~(1<<k); 
  // wykonujemy AND x i liczby, która na każdym 
  // miejscu poza k-tym ma jedynkę
  ```

- Ustaw $k$-ty bit zmiennej $x$:
  ```c
  x |= 1<<k;
  // wykonujemy OR x i liczby, która na każdym
  // miejscu poza k-tym ma zero
  ```

- Zaneguj $k$-ty bit zmiennej $x$:
  ```c
  x ^= 1<<k;
  // wykonujemy XOR x i liczby, która na każdym
  // miejscu poza k-tym ma zero
  ```
  | A | B | A XOR B |
  |:-:|:-:|:-------:|
  | 0 | 0 |    0    |
  | 0 | 1 |    1    |
  | 1 | 0 |    1    |
  | 1 | 1 |    0    |