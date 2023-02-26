> **Zadanie 7.** Blok pamięci podręcznej procesorów `x86-64` ma 64 bajty. Dla uproszczenia przyjmijmy, że w jednym cyklu zegarowym między pamięcią a procesorem można przesłać 64 bity danych. Ile nanosekund, w pesymistycznym przypadku, zajmie sprowadzenie bloku pamięci podręcznej z pamięci DRAM dla poniżej scharakteryzowanych modułów:
>
> - DDR4-1600, $t_{CLK} = 800 MHz, \ t_{CAS} = 10, \ t_{RCD} = 10, \ t_{RP} = 10, \ t_{RAS} = 25$
> - DDR4-2133, $t_{CLK} = 1066.67 MHz, \ t_{CAS} = 15, \ t_{RCD} = 15, \ t_{RP} = 15, \ t_{RAS} = 36$  
>
>Powtórz obliczenia zakładając, że pamięć działa w trybie sekwencyjnym (ang. *burst mode*), tj. podaje na kolejnych zboczach zegara szesnaście 64-bitowych słów bez czekania na polecenie zmiany kolumny.

Blok ma 64 bajty, w jednym cyklu możemy przesyłać 64 bity, zatem będziemy przesyłać 8 słów.

$c_1 = t_{RP} + max(t_{RCD} + 8(t_{CAS} + 1), t_{RAS}) = 108$  
$c_2 = t_{RP} + max(t_{RCD} + 8(t_{CAS} + 1), t_{RAS}) = 158$

$t_1 = \frac{c_1}{t_{CLK}} = \frac{108}{800 MHz} = 135 ns$  
$t_2 = \frac{c_2}{t_{CLK}} = \frac{158}{1066.67 MHz} = 148.52 ns$

$c_{b1} = t_{RP} + max(t_{RCD} + t_{CAS} + 4, t_{RAS}) = 39$  
$c_{b2} = t_{RP} + max(t_{RCD} + t_{CAS} + 4, t_{RAS}) = 55$

$t_{b1} = \frac{c_1}{t_{CLK}} = \frac{39}{800 MHz} = 48.75 ns$  
$t_{b2} = \frac{c_2}{t_{CLK}} = \frac{55}{1066.67 MHz} = 51.56 ns$