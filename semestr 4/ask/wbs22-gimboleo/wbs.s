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
        .globl  wbs
        .type wbs, @function

/*
 * W moim rozwiązaniu używam następującej techniki:
 * Rozwiązanie polega na zmodyfikowaniu implementacji popcnt wspominanej na ćwiczeniach (i użytej przeze mnie na pracowni clz).
 *
 * Podobnie jak w zwykłym popcnt zastosujemy strategie dziel i zwyciężaj.
 * Będziemy jednak de facto obliczali 2 popcnt jednocześnie: zwykły i ważony.
 * Zwykły popcnt będzie nam potrzebny do odpowiedniego obliczania tego ważonego.
 *
 * W trywialny sposób obliczamy kubełki 2-bitowe ważonego popcounta. Chcemy je teraz połączyć w kubełki 4-bitowe.
 * (10 10 -> 3210)
 * Dodając jednak sąsiednie kubełki do siebie nie otrzymujemy pełnej sumy ważonej (otrzymujemy 1010)
 * Mamy dobrze policzone wystąpienia 0. i 1. bitu w każdym kubełku, ale brakuje nam liczby wystąpień 2. i 3. bitu razy dwa.
 * (3210 - 1010 = 2200)
 * Te dodatkowe wystąpienia weźmiemy z kubełków 2-bitowych zwykłego popcounta.
 *
 * Analogicznie będziemy postępować aż do kubełków 16-bitowych.
 * (3210 3210 -> 76543210 (brakuje 44440000))
 * (76543210  76543210 -> 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 (brakuje 8888888800000000))
 *
 * Dalsze obliczenia możemy skrócić za pomocą mnożenia przez magiczne stałe.
 * Mamy liczbę podzieloną na 4 kubełki postaci 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0.
 * Skorzystamy z tego, że wartości w każdym z kubełków są już małe w stosunku do ich rozmiaru (max 00000000 01111000).
 * Oznacza to, że możemy je dodać do siebie nie ryzykując przepełnienia pomiędzy kubełkami.
 * Dodawanie to wykonamy za pomocą jednej instrukcji mnożenia.
 * x + (x << 16) + (x << 32) + (x << 48) = x + 65536x + 4294967296x + 281474976710656x = 281479271743489x
 * Takie mnożenie utworzy nam pożądaną sumę w najstarszych 16 bitach liczby.
 *
 * Wciąż brakuje nam jednak dopełnienia wystąpień z zwykłego popcounta do uzyskania poprawnego wyniku.
 * W nim wartości również są na tyle małe (max 00000000 00010000), że możemy je dodać za pomocą mnożenia.
 * Najmłodszy kubełek nie wymaga dopełnienia, 2-gi najmłodszy kubełek musimy przemnożyć przez 16, 3-ci przez 32, 4-ty przez 48.
 * 48x + 32(x << 16) + 16(x << 32) = 48x + 2097152x + 68719476736x = 68721573936x
 * Takie mnożenie utworzy nam pożądaną sumę w najstarszych 16 bitach liczby.
 *
 * Na koniec wystarczy wyłuskać obie te sumy z najstarszych bitów i dodać je do siebie.
 */

