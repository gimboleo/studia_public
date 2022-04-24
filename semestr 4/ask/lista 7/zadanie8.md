> **Zadanie 8.** W języku C++ klasy mogą posiadać wirtualne metody. Zauważ, że w wierszu $12$ nie wiemy jakiego typu jest obiekt, na który wskazuje `«bp»`, tj. może to być zarówno `«Base»` jak i `«Derived»`. Użyj strony https://godbolt.org, żeby skompilować poniższy kod z opcjami `«-Os -fno-rtti»`². W wygenerowanym wydruku znajdź miejsce definicji i użycia **tabeli metod wirtualnych**. Opisz zawartość rekordu aktywacji procedury przed wykonaniem wiersza $18$. Skąd implementacja metody `«doit»` wie, gdzie w pamięci znajduje się zmienna `«data»`?
> ```c
> struct Base {
>     Base(int n) : data(n) {}
>     int data;
>     virtual int doit(int n) { return n - data; }
> };
> 
> struct Derived : Base {
>     Derived(int n) : Base(n + 1) {}
>     int doit(int n) { return n * data; }
> };
> 
> int doit(Base *bp) {
>     return bp->doit(1);
> }
> 
> int main(int argc, char *argv[]) {
>     Base b = Base(10);
>     Derived d = Derived(20);
>     return doit(&b) + doit(&d);
> }
> ```
>> ²To samo można osiągnąć poleceniem `«gcc -Os -fno-rtti -S -o - example.cpp | c++filt»`.

# [Flaga -fno-rtti](https://gcc.gnu.org/onlinedocs/gcc-4.4.7/gcc/C_002b_002b-Dialect-Options.html)
# [Goldbolt](https://godbolt.org/z/KoKs598WY)

```assembly
Base::doit(int):
        movl    %esi, %eax
        subl    8(%rdi), %eax                       ;return 1 - data
        ret
Derived::doit(int):
        movl    8(%rdi), %eax
        imull   %esi, %eax                          ;return data * 1
        ret
doit(Base*):
        movq    (%rdi), %rax                        ;wyciągnięcie wskaźnika na vtable
        movl    $1, %esi                            ;ustawienie 1 jako drugiego argumentu
        movq    (%rax), %rax                        ;wyciągnięcie adresu metody
        jmp     *%rax                               ;skok do metody
main:
        pushq   %rbx
        subq    $32, %rsp                           ;alokacja miejsca na stosie
        movq    %rsp, %rdi
        movq    $vtable for Base+16, (%rsp)         ;b = Base(10);
        movl    $10, 8(%rsp)
        movl    $21, 24(%rsp)                       ;d = Derived(20);
        movq    $vtable for Derived+16, 16(%rsp)
        call    doit(Base*)                         ;doit(&b)
        leaq    16(%rsp), %rdi
        movl    %eax, %ebx
        call    doit(Base*)                         ;doit(&d)
        addq    $32, %rsp                           ;czyszczenie stosu
        addl    %ebx, %eax                          ;return doit(&b) + doit(&d)
        popq    %rbx
        ret
vtable for Base:
        .quad   0
        .quad   0
        .quad   Base::doit(int)
vtable for Derived:
        .quad   0
        .quad   0
        .quad   Derived::doit(int)
```

Tak jak wspomniane jest w treści zadania, nie jesteśmy w stanie w czasie kompilacji powiedzieć, z której definicji funkcji `doit` będziemy musieli skorzystać, gdyż może być to zarówno ta pochodząca z `Base` jak i z `Derived`, w zależności od obiektu, który przyjdzie jako argument. W języku C++ problem ten jest rozwiązywany przez tworzenie **tablic metod wirtualnych**.

Obiekty tej samej klasy współdzielą taką tablicę. Zawiera ona adresy metod wirtualnych, które mają zostać wywołane w przypadku obiektu danej klasy.

Każdy obiekt otrzyma wskaźnik na swoją tablicę metod wirtualnych jako ukryte pole:

|                Wartość                | Adres | Dodatkowe informacje |
|:-------------------------------------:|:-----:|:--------------------:|
|             Adres powrotu             |   32  |    Pierwotny %rsp    |
|                   21                  |   24  |        d.data        |
| Wskaźnik na tablicę metod dla Derived |   16  |                      |
|                   10                  |   8   |        b.data        |
|   Wskaźnik na tablicę metod dla Base  |   0   |                      |
|             Adres powrotu             |   -8  |                      |

Kompilator umieścił wskaźniki na tablice metod na początku obiektów.

Procedura `doit` wyciągnie z wskaźnika danego obiektu adres metody, do której następnie skoczy pozostawiając swój wskaźnik jako pierwszy, niejawny argument. Na jego podstawie poszczególne metody wiedzą, gdzie w pamięci znajduje się zmienna `data`.