> **Zadanie 7.** Napisz wyrażenie w języku C, które oblicza się do 0 jeśli liczba x jest potęgą dwójki.

```c
x = ((x == 0) || (x & (x - 1)));
```

Liczbę 0 rozważamy jako oddzielny przypadek, zwracamy 1.

Dla niezerowej liczby:<Br>
Jeśli jest ona potęgą dwójki, jest postaci 10000...000.<br>
Liczba o jeden mniejsza jest postaci 1111...111 i jest o jeden bit 'krótsza'.<br>
Oznacza to, że te liczby nie mają bitów 'wspólnych' więc operator AND zwraca 0.