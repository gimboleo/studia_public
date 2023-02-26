> **Zadanie 5.** Przebieg operacji dostępu do **pamięci dynamicznej** przedstawiono zgrubnie w [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), §6.1.1]. Zapoznaj się z [[2](https://www.akkadia.org/drepper/cpumemory.pdf), §2] po czym odpowiedz na następujące pytania. Co musi się stać przed zleceniem **wyboru wiersza**? Wyjaśnij zasadę działania **wzmacniaczy odczytu** (ang. *sense amplifiers*). Czemu otwarty wiersz musi zostać wczytany do bufora przed zleceniem **wyboru kolumny**? Co musi się wydarzyć w trakcie zamykania wiersza? Czemu pamięć dynamiczna musi być **odświeżana** w przeciwieństwie do **pamięci statycznej**? W jaki sposób przeprowadzane jest odświeżanie całej pamięci?
>> **Wskazówka:** Więcej informacji na temat wewnętrznej organizacji pamięci dynamicznych można znaleźć w [[3](https://github.com/KevinOfNeu/ebooks/blob/master/Memory%20systems%20Cache%20DRAM%20Disk.pdf), §8].

- Przed zleceniem wyboru wiersza musi zostać wykonany *precharge*, który resetuje wzmacniacze odczytu i przygotowuje je do załadowania nowego wiersza.

- Kondensatory występujące w komórkach pamięci DRAM mają bardzo małą pojemność. Sygnał otrzymywany z komórki w momencie odczytu jest więc bardzo słaby i potrzebny jest wzmacniacz odczytu, który taką niewielką zmianę napięcia wykryje i zamieni ją na rozpoznawalny stan logiczny. Oprócz tego po odczycie wzmacniacz wpisuje z powrotem do odczytanej komórki wzmocnioną wartość, która 'wylewa się' w wyniku zczytania z niej informacji.

- Bufor pozwala na operowanie na wielu kolumnach z tego samego rzędu bez wczytywania nowych informacji z DRAM'u. Dodatkowo bufor jest pamięcią statyczną i wczytane do niego informacje są tam bezpieczne.

- W trakcie zamykania wiersza trzeba umieścić dane z bufora z powrotem w odpowiednim miejscu w pamięci DRAM.

- Pamięc dynamiczna musi być odświeżana, ponieważ z kondensatorów wraz z czasem ładunek wycieka i jest podatny na fluktuacje.

- Odświeżanie całej pamięci odbywa się wiersz po wierszu. Moduł DRAM utrzymuje licznik pamiętający adres ostatnio odświeżonego wiersza. Kontroler z ustaloną częstotliwością wydaje polecenie odświeżenia, które zwiększa licznik i odświeża wiersz.