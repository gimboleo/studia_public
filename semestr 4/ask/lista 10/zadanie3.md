> **Zadanie 3.** 32-bitowa **magistrala** ma **przepustowość** (ang. *throughput*) 10 milionów transferów na sekundę. Do magistrali podpięty jest prosty procesor `RISC` bez pamięci podręcznej, kontroler dysku twardego z `DMA` i pamięć operacyjna. Wszystkie instrukcje są 32-bitowe, a ich wykonanie zajmuje **dwa cykle magistrali**. W pierwszym cyklu następuje pobranie instrukcji z pamięci i jej zdekodowanie, a w drugim jej wykonanie. Dla instrukcji wykonujących dostęp do pamięci w drugim cyklu nastąpi odwołanie do pamięci. Dla pozostałych instrukcji w drugim cyklu procesor nie odwołuje się do magistrali.
>
> Moduł `DMA` kontrolera dysku do transferu danych używa techniki **podkradania cykli** (ang. [*cycle stealing*](https://en.wikipedia.org/wiki/Cycle_stealing)). Procesor wykonuje ciąg instrukcji, z których 40% robi dostęp do danych w pamięci. Moduł `DMA` może transferować dane z dysku z prędkością 5 MB/s. Ile instrukcji przetworzy w ciągu sekundy procesor, gdy transfer danych z dysku jest $(a)$ nieaktywny $(b)$ aktywny.
>> **Zastanów się:** Co złego mogłoby się stać, gdyby kontroler dysku dostawał wyłącznie cykle magistrali nieużywane przez procesor?

$(a)$ Wykonanie instrukcji trwa $2$ cykle, a przepustowość wynosi $10^7 \ t/s$, zatem procesor w jedną sekundę wykona $10^7 / 2 = 5 \cdot 10^6$ instrukcji.

$(b)$ $32 / 8 \cdot 10^6 = 40 \ MB/s; \ 5 \ MB/s \ / \ 40 \ MB/s = 0.125; \ 0.125 \cdot 2 = 0.25; \ 0.25 \cdot 0.4 = 0.1; \  5 \cdot 10^6 \cdot (1 - 0.1) = 4950000$

Co by się stało gdyby kontroler DMA dostawał tylko cykle na magistrali nieużywane przez procesor? Mogłoby dojść do sytuacji w której kontroler DMA w ogóle nie jest w stanie wykonać swojej pracy. Jeszcze gorzej jeśli procesor czeka na koniec transferu w sposób wykorzystujący polling pamięci - nastąpiłoby wtedy zakleszczenie - procesor czeka na kontroler DMA, a kontroler DMA czeka na wolny cykl na magistrali.