wbs:
        movq    %rdi, %rcx                      /* 2-bitowe przedziały ważonego popcnt */
        shrq    $1, %rcx                        /* Równoważny informacji o stanie najstarszego bitu */
        andq    .m1, %rcx



        movq    %rdi, %rdx                      /* 2-bitowe przedziały zwykłego popcnt */
        subq    %rcx, %rdx                      /* x -= ((x >> 1) & 0x5555555555555555) */
                                                /* Odjęcie od całego takiego przedziału jego starszego bitu daje liczbę jego zapalonych bitów */
                                                /* 00 - 00 = 00; 01 - 00 = 01; 10 - 01 = 01; 11 - 01 = 10 */

        movq    %rcx, %rsi                      /* Dodanie do siebie sąsiednich 2-bitowych przedziałów ważonego popcnt */
        shrq    $2, %rsi
        addq    %rsi, %rcx
        andq    .m2, %rcx

        movq    %rdx, %rax                      /* Dodanie do tej sumy dwukrotności zwykłego popcnt starszego z kubełków dla każdej pary */
        shrq    $2, %rax                        /* Otrzymujemy 4-bitowe przedziały ważonego popcnt */
        andq    .m2, %rax
        leaq    (%rcx,%rax,2), %rcx



        movq    %rdx, %rax                      /* 4-bitowe przedziały zwykłego popcnt */ 
        shrq    $2, %rax                        /* x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333) */
        andq    .m2, %rdx                       /* Dodajemy sąsiednie 2-bitowe przedziały do siebie */
        andq    .m2, %rax                       /* 00 + 00 = 0000; 00 + 01 = 0001; 00 + 10 = 0010 */
        addq    %rax, %rdx                      /* 01 + 01 = 0010; 01 + 10 = 0011; 10 + 10 = 0100 */

        movq    %rcx, %rsi                      /* Dodanie do siebie sąsiednich 4-bitowych przedziałów ważonego popcnt */
        shrq    $4, %rsi                        
        addq    %rsi, %rcx
        andq    .m3, %rcx

        movq    %rdx, %rax                      /* Dodanie do tej sumy czterokrotności zwykłego popcnt starszego z kubełków dla każdej pary */
        shrq    $4, %rax                        /* Otrzymujemy 8-bitowe przedziały ważonego popcnt */
        andq    .m3, %rax
        leaq    (%rcx,%rax,4), %rcx



        movq    %rdx, %rax                      /* 8-bitowe przedziały zwykłego popcnt */ 
        shrq    $4, %rax                        /* x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f */
        addq    %rax, %rdx                      /* Największy przedział 4-bitowy to 0100 zatem przy sumowaniu... */
        andq    .m3, %rdx                       /* ...nie dojdzie do overflow - maskę nakładamy na sumę */

        movq    %rcx, %rsi                      /* Dodanie do siebie sąsiednich 8-bitowych przedziałów ważonego popcnt */
        shrq    $8, %rsi
        addq    %rsi, %rcx
        andq    .m4, %rcx

        movq    %rdx, %rax                      /* Dodanie do tej sumy osmiokrotności zwykłego popcnt starszego z kubełków dla każdej pary */
        shrq    $8, %rax                        /* Otrzymujemy 16-bitowe przedziały ważonego popcnt */
        andq    .m4, %rax
        leaq    (%rcx,%rax,8), %rcx



        addq    %rax, %rdx                      /* 16-bitowe przedziały zwykłego popcnt */ 
        andq    .m4, %rdx                       /* x = (x + x >> 8) & 0x00ff00ff00ff00ff */
        imulq   .magic, %rdx                    /* Obliczenie odpowiednio wyważonego popcnt do końca przez wymnożenie przez magiczną stałą */

        imulq   .magic2, %rcx                   /* Zsumowanie wszystkich ważonych kubełków przez wymnożenie przez magiczną stałą */
        
        leaq    (%rcx, %rdx,), %rax             
        shrq    $48, %rax                       /* Powyższe mnożenia umieściły pożądane wyniki w górnych 16 bitach rejestru */
        ret

        .size wbs, .-wbs

        .data
        .m1: .quad 0x5555555555555555           /* 0101010101010101010101010101010101010101010101010101010101010101 */
        .m2: .quad 0x3333333333333333           /* 0011001100110011001100110011001100110011001100110011001100110011 */
        .m3: .quad 0x0f0f0f0f0f0f0f0f           /* 0000111100001111000011110000111100001111000011110000111100001111 */
        .m4: .quad 0x00ff00ff00ff00ff           /* 0000000011111111000000001111111100000000111111110000000011111111 */
        .magic: .quad 0x0000001000200030        /* 48x + 32(x << 16) + 16(x << 32) = 48x + 2097152x + 68719476736x = 68721573936x */   
        .magic2: .quad 0x0001000100010001       /* x + (x << 16) + (x << 32) + (x << 48) = x + 65536x + 4294967296x + 281474976710656x = 281479271743489x */
        