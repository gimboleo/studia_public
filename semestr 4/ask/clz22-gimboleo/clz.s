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
        .globl  clz
        .type   clz, @function

/*
 * W moim rozwiązaniu używam następującej techniki: 
 * Rozwiązanie polega na zastosowaniu strategii dziel i zwyciężaj i jest podzielone na 2 części.
 *
 * Najpierw 'rozsmarowujemy' najbardziej znaczący bit liczby na prawo upewniając się, że liczba składa się z...
 * ...samych jedynek (nie licząc prefixu zer, którego długości szukamy).
 *
 * Następnie liczymy liczbę zapalonych bitów w tak zmodyfikowanej liczbie - dzielimy ją na kubełki, wyznaczając w...
 * ...każdym z nich liczbę zapalonych bitów, po czym łączymy je w większe kubełki dopóki nie uzyskamy jednego kubełka...
 * ...o długości całej liczby. Taką wartość wystarczy odjąć od liczby 64, żeby otrzymać rozwiązanie.
*/

clz:
        movabsq $0x5555555555555555, %r8        /* 0101010101010101010101010101010101010101010101010101010101010101 */
        movabsq $0x3333333333333333, %r9        /* 0011001100110011001100110011001100110011001100110011001100110011 */
        movabsq $0x0f0f0f0f0f0f0f0f, %r10       /* 0000111100001111000011110000111100001111000011110000111100001111 */

        movq    %rdi, %rdx                      /* x |= x >> 1 */
        shrq    $1, %rdx
        orq     %rdi, %rdx
        movq    %rdx, %rax                      /* x |= x >> 2 */
        shrq    $2, %rax
        orq     %rax, %rdx
        movq    %rdx, %rax                      /* x |= x >> 4 */
        shrq    $4, %rax
        orq     %rax, %rdx
        movq    %rdx, %rax                      /* x |= x >> 8 */
        shrq    $8, %rax
        orq     %rax, %rdx
        movq    %rdx, %rax                      /* x |= x >> 16 */
        shrq    $16, %rax
        orq     %rax, %rdx
        movq    %rdx, %rax                      /* x |= x >> 32 */
        shrq    $32, %rax                       /* W tym momencie wszystkie bity do najbardziej znaczącego są zapalone */          
        orq     %rax, %rdx                      /* Teraz wystarczy policzyć liczbę zapalonych bitów */

        movq    %rdx, %rax                      /* x -= ((x >> 1) & 0x5555555555555555) */
        shrq    $1, %rax                        /* Rozważamy 2-bitowe przedziały liczby */
        andq    %r8, %rax                       /* Odjęcie od całego takiego przedziału jego starszego bitu daje liczbę jego zapalonych bitów */
        subq    %rax, %rdx                      /* 00 - 00 = 00; 01 - 00 = 01; 10 - 01 = 01; 11 - 01 = 10 */

        movq    %rdx, %rax                      /* x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333) */
        shrq    $2, %rax                        /* Rozważamy 4-bitowe przedziały liczby */
        andq    %r9, %rdx                       /* Dodajemy sąsiednie 2-bitowe przedziały do siebie */
        andq    %r9, %rax                       /* 00 + 00 = 0000; 00 + 01 = 0001; 00 + 10 = 0010 */
        addq    %rax, %rdx                      /* 01 + 01 = 0010; 01 + 10 = 0011; 10 + 10 = 0100 */

        movq    %rdx, %rax                      /* x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f */
        shrq    $4, %rax                        /* Rozważamy 8-bitowe przedziały liczby */
        addq    %rax, %rdx                      /* Największy przedział 4-bitowy to 0100 zatem przy sumowaniu... */
        andq    %r10, %rdx                      /* ...nie dojdzie do overflow - maskę nakładamy na sumę */

        movq    %rdx, %rax                      /* x += x >> 8 */
        shrq    $8, %rax                        /* Od tej pory mniejsze przedziały zajmują nie więcej, niż połowę... */
        addq    %rax, %rdx                      /* ...większego przedziału, więc możemy zignorować nakładanie maski */
        movq    %rdx, %rax                      /* x += x >> 16 */
        shrq    $16, %rax
        addq    %rax, %rdx
        movq    %rdx, %rax                      /* x += x >> 32 */
        shrq    $32, %rax
        addq    %rax, %rdx

        movl    $64, %eax                       /* return 64 - (x & 255) */
        movzbl  %dl, %edx                       /* Policzyliśmy liczbę zapalonych bitów, a interesują nas zgaszone, ... */
        subl    %edx, %eax                      /* ...więc zwracamy 64 - liczba zapalonych bitów (po nałożeniu maski) */
        ret

        .size   clz, .-clz
