> **Zadanie 2.** Co przechowują sekcje `«.strtab»` i `«.shstrtab»` [[2](http://www.sco.com/developers/gabi/latest/contents.html), 4-17]? Opisz znaczenie pól rekordu symbolu `«Elf64_Sym»` [[2](http://www.sco.com/developers/gabi/latest/contents.html), 4-18] przechowywanego w **tablicy symboli** [[2](http://www.sco.com/developers/gabi/latest/contents.html), 4], oraz pól rekordu nagłówka sekcji `«Elf64_Shdr»` [[2](http://www.sco.com/developers/gabi/latest/contents.html), 4-8]. Na podstawie zdobytej wiedzy omów wydruk polecenia [readelf](https://sourceware.org/binutils/docs/binutils/readelf.html) z opcjami `«-t -s»` na pliku `«swap.o»`. Skąd wiadomo gdzie w pliku relokowalnym znajdują się nagłówki sekcji oraz zawartość poszczególnych sekcji? Jaka jest pozycja danego symbolu względem początku sekcji?

Sekcja `«.strtab»` *(string table)* przechowuje stringi reprezentujące nazwy symboli. Sekcja `«.shstrtab»` *(section header string table)* przechowuje nazwy sekcji.

[Pola rekordów `«Elf64_Sym»` tablicy symboli.](http://www.sco.com/developers/gabi/latest/ch4.symtab.html)

[Pola rekordów `«Elf64_Shdr»` tablicy nagłówków sekcji.](http://www.sco.com/developers/gabi/latest/ch4.sheader.html)

```
readelf -t -s swap.o

======================================================

There are 13 section headers, starting at offset 0x4a0:

Section Headers:
  [Nr] Name
       Type              Address          Offset            Link
       Size              EntSize          Info              Align
       Flags
  [ 0] 
       NULL             0000000000000000  0000000000000000  0
       0000000000000000 0000000000000000  0                 0
       [0000000000000000]: 
  [ 1] .text
       PROGBITS         0000000000000000  0000000000000040  0
       000000000000007d 0000000000000000  0                 1
       [0000000000000006]: ALLOC, EXEC
  [ 2] .rela.text
       RELA             0000000000000000  0000000000000310  10
       0000000000000108 0000000000000018  1                 8
       [0000000000000040]: INFO LINK
  [ 3] .data
       PROGBITS         0000000000000000  00000000000000c0  0
       0000000000000008 0000000000000000  0                 8
       [0000000000000003]: WRITE, ALLOC
  [ 4] .rela.data
       RELA             0000000000000000  0000000000000418  10
       0000000000000018 0000000000000018  3                 8
       [0000000000000040]: INFO LINK
  [ 5] .bss
       NOBITS           0000000000000000  00000000000000c8  0
       0000000000000010 0000000000000000  0                 8
       [0000000000000003]: WRITE, ALLOC
  [ 6] .rodata.str1.1
       PROGBITS         0000000000000000  00000000000000c8  0
       000000000000000a 0000000000000001  0                 1
       [0000000000000032]: ALLOC, MERGE, STRINGS
  [ 7] .rodata.cst8
       PROGBITS         0000000000000000  00000000000000d8  0
       0000000000000008 0000000000000008  0                 8
       [0000000000000012]: ALLOC, MERGE
  [ 8] .comment
       PROGBITS         0000000000000000  00000000000000e0  0
       0000000000000028 0000000000000001  0                 1
       [0000000000000030]: MERGE, STRINGS
  [ 9] .note.GNU-stack
       PROGBITS         0000000000000000  0000000000000108  0
       0000000000000000 0000000000000000  0                 1
       [0000000000000000]: 
  [10] .symtab
       SYMTAB           0000000000000000  0000000000000108  11
       00000000000001c8 0000000000000018  14                8
       [0000000000000000]: 
  [11] .strtab
       STRTAB           0000000000000000  00000000000002d0  0
       000000000000003d 0000000000000000  0                 1
       [0000000000000000]: 
  [12] .shstrtab
       STRTAB           0000000000000000  0000000000000430  0
       000000000000006b 0000000000000000  0                 1
       [0000000000000000]: 

Symbol table '.symtab' contains 19 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000000     0 SECTION LOCAL  DEFAULT    5 
     2: 0000000000000000     8 FUNC    LOCAL  DEFAULT    1 incr
     3: 0000000000000000     4 OBJECT  LOCAL  DEFAULT    5 count.0
     4: 0000000000000000     0 SECTION LOCAL  DEFAULT    6 
     5: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT    6 .LC1
     6: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT    7 .LC0
     7: 0000000000000004     4 OBJECT  LOCAL  DEFAULT    5 sum
     8: 0000000000000008     8 OBJECT  LOCAL  DEFAULT    5 bufp1
     9: 0000000000000000     0 SECTION LOCAL  DEFAULT    1 
    10: 0000000000000000     0 SECTION LOCAL  DEFAULT    3 
    11: 0000000000000000     0 SECTION LOCAL  DEFAULT    7 
    12: 0000000000000000     0 SECTION LOCAL  DEFAULT    8 
    13: 0000000000000000     0 SECTION LOCAL  DEFAULT    9 
    14: 0000000000000008    72 FUNC    GLOBAL DEFAULT    1 addf
    15: 0000000000000000     0 NOTYPE  GLOBAL DEFAULT  UND printf
    16: 0000000000000050    45 FUNC    GLOBAL DEFAULT    1 swap
    17: 0000000000000000     0 NOTYPE  GLOBAL DEFAULT  UND buf
    18: 0000000000000000     8 OBJECT  GLOBAL DEFAULT    3 bufp0
```

Pole `«e_shoff»` nagłówka pliku ELF trzyma offset tablicy nagłówków sekcji od początku pliku. W tej tablicy znaleźć można informacje o poszczególnych sekcjach.

Dla zdefiniowanych symboli pole `«st_value»` trzyma offset danego symbolu od początku jego sekcji.