> **Zadanie 1.** Zastąp instrukcję dzielenia całkowitoliczbowego zmiennej $n$ typu `int32_t` przez stałą $3$ przy pomocy operacji mnożenia liczb typu `int64_t`. Skorzystaj z faktu, że $\frac{x}{k} ≡ x · \frac{1}{k}$. Zapisz $\frac{1}{k}$ przy pomocy **liczby stałopozycyjnej** (ang. fixed point number). Przedstaw dowód poprawności swojego rozwiązania. Instrukcja dzielenia działa zgodnie z wzorem podanym na wykładzie, tj.:
$div3(n) = \left \{ \begin{array}{} 
\lfloor \frac{n}{3} \rfloor & dla & n \geq 0  \\ 
\lceil \frac{n}{3} \rceil & dla & n < 0
\end{array} \right.$
> Najpierw rozwiąż zadanie dla przypadku $n ≥ 0$, a potem uogólnij to na pełen przedział liczb.
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §10.3 książki „Uczta programistów”.

$\frac{1}{k} = \frac{1}{3} = 0.(01)_2$

Idea polega na pomnożeniu $n$ przez 'odwrotność' liczby $3$ (~$\frac{2^{32}}{3}$), a następnie przesunięciu wyniku tej operacji o $32$ bity w prawo aby uzyskać wynik dzielenia.

Dokładniej będziemy mnożyć przez 'magiczną' liczbę
$55555556_{16} = 0101 \space 0101 \space 0101 \space 0101 \space 0101 \space 0101 \space 0101 \space 0110_2 = \frac{2^{32} + 2}{3}$, która w rzeczywistości jest zaokrąglonym w górę wynikiem $\frac{2^{32}}{3}$ (zaokrąglenie w górę pozbędzie się błędu).

Do dowiedzenia poprawności takiej operacji przyda nam się kilka podstawowych własności sufitu i podłogi:
$$0 \leq x < \left| \frac{1}{d} \right| \rightarrow \left\lfloor \frac{n}{d} + x \right\rfloor = \left\lfloor \frac{n}{d} \right\rfloor$$
$$- \left| \frac{1}{d} \right| < x \leq 0 \rightarrow \left\lceil \frac{n}{d} + x \right\rceil = \left\lceil \frac{n}{d} \right\rceil$$
$$d > 0 \rightarrow \left\lfloor \frac{n}{d} \right\rfloor = \left\lceil \frac{n - d + 1}{d} \right\rceil$$

Rozważmy dwa przypadki:
- $n \geq 0$  
  $\left\lfloor \frac{2^{32} + 2}{3} \cdot \frac{n}{2^{32}} \right\rfloor = \left\lfloor \frac{n}{3} + \frac{2n}{3 \cdot 2^{32}} \right\rfloor =^1 \left\lfloor \frac{n}{3} \right\rfloor$  
  
  1.    $0 \leq n < 2^{31} \rightarrow 0 \leq 2n < 2^{32} \rightarrow 0 \leq \frac{2n}{3 \cdot 2^{32}} < \frac{1}{3}$

- $n < 0$  
  W tym przypadku do naszego wyniku będziemy musieli dodać $1$.  
  $\left\lfloor \frac{2^{32} + 2}{3} \cdot \frac{n}{2^{32}} \right\rfloor + 1 = \left\lfloor \frac{2^{32} + 2}{3} \cdot \frac{n}{2^{32}} + 1 \right\rfloor = \left\lfloor \frac{2^{32}n + 2n + 3 \cdot 2^{32}}{3 \cdot 2^{32}} \right\rfloor = \left\lceil \frac{2^{32}n + 2n + 1}{3 \cdot 2^{32}} \right\rceil = \left\lceil \frac{n}{3} + \frac{2n + 1}{3 \cdot 2^{32}} \right\rceil =^2 \left\lceil \frac{n}{3} \right\rceil$

  2.    $-2^{31} \leq n \leq -1 \rightarrow -2^{32} \leq 2n \leq -2 \rightarrow -\frac{1}{3} < \frac{2n + 1}{3 \cdot 2^{32}} \leq 0$

Zatem rozwiązanie wygląda następująco:
```c
int32_t div3(int32_t n) {
    const int64_t magic = 0x55555556;
    return (n * magic >> 32) + (n >> 31 & 1);
}
```