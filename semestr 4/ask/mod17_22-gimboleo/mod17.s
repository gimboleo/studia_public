/*
 * UWAGA! W poniższym kodzie należy zawrzeć krótki opis metody rozwiązania
 *        zadania. Będzie on czytany przez sprawdzającego. Przed przystąpieniem
 *        do rozwiązywania zapoznaj się dokładnie z jego treścią. Poniżej należy
 *        wypełnić oświadczenie o samodzielnym wykonaniu zadania.
 *
 * Oświadczam, że zapoznałem(-am) się z regulaminem prowadzenia zajęć
 * i jestem świadomy(-a) konsekwencji niestosowania się do podanych tam zasad.
 *
 * Imię i nazwisko, numer indeksu: Jakub Kowalski, 323419
 */

        .text
        .globl  mod17
        .type   mod17, @function

/*
 * W moim rozwiązaniu używam następującej techniki:
 * Rozwiązanie w dużej mierze polega na impelementacji wskazówki z polecenia.
 *
 * W pierwszej części liczymy różnicę sum cyfr (szesnatkowych) na parzystych i nieparzystych pozycjach metodą dziel i zwyciężaj.
 * Robimy to upychając na początku liczby z nieparzystych i parzystych pozycji do różnych połów rejestru, a następnie dodając kubełki.
 * Po odjęciu od siebie dwóch finałowych kubełków otrzymujemy naszą róźnicę z przedziału <-120, 120>.
 *
 * Przedział ten jest za duży, żeby zwrócić rozwiązanie, musimy go zmniejszyć wywołując cały proces jeszcze raz.
 * Dla jednoznaczności obliczeń przesuniemy cały przedział o najmniejszą wielokrotność 17, która zmieni go w nieujemny.
 * Taką wielokrotnością jest 136, otrzymany przedział to <16, 256>_10 = <10, 100>_16.
 * Najprościej jest wykonać obliczenia dla przedziału <16, 255>_10 = <10, FF>_16 (liczby 2-cyfrowe szesnastkowo),
 * a następnie upewnić się przy pomocy tricków bitowych, że dla 0x100 zwracamy odpowiednią wartość (czyli 1).
 *
 * Wykonując obliczenia dla podproblemu uzyskamy liczbę z przedziału <-15, 15>. Po zmapowaniu liczb ujemnych na dodatnie
 * o tej samej wartości modulo 17 uzyskujemy przedział <0, 16>, czyli nasze rozwiązanie.
 *
 * W przypadku liczby 0x100 doprowadzamy do uzyskania liczby -0x100, którą jesteśmy w stanie zmapować na rozwiązanie równe 1.
 */

mod17:
        movq    %rdi, %rcx                      /* Upchanie cyfr o nieparzystych pozycjach na dolne 32 bity */       
        andq    .m1, %rcx                       /* 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 => 0 0 0 0 0 0 0 0 7+15 5+13 3+11 1+9 */
        movq    %rcx, %rax
        shrq    $32, %rax
        addl    %ecx, %eax
        movq    %rdi, %rdx                      /* Upchanie cyfr o parzystych pozycjach na górne 32 bity */
        shrq    $4, %rdx                        /* 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 => 8+16 6+14 4+12 2+10 0 0 0 0 0 0 0 0 */
        andq    .m1, %rdx
        movq    %rdx, %rsi
        shrq    $32, %rsi
        addl    %esi, %edx
        shlq    $32, %rdx 
        orq     %rdx, %rax                      /* 8+16 6+14 4+12 2+10 7+15 5+13 3+11 1+9 */

        movq    %rax, %rdx                      /* Dodanie wszystkich liczb tej samej parzystości do siebie */
        shrq    $8, %rdx
        addq    %rdx, %rax                      /* 6+14+8+16 2+10+4+12 5+13+7+15 1+9+3+11 */
        movq    %rax, %rdx
        shrq    $16, %rdx
        addq    %rdx, %rax                      /* 2+10+4+12+6+14+8+16 1+9+3+11+5+13+7+15 */
        movq    %rax, %rdx                      /* Maksymalna wartość sumy dla danej parzystości to 120, które mieści się na 8 bitach */
        shrq    $32, %rdx                       /* Dodatkowo w trakcie dodawania, powyżej 8 bita dla danej parzystości powstały śmieciowe dane, trzeba je uciąć */
        movzbl  %al, %eax                       /* 1+9+3+11+5+13+7+15 */
        movzbl  %dl, %edx                       /* 2+10+4+12+6+14+8+16 */

        subw    %dx, %ax                        /* Różnica parzystych i nieparzystych z przedziału <-120, 120>_10 */
        addw    $136, %ax                       /* Róźnica z biasem z przedziału <16, 256>_10 = <10, 100>_16 */
        movw    %ax, %dx                        /* Rozwiązanie podproblemu dla otrzymanej liczby 2-cyfrowej (lub 3-cyfrowej = 256_10 = 100_16) */
        shrb    $4, %dl                         /* 2 (dla 0x100 %dx = 0x100) */
        andw    $0xf, %ax                       /* 1 (dla 0x100 %ax = 0x0) */
        subw    %dx, %ax                        /* 1-2 z przedziału <-15, 15> mieszczące się na 8 bitach (dla 0x100 %ax = -0x100 = 1111111100000000_2 */

        shlb    $4, %dh                         /* 0 (16 dla 0x100) */
        andb    $17, %ah                        /* 0 jeśli wynik nieujemny, 17 wpp. (17 dla 0x100) */
        subb    %dh, %ah                        /* 0 jeśli wynik nieujemny, 17 wpp. (1 dla 0x100) */
        addb    %ah, %al                        /* wynik bez zmian jeśli nieujemny, +17 wpp. (0 + 1 = 1 dla 0x100 = 256) */
        movzbl  %al, %eax                       /* Wyłuskanie rozwiązania z rejestru */
        ret

        .size   mod17, .-mod17

        .data
        .m1: .quad 0x0f0f0f0f0f0f0f0f           /* 0000111100001111000011110000111100001111000011110000111100001111 */
