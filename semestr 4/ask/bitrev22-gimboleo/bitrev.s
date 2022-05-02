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
        .globl  bitrev
        .type bitrev, @function

/*
 * W moim rozwiązaniu używam następującej techniki:
 * Rozwiązanie polega na zastosowaniu strategii dziel i zwyciężaj i jest podzielone na 2 części.
 *
 * Najpierw odwracamy za pomocą prostych masek i przesunięć kubełki kolejno 2, 4 i 8 bitowe uzyskując...
 * ...poprawne odwrócenia w zakresie poszczególnych bajtów.
 *
 * Następnie ustawiamy w odpowiedniej kolejności wszystkie bajty. Zamiast masek i przesunięć...
 * ...możemy tym razem skorzystać z instrukcji rol/ror.
 */

bitrev:
        movabsq $0x5555555555555555, %r8        /* 0101010101010101010101010101010101010101010101010101010101010101 */
        movabsq $0x3333333333333333, %r9        /* 0011001100110011001100110011001100110011001100110011001100110011 */
        movabsq $0x0f0f0f0f0f0f0f0f, %r10       /* 0000111100001111000011110000111100001111000011110000111100001111 */

        movq    %rdi, %rax                      /* x = ((x >> 1) & %r8) | ((x & %r8) << 1) */
        shrq    $1, %rax
        andq    %r8, %rax
        andq    %rdi, %r8
        leaq    (%rax, %r8, 2), %rax
        movq    %rax, %r8                       /* x = ((x >> 2) & %r9) | ((x & %r9) << 2) */
        shrq    $2, %r8
        andq    %r9, %r8
        andq    %r9, %rax
        leaq    (%r8, %rax, 4), %rax
        movq    %rax, %r8                       /* x = ((x >> 4) & %r10) | ((x & %r10) << 4) */
        shrq    $4, %r8
        andq    %r10, %r8
        andq    %r10, %rax
        leaq    (%rax, %rax), %rax
        leaq    (%r8, %rax, 8), %rax  

        movq    %rax, %rdx                      /* A B C D E F G H */                  
        rolw    $8, %ax                         /* A B C D E F H G */
        roll    $16, %eax                       /* 0 0 0 0 H G E F */
        rolw    $8, %ax                         /* 0 0 0 0 H G F E */
        shrq    $32, %rdx                       /* 0 0 0 0 A B C D */
        rolw    $8, %dx                         /* 0 0 0 0 A B D C */
        roll    $16, %edx                       /* 0 0 0 0 D C A B */ 
        rolw    $8, %dx                         /* 0 0 0 0 D C B A */
        shlq    $32, %rax                       /* H G F E 0 0 0 0 */
        orq     %rdx, %rax                      /* H G F E A B C D */
        ret

        .size bitrev, .-bitrev
