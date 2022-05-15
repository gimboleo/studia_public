> **Zadanie 5.** Zmodyfikuj opcje kompilacji programu `«ropex»` w pliku `«Makefile»`. Najpierw zleć kompilatorowi dodanie **kanarków** (ang. *canary*) włączając opcję `«-fstack-protector»`. Pokaż, że program wykrywa **uszkodzenie stosu** (ang. *stack smashing*). Posługując się debuggerem gdb zaprezentuj, że przy każdym uruchomieniu programu wartość kanarka jest inna. Następnie usuń opcję wymuszającą statyczną konsolidację `«-static»` i dodaj opcję `«-fpie»`, aby umożliwić **randomizację rozkładu przestrzeni adresowej** (ang. *Address Space Layout Randomization*). Pokaż, że adres gadżetu o nazwie `«gadget»` jest inny przy każdym uruchomieniu programu. Następnie dodaj opcję kompilacji `«-z noexecstack»,` która zapisuje w pliku ELF informacje o tym, że procesor nie powinien próbować wykonywać zawartości stosu. Przy pomocy programu `«pmap»` zweryfikuj, że istotnie stos uruchomionego programu `«ropex»` nie jest wykonywalny. Czemu każde z zastosowanych wyżej zabezpieczeń utrudnia zadanie atakującemu?
>> **Uwaga!** Debugger gdb może wyłączyć ASLR przeprowadzaną przez konsolidator dynamiczny, aby ułatwić sobie pracę.

### Oryginalna kompilacja
- `gcc -ggdb -static -Og -Wall -fno-pie -fno-stack-protector -fno-asynchronous-unwind-tables -c -o ropex.o ropex.c`
- `as -o gadget.o gadget.s`
- `gcc -ggdb -static -Og -Wall -fno-pie -fno-stack-protector -fno-asynchronous-unwind-tables -Wl,-Map=ropex.map -o ropex ropex.o gadget.o`

### Dodanie kanarków
- `gcc -ggdb -static -Og -Wall -fno-pie -fstack-protector -fno-asynchronous-unwind-tables -c -o ropex2.o ropex.c`
- `gcc -ggdb -static -Og -Wall -fno-pie -fstack-protector -fno-asynchronous-unwind-tables -Wl,-Map=ropex.map -o ropex ropex2.o gadget.o`
- `./ropex2 ropex2.in` kończy się wykryciem uszkodzenia stosu
- `gdb --args ropex2 ropex2.in` (`x/56b $sp` / `x/96b $sp`)
- Znacznie utrudnia atak przez przepełnienie bufora

### Dodanie ASLR
- `gcc -ggdb -fpie -Og -Wall -fstack-protector -fno-asynchronous-unwind-tables -c -o ropex3.o ropex.c`
- `gcc -ggdb -fpie -Og -Wall -fstack-protector -fno-asynchronous-unwind-tables -Wl,-Map=ropex.map -o ropex3 ropex3.o gadget.o`
- `gdb --args ropex3 ropex2.in` (`set disable-randomization off`, `info adress gadget`)
- Znacznie utrudnia znalezienie gadżetów w kodzie

### Niewykonywalny stos
- `gcc -ggdb -fpie -Og -Wall -fstack-protector -fno-asynchronous-unwind-tables -z noexecstack -c -o ropex4.o ropex.c`
- `gcc -ggdb -fpie -Og -Wall -fstack-protector -fno-asynchronous-unwind-tables -z noexecstack -Wl,-Map=ropex.map -o ropex4 ropex4.o gadget.o`
- `ps - e`
- `psmap -x xxxxx`
- Uniemożliwia wykonanie własnego kodu ze stosu