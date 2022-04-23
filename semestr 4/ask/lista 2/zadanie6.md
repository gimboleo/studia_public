> **Zadanie 6.** Podaj wyrażenie zawierające wyłącznie zmienne `«x»` i `«y»`, którego wartością logiczną jest wynik porównania `«x < y»` dla liczb (a) bez znaku (b) ze znakiem.
>> **Wskazówka:** Spróbuj rozwiązać zadanie samodzielnie, a następnie przeczytaj §2.11 książki „Uczta programistów”.

`((x >> 1) - (y >> 1) - (~x & y & 1) >> N - 1) & 1`

- Liczby bez znaku: Po przesunięciu liczb o jedno miejsce w prawo, na ostatnim miejscu mają one $0$. Po ich odjęciu, jeśli `x` była mniejsza, na ostatnim miejscu otrzymamy $1$ poprzez pożyczkę. Musimy jednak jeszcze wziąć pod uwagę potencjalną pożyczkę z pierwszych, usuniętych przez nas bitów.
- Liczby ze znakiem: Postępujemy analogicznie :
  - Jeżeli liczby są tych samych znaków, 2 ostatnie bity (zduplikowany bit znaku) wyzerują się i sytuacja jest identyczna jak w liczbach bez znaku. 
  - Jeżeli `x` jest ujemne, a `y` dodatnie, odejmowanie $11xx...xx_2 - 00yy...yy_2$ zawsze pozostawi nam $1$ na ostatnim bicie.
  - Jeżeli `x` jest dodatnie, a `y` ujemne, odejmowanie $00xx...xx_2 - 11yy...yy_2$ zawsze pozostawi nam $0$ na ostatnim bicie.