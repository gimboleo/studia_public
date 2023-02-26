> **Zadanie 9.** Liczba w formacie `BCD` *(ang. binary coded decimal)* jest reprezentowana przez liczbę binarną, której kolejne półbajty *(ang. nibble)* kodują cyfry dziesiętne od $0$ do $9$. Napisz w asemblerze `x86-64` ciało funkcji `«bcd_add»`, która dodaje dwie $16$-cyfrowe liczby przekazane w rejestrach `%rdi` i `%rsi`, a wynik zwróci w rejestrze `%rax`. Nie można używać instrukcji mnożenia i dzielenia.
>> **Źródło:** Zadanie 100 z [[1](https://ia601602.us.archive.org/29/items/B-001-001-251/B-001-001-251.pdf), 7.1.3].

# [Instrukcja movabsq](https://stackoverflow.com/questions/40315803/difference-between-movq-and-movabsq-in-x86-64)

Mamy $x = (x_{15}...x_0)_{16} \ \ \ y = (y_{15}...y_0)_{16}$, gdzie $x_i, y_i$ to kolejne półbajty reprezentujące jedną cyfrę. Chcemy obliczyć $u = (u_{15}...u_0)_{10} = (x_{15}...x_0)_{10} + (y_{15}...y_0)_{10}$, gdzie $x_i, y_i$ to kolejne cyfry.

Zauważmy, że dodawanie binarne półbajtów prawie daje dobre rowiązanie:
- Jeżeli suma dwóch cyfr nie przekracza $9$, wynik jest w porządku.
- Jeżeli suma jest większa od $9$, w półbajcie otrzymamy za duży wynik, którego część powinna zostać przeniesiona. Aby uzyskać odpowiednią cyfrę należy do wyniku dodać $6$ - wtedy w obecnym półbajcie zostanie ostatnia cyfra dodawania, a reszta zostanie przeniesiona do następnego:
  - $10 + 6 = 16 = 10_{16} =_{chop} 0_{16}$
  - $11 + 6 = 17 = 11_{16} =_{chop} 1_{16}$
  - $12 + 6 = 18 = 12_{16} =_{chop} 2_{16}$
  - $13 + 6 = 19 = 13_{16} =_{chop} 3_{16}$
  - $14 + 6 = 20 = 14_{16} =_{chop} 4_{16}$
  - $15 + 6 = 21 = 15_{16} =_{chop} 5_{16}$
  - $16 + 6 = 22 = 16_{16} =_{chop} 6_{16}$
  - $17 + 6 = 23 = 17_{16} =_{chop} 7_{16}$
  - $18 + 6 = 24 = 18_{16} =_{chop} 8_{16}$
  - $19 + 6 = 25 = 19_{16} =_{chop} 9_{16}$

```c
uint64_t bcd_add(uint64_t x, uint64_t y) {
    uint64_t t1 = x + 0x6666666666666666;
    uint64_t t2 = t1 + y;
    uint64_t t3 = t1 ^ y;
    uint64_t t4 = t2 ^ t3;
    uint64_t t5 = ~t4 & 0x11111110;
    uint64_t t6 = (t5 >> 2) | (t5 >> 3);
    return t2 - t6;
}
```

- Dodajmy do każdego półbajtu $x$ liczbę $6$ - wiemy, że żaden półbajt nie wygeneruje przeniesienia, ponieważ każdy zawiera liczby mniejsze od $10$. Wynik tej operacji przechowajmy w $t_1$.
- Po dodaniu do $t_1$ liczby $y$ ($t_2$) półbajt wygeneruje przeniesienie wtedy i tylko wtedy, gdy suma odpowiadających mu cyfr z $x$ i $y$ powoduje przeniesienie ($9 + 6 = 15 = F_{16}$, co mieści się w jednym półbajcie. Suma $6$ z liczbą większą od $9$ już się nie zmieści). Zatem $t_2$ zawiera dobry wynik dla sum generujących przeniesienia, od reszty trzeba odjąć dodaną wcześniej liczbę $6$.
- W $t_3$ wykonujemy dodawanie $x + y$ ignorując przeniesienia za pomocą `XOR`'a.
- Zauważmy, że $t_2$ i $t_3$ różnią się na dokładnie tych bitach, które otrzymały przeniesienie. Zatem w $t_4$ mamy informację o tym, które bajty otrzymują przeniesienie.
- Negacja z $t_4$ będzie nam mówiła, na których bitach nie znalazło się przeniesienie. Korzystając z maski $(0001 \ 0001 \ ... \ 0001 \ 0000)_2$ otrzymujemy informację, które półbajty nie otrzymały przeniesienia od swoich sąsiadów. Od takich sąsiadów należy odjąć $6$ ($t_5$).
- Każdy zapalony bit z $t_5$ za pomocą przesunięć bitowych w prawo zamieniamy na liczbę $0110_2 = 6_{10}$ na bitach sąsiada, który nie wygenerował przeniesienia ($t_6$).
- Odejmując $t_6$ od $t_2$ otrzymujemy właściwy wynik.



```assembly
bcd_add:    movabsq $0x6666666666666666, %rax
            movabsq $0x1111111111111110, %rdx
            addq    %rax, %rdi
            leaq    (%rdi, %rsi), %rax
            xorq    %rsi, %rdi
            xorq    %rax, %rdi
            notq    %rdi
            andq    %rdx, %rdi
            movq    %rdi, %rdx
            shrq    $3, %rdi
            shrq    $2, %rdx
            orq     %rdi, %rdx
            subq    %rdx, %rax
            ret
```