# NIEDEKLAROWANE

> **Zadanie 2.** Mamy dwa wektory $\overrightarrow{x}$ i $\overrightarrow{y}$ długości $n = 2^k$, których elementami są liczby w zakresu $[0, 1)$ zapisane w **reprezentacji stałopozycyjnej** `Q0.32`. Chcemy obliczyć wynik typu `Q0.32` poniższego wyrażenia:
> $$div3(\overrightarrow{x}, \overrightarrow{y}) = \frac{1}{n} \sum\limits_{i = 1}^n (x_i - y_i)^2$$
> Zauważ, że wyniki pośrednie muszą być być zapisane w reprezentacji `Q32.32`. Nie można osobno liczyć części całkowitej i ułamkowej. Można używać wszystkich konstrukcji języka C poza liczbami zmiennopozycyjnymi.