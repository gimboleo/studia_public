> **Zadanie 8.** Program czyta sekwencyjnie jednowymiarową tablicę o rozmiarze 4GiB położoną pod adresem podzielnym przez $2^{20}$. W komputerze zainstalowano dwa moduły pamięci DDR4-2133 o parametrach: $t_{CAS} = 15, \ t_{RCD} = 15, \ t_{RP} = 15, \ t_{RAS} = 36$, maksymalny rozmiar transferu sekwencyjnego to 16 słów, długość wiersza (ang. *DRAM page size*) wynosi 8KiB. Ile czasu zajmie sprowadzenie danych do procesora? Należy pominąć rozważanie opóźnień wynikających z działania pamięci podręcznej i kontrolera pamięci. 
>
> Powtórz obliczenia dla systemu dysponującego pamięcią w konfiguracji dwukanałowej (ang. *dual-channel*).

Liczba wierszy w tablicy: $\frac{4GiB}{8KiB} = \frac{4 * 2^{30}}{8 * 2^{10}} = 2^{19}$

W jednej 'iteracji' odczytu sekwencyjnego możemy przeczytać $16$ słów, każde po $8$ bajtów $\rightarrow$ $128$ bajtów na 'iterację'.

Jeden wiersz ma $8 KiB$, czyli $8192$ bajtów.
Do przeczytania jednego wiersza potrzebujemy zatem $64$ 'iteracji'.

Jedna z nich trwa $t_{CAS} + 16 = 31$ cykli.

Przeczytanie wiersza potrwa więc $t_{RCD} + 64 \cdot 31 + t_{RP} = 2014$ cykli.

Przeczytanie wszystkich wierszy to $\frac{2^{19} \cdot 2014}{1066.67 MHz} \approx 0.99 s$

---

Konfiguracja dwukanałowa pozwala nam czytać jednocześnie $32$ słowa:

Mamy $32$ iteracje po $t_{CAS} + 32 = 47$ cykli.

Przeczytanie wiersza potrwa $t_{RCD} + 32 \cdot 47 + t_{RP} = 1534$ cykli.

Przeczytanie wszystkich wierszy to $\frac{2^{19} \cdot 1534}{1066.67 MHz} \approx 0.75 s$