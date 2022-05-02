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
        .globl  addsb
        .type   addsb, @function

/*
 * W moim rozwiązaniu używam następującej techniki:
 * Rozwiązanie jest podzielone na 2 części.
 *
 * Najpierw wykonujemy dodawanie x + y na poszczególnych bajtach zapobiegając przeniesieniu między bajtami.
 * Wykonujemy je prostymi maskami tak jak w zadaniu 2.4.
 * Najpierw liczymy wszystkie bity w bajtach poza ostatnimi, żeby zapobiec nielegalnemu przeniesieniu, ... 
 * ...a potem 'ręcznie' wyliczamy wartości ostatnich bitów ignorując ich przeniesienie.
 *
 * Teraz chcemy upewnić się, że jeżeli wynik dodawania w danym bajcie jest przekręcony, ustawimy jego wartość na -128/127.
 * W tym celu najpierw wyliczamy wartość logiczną, która odpowiada na pytanie czy dodawanie spowodowało overflow.
 * Robimy to za pomocą porównania bitu znaku wyniku z bitami znaku elementów sumy (tak jak w zadaniu 2.3).
 * Za pomocą masek w postaci rozsmarowanych na cały bajt bitów znaku i overflow możemy skonstruować odpowiedni wynik.
 */

addsb:
        movabsq $0x7F7F7F7F7F7F7F7F, %r8        /* 01111111 01111111 01111111 01111111 01111111 01111111 01111111 01111111 */
        movabsq $0x8080808080808080, %r9        /* 10000000 10000000 10000000 10000000 10000000 10000000 10000000 10000000 */

        movq %rdi, %rax                         /* s = (x & %r8) + (y & %r8) */
        movq %rsi, %rdx
        andq %r8, %rax
        andq %r8, %rdx
        addq %rdx, %rax
        movq %rdi, %rcx                         /* s ^= (x ^ y) & %r9 */
        xorq %rsi, %rcx
        andq %r9, %rcx
        xorq %rcx, %rax

        movq %rdi, %rdx                         /* ((s ^ x) & (s ^ y) & %r9) >> 7 */                       
        movq %rsi, %rcx
        xorq %rax, %rdx
        xorq %rax, %rcx
        andq %rcx, %rdx
        andq %r9, %rdx 
        shrq $7, %rdx                         

                                                /* Rozsmarowanie bitu overflow */
        leaq (%rdx, %rdx, 2), %rdx              /* 00000011... */
        leaq (%rdx, %rdx, 4), %rdx              /* 00001111... */
        leaq (, %rdx, 8), %rcx                  /* 01111000... */
        leaq (%rdx, %rcx, 2), %rdx              /* 11111111... */

        andq %rdi, %r9                          /* Rozsmarowanie bitu znaku */
        shrq $7, %r9                            /* Analogiczne do tego powyżej */
        leaq (%r9, %r9, 2), %r9                 /* Rozważamy wyłącznie bit jednego z elementów sumy */
        leaq (%r9, %r9, 4), %r9                 /* (Sumowanie liczb przeciwnych znaków nie doprowadzi do overflow) */
        leaq (, %r9, 8), %rcx
        leaq (%r9, %rcx, 2), %r9

        xorq %r8, %r9                           /* 10000000... (dla ujemnych x, y) / 01111111... (dla nieujemnych x, y) */
        andq %rdx, %r9                          /* Wyzerowanie tej maski, jeżeli overflow nie wystąpił */
        notq %rdx
        andq %rdx, %rax                         /* Wyzerowanie wyniku, jeżeli overflow wystąpił */
        orq %r9, %rax                           /* Nałożenie maski */
        ret

        .size   addsb, .-addsb
