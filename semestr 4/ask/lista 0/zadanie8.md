> **Zadanie 8.** Napisz ciąg instrukcji w języku C, który skonwertuje zmienną x z formatu little-endian do formatu big-endian. Należy użyć jak najmniejszej liczby operacji bitowych.

![Little/Big Endian](https://i.imgur.com/B899rY2.png)

```c
unsigned long x;

unsigned long x1, x2, x3, x4;

x1 = (x & 0x000000ff) << 24;
x2 = (x & 0x0000ff00) << 8;
x3 = (x & 0x00ff0000) >> 8;
x4 = (x & 0xff000000) >> 24;

x = x1 | x2 | x3 | x4;
```