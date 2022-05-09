> **Zadanie 10 (bonus).** Plik wykonywalny powstały w wyniku kompilacji poniższych plików źródłowych powinien być nie dłuższy niż 1KiB. Na podstawie nagłówka pliku ELF wskaż w zdeasemblowanym pierwszą instrukcję, którą wykona procesor po wejściu do programu. Na podstawie nagłówków programu wskaż pod jaki adres wirtualny zostanie załadowany segment z sekcją `«.text»`.
>> ```c
>> /* start.c */
>> int is_even(long);
>> 
>> void _start(void) {
>>   asm volatile(
>>     "syscall"
>>     : /* no output */
>>     : "a" (0x3c), "D" (is_even(42)));
>> }
>> ```
>
>> ```c
>> /* even.c */
>> int is_odd(long n);
>>
>> int is_even(long n) {
>>   if (n == 0)
>>     return 1;
>>   else
>>     return is_odd(n - 1);
>> }
>> ```
>
>> ```c
>> /* odd.c */
>> int is_even(long n);
>> 
>> int is_odd(long n) {
>>   if (n == 0)
>>     return 0;
>>   else
>>     return is_even(n - 1);
>> }
>> ```
>
> Zapoznaj się z uproszczonym **skryptem konsolidatora** w pliku `«main.lds»`. Na podstawie [dokumentacji](https://sourceware.org/binutils/docs/ld/Scripts.html) wyjaśnij jak skrypt kieruje procesem konsolidacji poszczególnych sekcji i tworzeniem nagłówków programu.

[Linux Syscall Table](https://filippo.io/linux-syscall-table/)

```
readelf -h main

======================================================

ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00 
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              EXEC (Executable file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x400122                               /* !!! */
  Start of program headers:          64 (bytes into file)
  Start of section headers:          384 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         3
  Size of section headers:           64 (bytes)
  Number of section headers:         4
  Section header string table index: 3
```

```
objdump -d main

======================================================

main:     file format elf64-x86-64


Disassembly of section .text:

00000000004000e8 <.text>:
  4000e8:       48 85 ff                test   %rdi,%rdi
  4000eb:       75 06                   jne    0x4000f3
  4000ed:       b8 01 00 00 00          mov    $0x1,%eax
  4000f2:       c3                      retq   
  4000f3:       48 83 ec 08             sub    $0x8,%rsp
  4000f7:       48 83 ef 01             sub    $0x1,%rdi
  4000fb:       e8 05 00 00 00          callq  0x400105
  400100:       48 83 c4 08             add    $0x8,%rsp
  400104:       c3                      retq   
  400105:       48 85 ff                test   %rdi,%rdi
  400108:       75 06                   jne    0x400110
  40010a:       b8 00 00 00 00          mov    $0x0,%eax
  40010f:       c3                      retq   
  400110:       48 83 ec 08             sub    $0x8,%rsp
  400114:       48 83 ef 01             sub    $0x1,%rdi
  400118:       e8 cb ff ff ff          callq  0x4000e8
  40011d:       48 83 c4 08             add    $0x8,%rsp
  400121:       c3                      retq   
  400122:       48 83 ec 08             sub    $0x8,%rsp                    /* !!! */
  400126:       bf 2a 00 00 00          mov    $0x2a,%edi
  40012b:       e8 b8 ff ff ff          callq  0x4000e8
  400130:       89 c7                   mov    %eax,%edi
  400132:       b8 3c 00 00 00          mov    $0x3c,%eax
  400137:       0f 05                   syscall 
  400139:       48 83 c4 08             add    $0x8,%rsp
  40013d:       c3                      retq 
```

```
readelf -l main

======================================================

Elf file type is EXEC (Executable file)
Entry point 0x400122
There are 3 program headers, starting at offset 64

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
  LOAD           0x00000000000000e8 0x00000000004000e8 0x00000000004000e8   /* !!! */
                 0x0000000000000056 0x0000000000000056  R E    0x1000
  LOAD           0x00000000000000e8 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  R      0x1000
  LOAD           0x00000000000000e8 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     0x1000

 Section to Segment mapping:
  Segment Sections...
   00     .text 
   01     
   02   
```

```
main.lds

======================================================

OUTPUT_FORMAT("elf64-x86-64")       /* typ pliku wyjściowego */
OUTPUT_ARCH(i386:x86-64)            /* architektura procesora */
ENTRY(_start)                       /* entry point address */
PHDRS                               /* program headers (segmenty) */
{
  code   PT_LOAD FLAGS(5);          /* PT_LOAD - nagłówek segment do załadowania z pliku */
  rodata PT_LOAD FLAGS(4);          /* FLAGS(x) - ustawianie flag dla danego segmentu */
  data   PT_LOAD FLAGS(6);
}
SECTIONS                            /* zarządzanie sekcjami */
{
  . = 0x400000 + SIZEOF_HEADERS;    /* adres początkowej sekcji (. to location counter) */

  .text :                           /* nazwa sekcji wyjściowej */
  {
    *(.text .text.*)                /* regex matching sekcji wejściowych */
  } : code                          /* segment, w którym zapisana zostanie nowa sekcja */

                                    /* (linker sam dba o odpowiedni adres / alignment) */    

  .rodata :
  {
    *(.rodata .rodata.*)
  } : rodata

  .data : 
  {
    *(.data .data.*)
  } : data

  .bss :
  {
   *(.bss .bss.*)
   *(COMMON)
  } : data

  /DISCARD/ :                       /* sekcje odrzucone, nie dołączane do pliku wyjściowego */
  {
    *(.note.gnu.property)
  }
}
```