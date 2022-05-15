> **Zadanie 6.** Jądro systemu Linux nie potrafi załadować do pamięci pliku wykonywalnego skonsolidowanego dynamicznie – musi o to poprosić **interpreter programu** [[2](http://www.sco.com/developers/gabi/latest/contents.html), 5]. Rozważmy plik wykonywalny `«/bin/sleep»`. Na podstawie zawartości jego sekcji `«.interp»` podaj ścieżkę do konsolidatora dynamicznego [[2](http://www.sco.com/developers/gabi/latest/contents.html), 5]. Przy pomocy polecenia `«nm»` wyświetl wszystkie symbole dynamiczne – [ld.so(8)](https://man7.org/linux/man-pages/man8/ld.so.8.html) będzie musiał znaleźć ich definicje w bibliotekach dynamicznych. Przy pomocy polecenia `«readelf -d»` wyświetl sekcję `«.dynamic»` [[2](http://www.sco.com/developers/gabi/latest/contents.html), 5-9] i wskaż biblioteki, w których będą wyszukiwane definicje symboli. Na podstawie podręcznika [ldconfig(8)](https://man7.org/linux/man-pages/man8/ldconfig.8.html) znajdź plik konfiguracyjny przechowujący ścieżki, gdzie konsolidator będzie szukał bibliotek. Wskaż skąd zostanie załadowana biblioteka `«libc.so.6».` Przy pomocy polecenia [ldd(1)](https://man7.org/linux/man-pages/man1/ldd.1.html) wyświetl pod jakie adresy konsolidator załadowałby biblioteki, gdyby miał załadować program do pamięci. Czemu za każdym razem adresy bibliotek są inne?

```
readelf -l /bin/sleep

======================================================

Elf file type is DYN (Shared object file)
Entry point 0x2850
There are 13 program headers, starting at offset 64

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
  PHDR           0x0000000000000040 0x0000000000000040 0x0000000000000040
                 0x00000000000002d8 0x00000000000002d8  R      0x8
  INTERP         0x0000000000000318 0x0000000000000318 0x0000000000000318
                 0x000000000000001c 0x000000000000001c  R      0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]             /* !!! */
  LOAD           0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x00000000000014f0 0x00000000000014f0  R      0x1000
  LOAD           0x0000000000002000 0x0000000000002000 0x0000000000002000
                 0x0000000000003c21 0x0000000000003c21  R E    0x1000
  LOAD           0x0000000000006000 0x0000000000006000 0x0000000000006000
                 0x0000000000001f38 0x0000000000001f38  R      0x1000
  LOAD           0x0000000000008bb0 0x0000000000009bb0 0x0000000000009bb0
                 0x00000000000004d0 0x0000000000000688  RW     0x1000
  DYNAMIC        0x0000000000008c78 0x0000000000009c78 0x0000000000009c78
                 0x00000000000001f0 0x00000000000001f0  RW     0x8
  NOTE           0x0000000000000338 0x0000000000000338 0x0000000000000338
                 0x0000000000000020 0x0000000000000020  R      0x8
  NOTE           0x0000000000000358 0x0000000000000358 0x0000000000000358
                 0x0000000000000044 0x0000000000000044  R      0x4
  GNU_PROPERTY   0x0000000000000338 0x0000000000000338 0x0000000000000338
                 0x0000000000000020 0x0000000000000020  R      0x8
  GNU_EH_FRAME   0x0000000000006f6c 0x0000000000006f6c 0x0000000000006f6c
                 0x00000000000002b4 0x00000000000002b4  R      0x4
  GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     0x10
  GNU_RELRO      0x0000000000008bb0 0x0000000000009bb0 0x0000000000009bb0
                 0x0000000000000450 0x0000000000000450  R      0x1

 Section to Segment mapping:
  Segment Sections...
   00     
   01     .interp 
   02     .interp .note.gnu.property .note.gnu.build-id .note.ABI-tag .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt 
   03     .init .plt .plt.got .plt.sec .text .fini 
   04     .rodata .eh_frame_hdr .eh_frame 
   05     .init_array .fini_array .data.rel.ro .dynamic .got .data .bss 
   06     .dynamic 
   07     .note.gnu.property 
   08     .note.gnu.build-id .note.ABI-tag 
   09     .note.gnu.property 
   10     .eh_frame_hdr 
   11     
   12     .init_array .fini_array .data.rel.ro .dynamic .got 
```

----

```
nm --dynamic /bin/sleep

======================================================

                 U abort
                 U bindtextdomain
                 U calloc
                 U __ctype_b_loc
                 U __ctype_get_mb_cur_max
                 U __cxa_atexit
                 w __cxa_finalize
                 U dcgettext
                 U __errno_location
                 U error
                 U _exit
                 U exit
000000000000a018 D exit_failure
                 U fclose
                 U fflush
                 U fileno
                 U __fpending
                 U __fprintf_chk
                 U fputs_unlocked
                 U __freading
                 U free
                 U fseeko
                 U fwrite
                 U getopt_long
                 w __gmon_start__
0000000000006000 R _IO_stdin_used
                 U iswprint
                 w _ITM_deregisterTMCloneTable
                 w _ITM_registerTMCloneTable
                 U __libc_start_main
                 U lseek
                 U malloc
                 U mbrtowc
                 U mbsinit
                 U memcmp
                 U memcpy
                 U memset
                 U nanosleep
                 U newlocale
                 U nl_langinfo
000000000000a0a0 B opterr
000000000000a090 B optind
                 U __printf_chk
000000000000a080 B __progname
000000000000a098 B __progname_full
000000000000a098 V program_invocation_name
000000000000a080 V program_invocation_short_name
000000000000a0e8 B program_name
000000000000a020 D quote_quoting_options
0000000000009c20 D quoting_style_args
0000000000006ba0 R quoting_style_vals
                 U realloc
                 U setlocale
                 U __stack_chk_fail
000000000000a0c0 B stderr
000000000000a088 B stdout
                 U strlen
                 U strncmp
                 U strrchr
                 U strtod_l
                 U textdomain
000000000000a010 D Version
0000000000006f00 R version_etc_copyright
```

----

```
readelf -d /bin/sleep

======================================================

Dynamic section at offset 0x8c78 contains 27 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]    /* !!! */
 0x000000000000000c (INIT)               0x2000
 0x000000000000000d (FINI)               0x5c14
 0x0000000000000019 (INIT_ARRAY)         0x9bb0
 0x000000000000001b (INIT_ARRAYSZ)       8 (bytes)
 0x000000000000001a (FINI_ARRAY)         0x9bb8
 0x000000000000001c (FINI_ARRAYSZ)       8 (bytes)
 0x000000006ffffef5 (GNU_HASH)           0x3a0
 0x0000000000000005 (STRTAB)             0xa48
 0x0000000000000006 (SYMTAB)             0x448
 0x000000000000000a (STRSZ)              799 (bytes)
 0x000000000000000b (SYMENT)             24 (bytes)
 0x0000000000000015 (DEBUG)              0x0
 0x0000000000000003 (PLTGOT)             0x9e68
 0x0000000000000002 (PLTRELSZ)           1008 (bytes)
 0x0000000000000014 (PLTREL)             RELA
 0x0000000000000017 (JMPREL)             0x1100
 0x0000000000000007 (RELA)               0xe48
 0x0000000000000008 (RELASZ)             696 (bytes)
 0x0000000000000009 (RELAENT)            24 (bytes)
 0x000000000000001e (FLAGS)              BIND_NOW
 0x000000006ffffffb (FLAGS_1)            Flags: NOW PIE
 0x000000006ffffffe (VERNEED)            0xde8
 0x000000006fffffff (VERNEEDNUM)         1
 0x000000006ffffff0 (VERSYM)             0xd68
 0x000000006ffffff9 (RELACOUNT)          18
 0x0000000000000000 (NULL)               0x0
```

----

```
    /etc/ld.so.conf.d  cat /etc/ld.so.conf
include /etc/ld.so.conf.d/*.conf

    /etc/ld.so.conf.d  ls /etc/ld.so.conf.d
fakeroot-x86_64-linux-gnu.conf  i386-linux-gnu.conf  libc.conf  x86_64-linux-gnu.conf  zz_i386-biarch-compat.conf

    /etc/ld.so.conf.d  cat /etc/ld.so.conf.d/x86_64-linux-gnu.conf 
# Multiarch support
/usr/local/lib/x86_64-linux-gnu
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

    /etc/ld.so.conf.d  find /lib/x86_64-linux-gnu/ -name libc.so.6
/lib/x86_64-linux-gnu/libc.so.6
```

----

```
    /etc/ld.so.conf.d  ldd /bin/sleep 
linux-vdso.so.1 (0x00007ffccea7b000)
libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f1e05e3a000)
/lib64/ld-linux-x86-64.so.2 (0x00007f1e06061000)
```

[Dynamic linking](http://www.sco.com/developers/gabi/latest/ch5.dynamic.html)  
[Stack Overflow](https://stackoverflow.com/a/5169235)