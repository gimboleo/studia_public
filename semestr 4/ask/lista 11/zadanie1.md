![Treść zadania](https://i.imgur.com/u8ZiHE0.png)

- $5$ bitów na offset $\rightarrow 2^5 = 32$ bajty w bloku $\rightarrow 32 \ bajty / 32 \ bity = 8$ słów / blok
- $E = 1$; $5$ bitów na index $\rightarrow 32$ zbiory po $1$ wierszu każdy, $32$ wiersze łącznie
- $meta = valid + dirty + tag = 1 + 1 + 22 = 24$ bity; $data = 32 \cdot 8 = 256$ bitów; $\frac{24}{256 + 24} = 0,08571428571428571$ 