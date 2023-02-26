> **Zadanie 2.** Rozważmy napęd dyskietek 3½ o [następujących parametrach](https://jeffpar.github.io/kbarchive/kb/075/Q75131/): 300 obrotów na minutę, 512 bajtów na sektor, 18 sektorów na ścieżkę, 80 ścieżek na powierzchnię. Dysk sygnalizuje dostępność danych zgłaszając **przerwanie** na każdy przeczytany bajt, a wykonanie **procedury przerwania** zajmuje 16 µs¹. Następnie do systemu dodajemy **kontroler `DMA`**, więc przerwanie będzie generowane tylko raz po wczytaniu sektora do pamięci. Ile czasu zostanie procesorowi na pozostałe czynności w trakcie czytania $n$ sektorów $(a)$ bez użycia $(b)$ przy użyciu kontrolera `DMA`? Należy zignorować czas wyszukiwania ścieżki i sektora. W jaki sposób dodanie `DMA` do systemu poprawiło jego wydajność?
>> **¹**Około 128 cykli procesora w komputerze [IBM PC/AT](https://en.wikipedia.org/wiki/IBM_Personal_Computer/AT.) taktowanego zegarem 8 MHz
>
>> **Wskazówka:** Przerwania omówiono w [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), §8.1.2]. Przyjrzymy się im bliżej na przedmiocie *Systemy Operacyjne*.

[Przerwanie](https://pl.wikipedia.org/wiki/Przerwanie)

[Direct Memory Access](https://pl.wikipedia.org/wiki/Direct_Memory_Access)

$T_{avg \ transfer} = \frac{1}{300} \ \frac{1}{RPM} \cdot \frac{1}{18} \ \frac{track}{sectors} \cdot 60 \ \frac{s}{min} \approx 0.0111 \ s = 11.1 \ ms$  

$(a) \ \ \ T_{interrupt} = 512 \cdot 16 \cdot 10^{-3} \ ms = 8.192 \ ms$  
$T_{free} = n \cdot (T_{avg \ transfer} - T_{interrupt}) = n \cdot 2.908 \ ms$

$(b) \ \ \ T_{interrupt} = 16 \cdot 10^{-3} \ ms = 0.016 \ ms$  
$T_{free} = n \cdot (T_{avg \ transfer} - T_{interrupt}) = n \cdot 11.084 \ ms$

Dzięki `DMA` procesor zamiast obsługiwać wczytywanie sektora 512 razy (każdy bajt osobno), robi to tylko raz, co daje mu znacznie więcej czasu na wykonywanie innych instrukcji w trakcie operacji wczytywania danych z dysku.