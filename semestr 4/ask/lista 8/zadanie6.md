> **Zadanie 6.** Wydrukuj tablice **rekordów relokacji** z sekcji `«.rel.text»` i `«.rel.data»` pliku `«swap.o»` przy pomocy polecenia `«readelf -r»`. Na podstawie [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), §7.7.1] wytłumacz uczestnikom zajęć składowe **rekordów relokacji** `«Elf64_Rela»` [[2](http://www.sco.com/developers/gabi/latest/contents.html), 4-23]. Wyjaśnij jak na podstawie tablicy rekordów relokacji polecenie `«objdump -d -r swap.o»` identyfikuje w zdeasemblowanym kodzie miejsca, które konsolidator będzie musiał uzupełnić w trakcie generowania pliku wykonywalnego. Czy możliwe jest by asembler utworzył sekcję `«.rel.bss»`?

Po tym jak konsolidator przeprowadzi operację rozwiązywania symboli, zna miejsca dwołań i definicji symboli, oraz dokładny rozmiar sekcji kodu i danych w plikach relokowalnych. Może następnie rozpocząc proces relokacji, czyli zmerge'owania poszczególnych sekcji kodu / danych oraz zrelokowania symboli z ich relatywnych pozycji w poszczególnych plikach `.o` do ich ostatecznych adresów w pamięci. Relokacja składa się z dwóch części:
- Sekcje tego samego typu z wejściowych plików `.o` są łączone. Segmentom, sekcjom i symbolom są przypisywane ostateczne adresy.
- Adresy które do tej pory były niewypełnone (bo odwoływały się do jakichś zewnętrznych symboli) są uzupełniane do przypisanych w poprzednim kroku adresów na podstawie rekordów relokacji zawartych w plikach `.o`.

Gdy asembler generuje plik `.o` nie wie, gdzie kod i dane będą ostatecznie przechowywane w pamięci. Nie zna też lokalizacji żadnych zewnętrznie zdefiniowanych funkcji / zmiennych globalnych, do których odwołuje się moduł. Dlatego za każdym razem, gdy asembler napotyka referencję do symbolu, którego którego ostateczna lokalizacja nie jest znana, generuje rekord relokacji, który mówi konsolidatorowi jak zmodyfikować to odwołanie, gdy połączy pliki `.o` w plik wykonywalny. Rekordy relokacji dla kodu są umieszczane w `«.rel.text»`. Rekordy relokacji dla danych są umieszczane w `«.rel.data»`.

Rekord relokacji:
```c
typedef struct {
    long offset;    /* Offset of the reference to relocate */
    long type:32,   /* Relocation type (absolute / relative)*/
         symbol:32; /* Symbol table index */
    long addend;    /* Constant part of relocation expression */
} Elf64_Rela;
```

```
readelf -r swap.o

======================================================

Relocation section '.rela.text' at offset 0x310 contains 11 entries:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000000002  000100000002 R_X86_64_PC32     0000000000000000 .bss - 5
000000000018  000600000002 R_X86_64_PC32     0000000000000000 .LC0 - 4
000000000024  000100000002 R_X86_64_PC32     0000000000000000 .bss + 0
000000000034  000100000002 R_X86_64_PC32     0000000000000000 .bss + 0
00000000003d  00040000000a R_X86_64_32       0000000000000000 .rodata.str1.1 + 0
000000000047  000f00000004 R_X86_64_PLT32    0000000000000000 printf - 4
00000000005d  000100000002 R_X86_64_PC32     0000000000000000 .bss + 0
000000000061  00110000000b R_X86_64_32S      0000000000000000 buf + 4
000000000068  001200000002 R_X86_64_PC32     0000000000000000 bufp0 - 4
000000000070  001100000002 R_X86_64_PC32     0000000000000000 buf + 0
000000000078  001100000002 R_X86_64_PC32     0000000000000000 buf + 0

Relocation section '.rela.data' at offset 0x418 contains 1 entry:
  Offset          Info           Type           Sym. Value    Sym. Name + Addend
000000000000  001100000001 R_X86_64_64       0000000000000000 buf + 0
```

Korzystając z tej tabeli jesteśmy w stanie jednoznacznie zidentyfikować w zdeasemblowanym kodzie miejsca, które konsolidator będzie musiał uzupełnić:
```
objdump -d -r swap.o

======================================================

swap.o:     file format elf64-x86-64


Disassembly of section .text:

0000000000000000 <incr>:
   0:   83 05 00 00 00 00 01    addl   $0x1,0x0(%rip)        # 7 <incr+0x7>
                        2: R_X86_64_PC32        .bss-0x5
   7:   c3                      retq   

0000000000000008 <addf>:
   8:   48 83 ec 08             sub    $0x8,%rsp
   c:   66 0f ef c9             pxor   %xmm1,%xmm1
  10:   f3 0f 5a c8             cvtss2sd %xmm0,%xmm1
  14:   f2 0f 58 0d 00 00 00    addsd  0x0(%rip),%xmm1        # 1c <addf+0x14>
  1b:   00 
                        18: R_X86_64_PC32       .LC0-0x4
  1c:   66 0f ef c0             pxor   %xmm0,%xmm0
  20:   f3 0f 5a 05 00 00 00    cvtss2sd 0x0(%rip),%xmm0        # 28 <addf+0x20>
  27:   00 
                        24: R_X86_64_PC32       .bss
  28:   f2 0f 58 c1             addsd  %xmm1,%xmm0
  2c:   f2 0f 5a c0             cvtsd2ss %xmm0,%xmm0
  30:   f3 0f 11 05 00 00 00    movss  %xmm0,0x0(%rip)        # 38 <addf+0x30>
  37:   00 
                        34: R_X86_64_PC32       .bss
  38:   f3 0f 5a c0             cvtss2sd %xmm0,%xmm0
  3c:   bf 00 00 00 00          mov    $0x0,%edi
                        3d: R_X86_64_32 .rodata.str1.1
  41:   b8 01 00 00 00          mov    $0x1,%eax
  46:   e8 00 00 00 00          callq  4b <addf+0x43>
                        47: R_X86_64_PLT32      printf-0x4
  4b:   48 83 c4 08             add    $0x8,%rsp
  4f:   c3                      retq   

0000000000000050 <swap>:
  50:   b8 00 00 00 00          mov    $0x0,%eax
  55:   e8 a6 ff ff ff          callq  0 <incr>
  5a:   48 c7 05 00 00 00 00    movq   $0x0,0x0(%rip)        # 65 <swap+0x15>
  61:   00 00 00 00 
                        5d: R_X86_64_PC32       .bss
                        61: R_X86_64_32S        buf+0x4
  65:   48 8b 05 00 00 00 00    mov    0x0(%rip),%rax        # 6c <swap+0x1c>
                        68: R_X86_64_PC32       bufp0-0x4
  6c:   8b 10                   mov    (%rax),%edx
  6e:   8b 0d 00 00 00 00       mov    0x0(%rip),%ecx        # 74 <swap+0x24>
                        70: R_X86_64_PC32       buf
  74:   89 08                   mov    %ecx,(%rax)
  76:   89 15 00 00 00 00       mov    %edx,0x0(%rip)        # 7c <swap+0x2c>
                        78: R_X86_64_PC32       buf
  7c:   c3                      retq   
```

Z reguły asembler nie powinien utworzyć sekcji `«.rel.bss»` - w sekcji `«.bss»` znajdują się symbole zmiennych statycznych lub zaincjalizowanych wartością zerową i nie potrzebują relokacji - konsolidator już zna ich adresy. Sekcja taka może jednak powstać przez przypadek (przykładowo przez [umieszczenie kodu w sekcji `«.bss»`](https://stackoverflow.com/a/37057108)).