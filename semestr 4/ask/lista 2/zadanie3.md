> **Zadanie 3.** Napisz wyrażenie zawierające wyłącznie zmienne `«x»`, `«y»` i `«s»`, którego wartością logiczną jest odpowiedź na pytanie czy wykonanie instrukcji `«s = x + y»` spowodowało **nadmiar** (ang. overflow) lub **niedomiar** (ang. underflow).
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §2.12 książki „Uczta programistów”.

`((s ^ x) & (s ^ y) >> N - 1) & 1`

- Dla `x` i `y` przeciwnych znaków nie dojdzie do wyjścia poza zakres - koniunkcja obliczy się do liczby z $0$ na ostatniej pozycji, więc po przesunięciu otrzymamy $0$.
- Dla `x` i `y` tych samych znaków wyrażenie będzie prawdziwe, jeżeli `s = x + y` jest przeciwnego od nich znaku. Wtedy koniunkcja obliczy się do liczby z $1$ na ostatniej pozycji, którą przesuniemy na początek. W przeciwnym przypadku otrzymamy $0$.

Całość musimy jeszcze zand'ować z $1$, ponieważ korzystamy z przesunięcia **arytmetycznego** w prawo.