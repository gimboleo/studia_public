> **Zadanie 7.** Podaj fragment kodu, który oblicza funkcję:
$abs(x) = \left \{ \begin{array}{} 
x & dla & x \geq 0  \\ 
-x & dla & x < 0 
\end{array} \right.$
Skorzystaj z następującej własności: jeśli `«b»` jest wartością logiczną, to wyrażenie `«b ? x : y»` można
przetłumaczyć do `«b * x + !b * y»`.
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §2.4 książki „Uczta programistów”.

> Wersja korzystająca z własności z polecenia:
>> ```c
>> int abs(int x) {
>>     // x < 0 ? -x : x
>>     // (x < 0) * -x + (x >= 0) * x
>>
>>     // Dla nieujemnych 0 & -x | -1 & x == 0 | x == x
>>     // Dla ujemnych x: -1 & -x | 0 & x == -x | 0 == -x
>>     return x >> N - 1 & -x | ~(x >> N - 1) & x;
>> }
>> ```

> Wersja 'lepsza':
>> ```c
>> int abs(int x) {
>>     // Dla nieujemnych x: x ^ 0 - 0 == x
>>     // Dla ujemnych x: ~x - (-1) == ~x + 1 == -x
>>     int mask = x >> N - 1;
>>     return (x ^ mask) - mask;
>> }
>> ```