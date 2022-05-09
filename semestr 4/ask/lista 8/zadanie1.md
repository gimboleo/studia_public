> **Zadanie 1.** Poniżej podano zawartość pliku `«swap.c»`. Wskaż w nim wszystkie wystąpienia definicji i referencji do **symboli** [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), §7.5]. Dla każdego symbolu wskaż jego **zasięg widoczności** (tj. lokalny, globalny, zewnętrzny) oraz nazwę **sekcji**, w której go umieszczono (tj. `«.text»`, `«.data»`, `«.rodata»`, `«.bss»`). Wydając polecenie `«make swap.o»` wygeneruj `plik relokowalny` i zweryfikuj swoje odpowiedzi na podstawie wydruku z polecenia [nm](https://sourceware.org/binutils/docs/binutils/nm.html). Do czego konsolidator wykorzystuje tablicę symboli?

```c
extern int printf(const char *, ...);       // Deklaracja zewnętrznego symbolu
extern int buf[];                           // Deklaracja zewnętrznego symbolu

int *bufp0 = &buf[0];                       // Definicja symbolu i referencja do zewnętrznego symbolu
static int *bufp1;                          // Definicja symbolu
static float sum = 0.0;                     // Definicja symbolu

static void incr() {                        // Definicja symbolu
  static int count = 0;                     // Definicja symbolu
  count++;                                  // Referencja do symbolu
}

void addf(float x) {                        // Definicja symbolu
  sum += x + 3.14;                          // Referencja do symbolu stałej?
  printf("sum = %f\n", sum);                // Referencja do zewnętrznego symbolu i symbolu stringa
}

void swap() {                               // Definicja symbolu
  int temp;
  incr();                                   // Referencja do symbolu
  bufp1 = &buf[1];                          // Referencja do symbolu i zewnętrznego symbolu
  temp = *bufp0;                            // Referencja do symbolu
  *bufp0 = *bufp1;                          // Referencja do symboli
  *bufp1 = temp;                            // Referencja do symbolu
}
```

```
nm swap.o:

======================================================

0000000000000008 T addf            // global, section .text
                 U buf             // extern, 'section' .UNDEF
0000000000000000 D bufp0           // global, section .data
0000000000000008 b bufp1           // local, section .bss
0000000000000000 b count.0         // local, section .bss
0000000000000000 t incr            // local, section .text
0000000000000000 r .LC0            // local, section .rodata (3.14?)
0000000000000000 r .LC1            // local, section .rodata ("sum = %f\n")
                 U printf          // extern, 'section' .UNDEF
0000000000000004 b sum             // local, section .bss
0000000000000050 T swap            // global, section .text
```

Konsolidator wykorzystuje tablicę symboli do rozwiązywania symboli - w trakcie konsolidacji każda referencja do symbolu jest związywana z dokładnie jedną definicją symbolu.