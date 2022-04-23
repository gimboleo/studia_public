> **Zadanie 10.** Jakie ograniczenia standardu ASCII przyczyniły się do powstania UTF-8? Wyjaśnij zasadę kodowania znaków do postaci binarnej UTF-8 i zapisz poniższy ciąg znaków w systemie szesnastkowym:
>>Proszę zapłacić 5€!

**[UTF-8](https://en.wikipedia.org/wiki/UTF-8)** (8-bit Unicode Transformation Format) – system kodowania, wykorzystujący od 1 do 4 bajtów do zakodowania pojedynczego znaku, w pełni kompatybilny z ASCII. Jest najczęściej wykorzystywany do przechowywania napisów w plikach i komunikacji sieciowej.

Tablica ASCII ma tylko 128 znaków - do wielu celów to jest zdecydowanie za mało, UTF-8 rozwiązuje ten problem.

Kodowanie binarne zależy od tego o jakim znaku mówimy. Dla odpowiednich przedziałów kodów korzystamy z tabeli:

![Layout sekwencji bajtów](https://i.imgur.com/kS5LBGy.png)

Tekst do zakodowania: *Proszę zapłacić 5€!*

50 72 6f 73 7a c4 99 20 7a 61 70 c5 82 61 63 69 c4 87 20 35 e2 82 ac 21

Dla przykładu popatrzmy na €:

- Kod dla € to U+20AC.
- Jest to przedział między U+0800 a U+FFFF, więc potrzebujemy 3 bajtów. 
- $20AC_{16} = 0010 \space 0000 10\space10 1100_2$. 
- Korzystamy z tabeli w taki sposób, że w miejsce każdego $x$ wstawiamy kolejne bity. 
- Dostajemy na koniec takie kodowanie: $1110 \space 0010 \space 1000 \space 0010 \space 1010 \space 1100$ 
- Konwertujemy do systemu szesnastkowego: $1110 \space 0010 \space 1000 \space 0010 \space 1010 \space 1100 = E2 \space 82 \space AC$