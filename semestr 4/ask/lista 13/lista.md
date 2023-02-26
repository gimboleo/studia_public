# ASK INSTANT II

## WYSTARCZY ZALAĆ WRZĄTKIEM

---

### Zadanie 1

![](https://i.imgur.com/1GomI2o.png)

> Profilowanie programu polega na uruchomieniu wersji programu, w której został włączony kod instrumentacji, aby określić, ile czasu wymagają różne części programu. Może to być bardzo przydatne do identyfikacji części programu, na których powinniśmy się skoncentrować w naszych wysiłkach optymalizacyjnych.
Jedną z mocnych stron profilowania jest to, że można je przeprowadzić podczas uruchamiania rzeczywistego programu na realistycznych danych porównawczych.
Systemy uniksowe udostępniają program do profilowania gprof. Ten program generuje dwie formy informacji. Po pierwsze, określa, ile czasu procesora poświęcono na każdą z funkcji w programie. Po drugie, oblicza liczbę wywołań każdej funkcji, skategoryzowaną według tego, która funkcja wykonuje wywołanie. Obie formy informacji mogą być bardzo przydatne.
Czasy dają poczucie względnego znaczenia różnych funkcji w określaniu całkowitego czasu działania. Informacje o wywołaniu pozwalają nam zrozumieć dynamiczne zachowanie programu.

> Płaski profil składa się z listy wszystkich procedur, które są wywoływane podczas wykonywania programu, z liczbą ich wywołań i liczbą sekund czasu wykonania, za które same są odpowiedzialne.
Procedury są wymienione w kolejności malejącej czasu wykonania.
Dostępna jest również lista procedur, które nigdy nie są wywoływane podczas wykonywania programu, aby sprawdzić, czy nic ważnego nie zostało pominięte przez to wykonanie.
Płaski profil daje szybki przegląd używanych procedur i pokazuje procedury, które same są odpowiedzialne za dużą część czasu wykonania.
W praktyce ten profil zwykle pokazuje, że żadna pojedyncza funkcja nie jest w przeważającej mierze odpowiedzialna za całkowity czas trwania programu.
Zauważ, że dla tego profilu poszczególne czasy sumują się do całkowitego czasu wykonania.

> Główne wpisy profilu wykresu wywołań to wpisy z płaskiego profilu, powiększone o czas propagowany do każdej procedury od jej potomków.
Profil ten jest posortowany według sumy czasu samej procedury plus czasu odziedziczonego po jego potomkach.
Profil pokazuje, które z podprogramów wyższego poziomu spędzają dużą część całkowitego czasu wykonania w podprogramach, które wywołują. Dla każdej rutyny pokazujemy ilość czasu przeznaczoną przez każde dziecko na rutynę, która obejmuje czas dla samego dziecka i dla potomków dziecka (a tym samym potomków rutyny). Pokazujemy również procent, jaki te czasy reprezentują w całkowitym czasie przypadającym na dziecko.
Podobnie, rodzice każdej rutyny są wymienieni, wraz z czasem i procentem całkowitego czasu rutyny, przekazywanej do każdego z nich.

> ![](https://i.imgur.com/UbPCf55.png)

> Prosty schemat zliczania interwałów, w którym skompilowany program utrzymuje licznik dla każdej funkcji, rejestrując czas spędzony na wykonywaniu tej funkcji. System operacyjny powoduje przerywanie programu w regularnych odstępach czasu δ. Typowe wartości δ mieszczą się w zakresie od 1,0 do 10,0 milisekund. Następnie określa, jaką funkcję program wykonywał w momencie wystąpienia przerwania i zwiększa licznik dla tej funkcji o δ.

### Zadanie 2

![](https://i.imgur.com/MGEdkmp.png)

Flow programu:
Słowo przeczytane z pliku -> słowo zamienione na lowercase -> hashowanie słów -> każdy kubełek w hashu jest linked list -> program skanuje listę i sprawdza czy zawiera wpis, jeśli jest to zwiększa count, jeśli nie ma to dodaje -> sort po liczbie wpisów

Funkcje:
Quick 0 - Insertion Sort
Quick 1 - Quicksort

Hash 0 - Hashowanie przez dodawanie kodów ASCII i wzięcie modulo
Hash 1 - Hashowanie przez dodawanie kodów ASCII z modulo na końcu
Hash 2 - Hashowanie z XORem

Find 0 - Rekurencyjne przechodzenie listy z dodawaniem na koniec listy
Find 1 - Iteracyjne przechodzenie list z dodawaniem na początek list
Find 2 - Iteracyjne przechodzenie list z dodawaniem na koniec listy

Lower 0 - O(n^2) bo używa strlen w każdej iteracji
Lower 1 - O(n) bo używa strlen tylko raz

SIZE - rozmiar hashmapy

```
 ✘ gimboleo@gimboleo-BOHK-WAX9X  ~/Pulpit/ask22_lista_13  make gprof 
./dictionary-pg -file shakespeare.txt -size 1021 -hash 0 -quick 0 \
        -find 0 -lower 0 -verbose 1 -ngram 2
verbose 1
size    1021
hash    0
lower   0
find    0
ngram   2
quicksort       0
file    shakespeare.txt
N-gram size 2
Lower case function lower1
Hash function h_mod
Find element function find_ele_rec
1892    'i am'
965028 n-grams, 363039 unique, 266018 singletons.  Most common (1892) = 'i am'.  Longest (1 have length 32) = 'honorificabilitudinitatibus thou'
Total time = 143.461978 seconds
gprof -b dictionary-pg gmon.out
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls   s/call   s/call  name    
 95.02    133.67   133.67        1   133.67   133.67  sort_words
  4.99    140.69     7.02   965027     0.00     0.00  find_ele_rec
  0.11    140.85     0.16   965027     0.00     0.00  lower1
  0.04    140.91     0.06   965027     0.00     0.00  h_mod
  0.02    140.94     0.04   965028     0.00     0.00  get_token
  0.01    140.95     0.01   965027     0.00     0.00  insert_string
  0.00    140.96     0.01   965029     0.00     0.00  get_word
  0.00    140.96     0.01   363039     0.00     0.00  save_string
  0.00    140.96     0.00   363039     0.00     0.00  new_ele
  0.00    140.96     0.00        8     0.00     0.00  find_option
  0.00    140.96     0.00        7     0.00     0.00  add_int_option
  0.00    140.96     0.00        1     0.00     0.00  add_string_option
  0.00    140.96     0.00        1     0.00     0.00  parse_options
  0.00    140.96     0.00        1     0.00     0.00  show_options
  0.00    140.96     0.00        1     0.00   140.96  word_freq


                        Call graph


granularity: each sample hit covers 2 byte(s) for 0.01% of 140.96 seconds

index % time    self  children    called     name
                0.00  140.96       1/1           main [2]
[1]    100.0    0.00  140.96       1         word_freq [1]
              133.67    0.00       1/1           sort_words [3]
                0.01    7.24  965027/965027      insert_string [4]
                0.04    0.01  965028/965028      get_token [8]
-----------------------------------------------
                                                 <spontaneous>
[2]    100.0    0.00  140.96                 main [2]
                0.00  140.96       1/1           word_freq [1]
                0.00    0.00       7/7           add_int_option [13]
                0.00    0.00       1/1           add_string_option [14]
                0.00    0.00       1/1           parse_options [15]
                0.00    0.00       1/1           show_options [16]
-----------------------------------------------
              133.67    0.00       1/1           word_freq [1]
[3]     94.8  133.67    0.00       1         sort_words [3]
-----------------------------------------------
                0.01    7.24  965027/965027      word_freq [1]
[4]      5.1    0.01    7.24  965027         insert_string [4]
                7.02    0.01  965027/965027      find_ele_rec [5]
                0.16    0.00  965027/965027      lower1 [6]
                0.06    0.00  965027/965027      h_mod [7]
-----------------------------------------------
                             95820673             find_ele_rec [5]
                7.02    0.01  965027/965027      insert_string [4]
[5]      5.0    7.02    0.01  965027+95820673 find_ele_rec [5]
                0.01    0.00  363039/363039      save_string [10]
                0.00    0.00  363039/363039      new_ele [11]
                             95820673             find_ele_rec [5]
-----------------------------------------------
                0.16    0.00  965027/965027      insert_string [4]
[6]      0.1    0.16    0.00  965027         lower1 [6]
-----------------------------------------------
                0.06    0.00  965027/965027      insert_string [4]
[7]      0.0    0.06    0.00  965027         h_mod [7]
-----------------------------------------------
                0.04    0.01  965028/965028      word_freq [1]
[8]      0.0    0.04    0.01  965028         get_token [8]
                0.01    0.00  965029/965029      get_word [9]
-----------------------------------------------
                0.01    0.00  965029/965029      get_token [8]
[9]      0.0    0.01    0.00  965029         get_word [9]
-----------------------------------------------
                0.01    0.00  363039/363039      find_ele_rec [5]
[10]     0.0    0.01    0.00  363039         save_string [10]
-----------------------------------------------
                0.00    0.00  363039/363039      find_ele_rec [5]
[11]     0.0    0.00    0.00  363039         new_ele [11]
-----------------------------------------------
                0.00    0.00       8/8           parse_options [15]
[12]     0.0    0.00    0.00       8         find_option [12]
-----------------------------------------------
                0.00    0.00       7/7           main [2]
[13]     0.0    0.00    0.00       7         add_int_option [13]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[14]     0.0    0.00    0.00       1         add_string_option [14]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[15]     0.0    0.00    0.00       1         parse_options [15]
                0.00    0.00       8/8           find_option [12]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[16]     0.0    0.00    0.00       1         show_options [16]
-----------------------------------------------


Index by function name

  [13] add_int_option          [9] get_word               [15] parse_options
  [14] add_string_option       [7] h_mod                  [10] save_string
   [5] find_ele_rec            [4] insert_string          [16] show_options
  [12] find_option (options.c) [6] lower1                  [3] sort_words
   [8] get_token              [11] new_ele (dictionary.c)  [1] word_freq
```

```
 ✘ gimboleo@gimboleo-BOHK-WAX9X  ~/Pulpit/ask22_lista_13  make gprof QUICK=1
./dictionary-pg -file shakespeare.txt -size 1021 -hash 0 -quick 1 \
        -find 0 -lower 0 -verbose 1 -ngram 2
verbose 1
size    1021
hash    0
lower   0
find    0
ngram   2
quicksort       1
file    shakespeare.txt
N-gram size 2
Lower case function lower1
Hash function h_mod
Find element function find_ele_rec
1892    'i am'
965028 n-grams, 363039 unique, 266018 singletons.  Most common (1892) = 'i am'.  Longest (1 have length 32) = 'honorificabilitudinitatibus thou'
Total time = 10.307900 seconds
gprof -b dictionary-pg gmon.out
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls   s/call   s/call  name    
 95.21      6.60     6.60   965027     0.00     0.00  find_ele_rec
  1.45      6.70     0.10   965027     0.00     0.00  lower1
  0.72      6.75     0.05   965028     0.00     0.00  get_token
  0.72      6.80     0.05   965027     0.00     0.00  insert_string
  0.72      6.85     0.05        1     0.05     0.05  sort_words
  0.58      6.89     0.04   965027     0.00     0.00  h_mod
  0.58      6.93     0.04                             compare_ele
  0.22      6.94     0.02   363039     0.00     0.00  save_string
  0.00      6.94     0.00   965029     0.00     0.00  get_word
  0.00      6.94     0.00   363039     0.00     0.00  new_ele
  0.00      6.94     0.00        8     0.00     0.00  find_option
  0.00      6.94     0.00        7     0.00     0.00  add_int_option
  0.00      6.94     0.00        1     0.00     0.00  add_string_option
  0.00      6.94     0.00        1     0.00     0.00  parse_options
  0.00      6.94     0.00        1     0.00     0.00  show_options
  0.00      6.94     0.00        1     0.00     6.90  word_freq


                        Call graph


granularity: each sample hit covers 2 byte(s) for 0.14% of 6.94 seconds

index % time    self  children    called     name
                0.00    6.90       1/1           main [2]
[1]     99.4    0.00    6.90       1         word_freq [1]
                0.05    6.75  965027/965027      insert_string [3]
                0.05    0.00  965028/965028      get_token [6]
                0.05    0.00       1/1           sort_words [7]
-----------------------------------------------
                                                 <spontaneous>
[2]     99.4    0.00    6.90                 main [2]
                0.00    6.90       1/1           word_freq [1]
                0.00    0.00       7/7           add_int_option [14]
                0.00    0.00       1/1           add_string_option [15]
                0.00    0.00       1/1           parse_options [16]
                0.00    0.00       1/1           show_options [17]
-----------------------------------------------
                0.05    6.75  965027/965027      word_freq [1]
[3]     98.0    0.05    6.75  965027         insert_string [3]
                6.60    0.02  965027/965027      find_ele_rec [4]
                0.10    0.00  965027/965027      lower1 [5]
                0.04    0.00  965027/965027      h_mod [8]
-----------------------------------------------
                             95820673             find_ele_rec [4]
                6.60    0.02  965027/965027      insert_string [3]
[4]     95.2    6.60    0.02  965027+95820673 find_ele_rec [4]
                0.02    0.00  363039/363039      save_string [10]
                0.00    0.00  363039/363039      new_ele [12]
                             95820673             find_ele_rec [4]
-----------------------------------------------
                0.10    0.00  965027/965027      insert_string [3]
[5]      1.4    0.10    0.00  965027         lower1 [5]
-----------------------------------------------
                0.05    0.00  965028/965028      word_freq [1]
[6]      0.7    0.05    0.00  965028         get_token [6]
                0.00    0.00  965029/965029      get_word [11]
-----------------------------------------------
                0.05    0.00       1/1           word_freq [1]
[7]      0.7    0.05    0.00       1         sort_words [7]
-----------------------------------------------
                0.04    0.00  965027/965027      insert_string [3]
[8]      0.6    0.04    0.00  965027         h_mod [8]
-----------------------------------------------
                                                 <spontaneous>
[9]      0.6    0.04    0.00                 compare_ele [9]
-----------------------------------------------
                0.02    0.00  363039/363039      find_ele_rec [4]
[10]     0.2    0.02    0.00  363039         save_string [10]
-----------------------------------------------
                0.00    0.00  965029/965029      get_token [6]
[11]     0.0    0.00    0.00  965029         get_word [11]
-----------------------------------------------
                0.00    0.00  363039/363039      find_ele_rec [4]
[12]     0.0    0.00    0.00  363039         new_ele [12]
-----------------------------------------------
                0.00    0.00       8/8           parse_options [16]
[13]     0.0    0.00    0.00       8         find_option [13]
-----------------------------------------------
                0.00    0.00       7/7           main [2]
[14]     0.0    0.00    0.00       7         add_int_option [14]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[15]     0.0    0.00    0.00       1         add_string_option [15]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[16]     0.0    0.00    0.00       1         parse_options [16]
                0.00    0.00       8/8           find_option [13]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[17]     0.0    0.00    0.00       1         show_options [17]
-----------------------------------------------


Index by function name

  [14] add_int_option         [11] get_word               [10] save_string
  [15] add_string_option       [8] h_mod                  [17] show_options
   [9] compare_ele             [3] insert_string           [7] sort_words
   [4] find_ele_rec            [5] lower1                  [1] word_freq
  [13] find_option (options.c) [12] new_ele (dictionary.c)
   [6] get_token              [16] parse_options
```

```
gimboleo@gimboleo-BOHK-WAX9X  ~/Pulpit/ask22_lista_13  make gprof QUICK=1 FIND=1
./dictionary-pg -file shakespeare.txt -size 1021 -hash 0 -quick 1 \
        -find 1 -lower 0 -verbose 1 -ngram 2
verbose 1
size    1021
hash    0
lower   0
find    1
ngram   2
quicksort       1
file    shakespeare.txt
N-gram size 2
Lower case function lower1
Hash function h_mod
Find element function find_ele_iter_f
1892    'i am'
965028 n-grams, 363039 unique, 266018 singletons.  Most common (1892) = 'i am'.  Longest (1 have length 32) = 'honorificabilitudinitatibus thou'
Total time = 14.629121 seconds
gprof -b dictionary-pg gmon.out
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls   s/call   s/call  name    
 96.56     10.63    10.63   965027     0.00     0.00  find_ele_iter_f
  1.59     10.81     0.18   965027     0.00     0.00  lower1
  0.46     10.86     0.05   965027     0.00     0.00  h_mod
  0.46     10.91     0.05                             compare_ele
  0.36     10.95     0.04   965028     0.00     0.00  get_token
  0.36     10.99     0.04   965027     0.00     0.00  insert_string
  0.36     11.03     0.04        1     0.04     0.04  sort_words
  0.05     11.03     0.01                             Strlen
  0.00     11.03     0.00   965029     0.00     0.00  get_word
  0.00     11.03     0.00   363039     0.00     0.00  new_ele
  0.00     11.03     0.00   363039     0.00     0.00  save_string
  0.00     11.03     0.00        8     0.00     0.00  find_option
  0.00     11.03     0.00        7     0.00     0.00  add_int_option
  0.00     11.03     0.00        1     0.00     0.00  add_string_option
  0.00     11.03     0.00        1     0.00     0.00  parse_options
  0.00     11.03     0.00        1     0.00     0.00  show_options
  0.00     11.03     0.00        1     0.00    10.98  word_freq


                        Call graph


granularity: each sample hit covers 2 byte(s) for 0.09% of 11.03 seconds

index % time    self  children    called     name
                0.00   10.98       1/1           main [2]
[1]     99.5    0.00   10.98       1         word_freq [1]
                0.04   10.86  965027/965027      insert_string [3]
                0.04    0.00  965028/965028      get_token [8]
                0.04    0.00       1/1           sort_words [9]
-----------------------------------------------
                                                 <spontaneous>
[2]     99.5    0.00   10.98                 main [2]
                0.00   10.98       1/1           word_freq [1]
                0.00    0.00       7/7           add_int_option [15]
                0.00    0.00       1/1           add_string_option [16]
                0.00    0.00       1/1           parse_options [17]
                0.00    0.00       1/1           show_options [18]
-----------------------------------------------
                0.04   10.86  965027/965027      word_freq [1]
[3]     98.8    0.04   10.86  965027         insert_string [3]
               10.63    0.00  965027/965027      find_ele_iter_f [4]
                0.18    0.00  965027/965027      lower1 [5]
                0.05    0.00  965027/965027      h_mod [6]
-----------------------------------------------
               10.63    0.00  965027/965027      insert_string [3]
[4]     96.4   10.63    0.00  965027         find_ele_iter_f [4]
                0.00    0.00  363039/363039      save_string [13]
                0.00    0.00  363039/363039      new_ele [12]
-----------------------------------------------
                0.18    0.00  965027/965027      insert_string [3]
[5]      1.6    0.18    0.00  965027         lower1 [5]
-----------------------------------------------
                0.05    0.00  965027/965027      insert_string [3]
[6]      0.5    0.05    0.00  965027         h_mod [6]
-----------------------------------------------
                                                 <spontaneous>
[7]      0.5    0.05    0.00                 compare_ele [7]
-----------------------------------------------
                0.04    0.00  965028/965028      word_freq [1]
[8]      0.4    0.04    0.00  965028         get_token [8]
                0.00    0.00  965029/965029      get_word [11]
-----------------------------------------------
                0.04    0.00       1/1           word_freq [1]
[9]      0.4    0.04    0.00       1         sort_words [9]
-----------------------------------------------
                                                 <spontaneous>
[10]     0.0    0.01    0.00                 Strlen [10]
-----------------------------------------------
                0.00    0.00  965029/965029      get_token [8]
[11]     0.0    0.00    0.00  965029         get_word [11]
-----------------------------------------------
                0.00    0.00  363039/363039      find_ele_iter_f [4]
[12]     0.0    0.00    0.00  363039         new_ele [12]
-----------------------------------------------
                0.00    0.00  363039/363039      find_ele_iter_f [4]
[13]     0.0    0.00    0.00  363039         save_string [13]
-----------------------------------------------
                0.00    0.00       8/8           parse_options [17]
[14]     0.0    0.00    0.00       8         find_option [14]
-----------------------------------------------
                0.00    0.00       7/7           main [2]
[15]     0.0    0.00    0.00       7         add_int_option [15]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[16]     0.0    0.00    0.00       1         add_string_option [16]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[17]     0.0    0.00    0.00       1         parse_options [17]
                0.00    0.00       8/8           find_option [14]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[18]     0.0    0.00    0.00       1         show_options [18]
-----------------------------------------------


Index by function name

  [10] Strlen                  [8] get_token              [17] parse_options
  [15] add_int_option         [11] get_word               [13] save_string
  [16] add_string_option       [6] h_mod                  [18] show_options
   [7] compare_ele             [3] insert_string           [9] sort_words
   [4] find_ele_iter_f         [5] lower1                  [1] word_freq
  [14] find_option (options.c) [12] new_ele (dictionary.c)
```

```
gimboleo@gimboleo-BOHK-WAX9X  ~/Pulpit/ask22_lista_13  make gprof QUICK=1 FIND=1 SIZE=119993
./dictionary-pg -file shakespeare.txt -size 119993 -hash 0 -quick 1 \
        -find 1 -lower 0 -verbose 1 -ngram 2
verbose 1
size    119993
hash    0
lower   0
find    1
ngram   2
quicksort       1
file    shakespeare.txt
N-gram size 2
Lower case function lower1
Hash function h_mod
Find element function find_ele_iter_f
1892    'i am'
965028 n-grams, 363039 unique, 266018 singletons.  Most common (1892) = 'i am'.  Longest (1 have length 32) = 'honorificabilitudinitatibus thou'
Total time = 0.725058 seconds
gprof -b dictionary-pg gmon.out
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls  ms/call  ms/call  name    
 29.15      0.16     0.16   965027     0.00     0.00  find_ele_iter_f
 25.51      0.30     0.14   965027     0.00     0.00  lower1
 14.57      0.38     0.08                             compare_ele
  9.11      0.43     0.05   965027     0.00     0.00  h_mod
  9.11      0.48     0.05   965027     0.00     0.00  insert_string
  7.29      0.52     0.04   965028     0.00     0.00  get_token
  3.64      0.54     0.02   363039     0.00     0.00  new_ele
  1.82      0.55     0.01        1    10.02    10.02  sort_words
  0.00      0.55     0.00   965029     0.00     0.00  get_word
  0.00      0.55     0.00   363039     0.00     0.00  save_string
  0.00      0.55     0.00        8     0.00     0.00  find_option
  0.00      0.55     0.00        7     0.00     0.00  add_int_option
  0.00      0.55     0.00        1     0.00     0.00  add_string_option
  0.00      0.55     0.00        1     0.00     0.00  parse_options
  0.00      0.55     0.00        1     0.00     0.00  show_options
  0.00      0.55     0.00        1     0.00   470.95  word_freq


                        Call graph


granularity: each sample hit covers 2 byte(s) for 1.81% of 0.55 seconds

index % time    self  children    called     name
                0.00    0.47       1/1           main [2]
[1]     85.5    0.00    0.47       1         word_freq [1]
                0.05    0.37  965027/965027      insert_string [3]
                0.04    0.00  965028/965028      get_token [8]
                0.01    0.00       1/1           sort_words [10]
-----------------------------------------------
                                                 <spontaneous>
[2]     85.5    0.00    0.47                 main [2]
                0.00    0.47       1/1           word_freq [1]
                0.00    0.00       7/7           add_int_option [14]
                0.00    0.00       1/1           add_string_option [15]
                0.00    0.00       1/1           parse_options [16]
                0.00    0.00       1/1           show_options [17]
-----------------------------------------------
                0.05    0.37  965027/965027      word_freq [1]
[3]     76.4    0.05    0.37  965027         insert_string [3]
                0.16    0.02  965027/965027      find_ele_iter_f [4]
                0.14    0.00  965027/965027      lower1 [5]
                0.05    0.00  965027/965027      h_mod [7]
-----------------------------------------------
                0.16    0.02  965027/965027      insert_string [3]
[4]     32.7    0.16    0.02  965027         find_ele_iter_f [4]
                0.02    0.00  363039/363039      new_ele [9]
                0.00    0.00  363039/363039      save_string [12]
-----------------------------------------------
                0.14    0.00  965027/965027      insert_string [3]
[5]     25.5    0.14    0.00  965027         lower1 [5]
-----------------------------------------------
                                                 <spontaneous>
[6]     14.5    0.08    0.00                 compare_ele [6]
-----------------------------------------------
                0.05    0.00  965027/965027      insert_string [3]
[7]      9.1    0.05    0.00  965027         h_mod [7]
-----------------------------------------------
                0.04    0.00  965028/965028      word_freq [1]
[8]      7.3    0.04    0.00  965028         get_token [8]
                0.00    0.00  965029/965029      get_word [11]
-----------------------------------------------
                0.02    0.00  363039/363039      find_ele_iter_f [4]
[9]      3.6    0.02    0.00  363039         new_ele [9]
-----------------------------------------------
                0.01    0.00       1/1           word_freq [1]
[10]     1.8    0.01    0.00       1         sort_words [10]
-----------------------------------------------
                0.00    0.00  965029/965029      get_token [8]
[11]     0.0    0.00    0.00  965029         get_word [11]
-----------------------------------------------
                0.00    0.00  363039/363039      find_ele_iter_f [4]
[12]     0.0    0.00    0.00  363039         save_string [12]
-----------------------------------------------
                0.00    0.00       8/8           parse_options [16]
[13]     0.0    0.00    0.00       8         find_option [13]
-----------------------------------------------
                0.00    0.00       7/7           main [2]
[14]     0.0    0.00    0.00       7         add_int_option [14]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[15]     0.0    0.00    0.00       1         add_string_option [15]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[16]     0.0    0.00    0.00       1         parse_options [16]
                0.00    0.00       8/8           find_option [13]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[17]     0.0    0.00    0.00       1         show_options [17]
-----------------------------------------------


Index by function name

  [14] add_int_option         [11] get_word               [12] save_string
  [15] add_string_option       [7] h_mod                  [17] show_options
   [6] compare_ele             [3] insert_string          [10] sort_words
   [4] find_ele_iter_f         [5] lower1                  [1] word_freq
  [13] find_option (options.c) [9] new_ele (dictionary.c)
   [8] get_token              [16] parse_options
```

```
 gimboleo@gimboleo-BOHK-WAX9X  ~/Pulpit/ask22_lista_13  make gprof QUICK=1 FIND=1 SIZE=199999 HASH=2
./dictionary-pg -file shakespeare.txt -size 199999 -hash 2 -quick 1 \
        -find 1 -lower 0 -verbose 1 -ngram 2
verbose 1
size    199999
hash    2
lower   0
find    1
ngram   2
quicksort       1
file    shakespeare.txt
N-gram size 2
Lower case function lower1
Hash function h_xor
Find element function find_ele_iter_f
1892    'i am'
965028 n-grams, 363039 unique, 266018 singletons.  Most common (1892) = 'i am'.  Longest (1 have length 32) = 'honorificabilitudinitatibus thou'
Total time = 0.735289 seconds
gprof -b dictionary-pg gmon.out
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls  ms/call  ms/call  name    
 24.09      0.13     0.13   965027     0.00     0.00  lower1
 21.20      0.24     0.11   965027     0.00     0.00  find_ele_iter_f
 19.27      0.34     0.10                             compare_ele
 13.49      0.41     0.07   965027     0.00     0.00  insert_string
  5.78      0.44     0.03   965028     0.00     0.00  get_token
  4.82      0.46     0.03   363039     0.00     0.00  save_string
  3.85      0.48     0.02   965027     0.00     0.00  h_xor
  3.85      0.50     0.02        1    20.04    20.04  sort_words
  1.93      0.51     0.01   363039     0.00     0.00  new_ele
  1.93      0.52     0.01                             Strlen
  0.00      0.52     0.00   965029     0.00     0.00  get_word
  0.00      0.52     0.00        8     0.00     0.00  find_option
  0.00      0.52     0.00        7     0.00     0.00  add_int_option
  0.00      0.52     0.00        1     0.00     0.00  add_string_option
  0.00      0.52     0.00        1     0.00     0.00  parse_options
  0.00      0.52     0.00        1     0.00     0.00  show_options
  0.00      0.52     0.00        1     0.00   410.83  word_freq


                        Call graph


granularity: each sample hit covers 2 byte(s) for 1.92% of 0.52 seconds

index % time    self  children    called     name
                0.00    0.41       1/1           main [2]
[1]     78.8    0.00    0.41       1         word_freq [1]
                0.07    0.29  965027/965027      insert_string [3]
                0.03    0.00  965028/965028      get_token [7]
                0.02    0.00       1/1           sort_words [10]
-----------------------------------------------
                                                 <spontaneous>
[2]     78.8    0.00    0.41                 main [2]
                0.00    0.41       1/1           word_freq [1]
                0.00    0.00       7/7           add_int_option [15]
                0.00    0.00       1/1           add_string_option [16]
                0.00    0.00       1/1           parse_options [17]
                0.00    0.00       1/1           show_options [18]
-----------------------------------------------
                0.07    0.29  965027/965027      word_freq [1]
[3]     69.2    0.07    0.29  965027         insert_string [3]
                0.11    0.04  965027/965027      find_ele_iter_f [4]
                0.13    0.00  965027/965027      lower1 [5]
                0.02    0.00  965027/965027      h_xor [9]
-----------------------------------------------
                0.11    0.04  965027/965027      insert_string [3]
[4]     27.9    0.11    0.04  965027         find_ele_iter_f [4]
                0.03    0.00  363039/363039      save_string [8]
                0.01    0.00  363039/363039      new_ele [11]
-----------------------------------------------
                0.13    0.00  965027/965027      insert_string [3]
[5]     24.0    0.13    0.00  965027         lower1 [5]
-----------------------------------------------
                                                 <spontaneous>
[6]     19.2    0.10    0.00                 compare_ele [6]
-----------------------------------------------
                0.03    0.00  965028/965028      word_freq [1]
[7]      5.8    0.03    0.00  965028         get_token [7]
                0.00    0.00  965029/965029      get_word [13]
-----------------------------------------------
                0.03    0.00  363039/363039      find_ele_iter_f [4]
[8]      4.8    0.03    0.00  363039         save_string [8]
-----------------------------------------------
                0.02    0.00  965027/965027      insert_string [3]
[9]      3.8    0.02    0.00  965027         h_xor [9]
-----------------------------------------------
                0.02    0.00       1/1           word_freq [1]
[10]     3.8    0.02    0.00       1         sort_words [10]
-----------------------------------------------
                0.01    0.00  363039/363039      find_ele_iter_f [4]
[11]     1.9    0.01    0.00  363039         new_ele [11]
-----------------------------------------------
                                                 <spontaneous>
[12]     1.9    0.01    0.00                 Strlen [12]
-----------------------------------------------
                0.00    0.00  965029/965029      get_token [7]
[13]     0.0    0.00    0.00  965029         get_word [13]
-----------------------------------------------
                0.00    0.00       8/8           parse_options [17]
[14]     0.0    0.00    0.00       8         find_option [14]
-----------------------------------------------
                0.00    0.00       7/7           main [2]
[15]     0.0    0.00    0.00       7         add_int_option [15]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[16]     0.0    0.00    0.00       1         add_string_option [16]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[17]     0.0    0.00    0.00       1         parse_options [17]
                0.00    0.00       8/8           find_option [14]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[18]     0.0    0.00    0.00       1         show_options [18]
-----------------------------------------------


Index by function name

  [12] Strlen                  [7] get_token              [17] parse_options
  [15] add_int_option         [13] get_word                [8] save_string
  [16] add_string_option       [9] h_xor                  [18] show_options
   [6] compare_ele             [3] insert_string          [10] sort_words
   [4] find_ele_iter_f         [5] lower1                  [1] word_freq
  [14] find_option (options.c) [11] new_ele (dictionary.c)
```

```
 gimboleo@gimboleo-BOHK-WAX9X  ~/Pulpit/ask22_lista_13  make gprof QUICK=1 FIND=1 SIZE=199999 HASH=2 LOWER=1
./dictionary-pg -file shakespeare.txt -size 199999 -hash 2 -quick 1 \
        -find 1 -lower 1 -verbose 1 -ngram 2
verbose 1
size    199999
hash    2
lower   1
find    1
ngram   2
quicksort       1
file    shakespeare.txt
N-gram size 2
Lower case function lower2
Hash function h_xor
Find element function find_ele_iter_f
1892    'i am'
965028 n-grams, 363039 unique, 266018 singletons.  Most common (1892) = 'i am'.  Longest (1 have length 32) = 'honorificabilitudinitatibus thou'
Total time = 0.542261 seconds
gprof -b dictionary-pg gmon.out
Flat profile:

Each sample counts as 0.01 seconds.
  %   cumulative   self              self     total           
 time   seconds   seconds    calls  ms/call  ms/call  name    
 40.82      0.11     0.11   965027     0.00     0.00  find_ele_iter_f
 22.27      0.17     0.06   965027     0.00     0.00  insert_string
 18.56      0.22     0.05                             compare_ele
  3.71      0.23     0.01   965028     0.00     0.00  get_token
  3.71      0.24     0.01   965027     0.00     0.00  lower2
  3.71      0.25     0.01   363039     0.00     0.00  new_ele
  3.71      0.26     0.01        1    10.02    10.02  sort_words
  3.71      0.27     0.01                             h_add
  0.00      0.27     0.00   965029     0.00     0.00  get_word
  0.00      0.27     0.00   965027     0.00     0.00  h_xor
  0.00      0.27     0.00   363039     0.00     0.00  save_string
  0.00      0.27     0.00        8     0.00     0.00  find_option
  0.00      0.27     0.00        7     0.00     0.00  add_int_option
  0.00      0.27     0.00        1     0.00     0.00  add_string_option
  0.00      0.27     0.00        1     0.00     0.00  parse_options
  0.00      0.27     0.00        1     0.00     0.00  show_options
  0.00      0.27     0.00        1     0.00   210.42  word_freq


                        Call graph


granularity: each sample hit covers 2 byte(s) for 3.70% of 0.27 seconds

index % time    self  children    called     name
                0.00    0.21       1/1           main [2]
[1]     77.8    0.00    0.21       1         word_freq [1]
                0.06    0.13  965027/965027      insert_string [3]
                0.01    0.00  965028/965028      get_token [6]
                0.01    0.00       1/1           sort_words [9]
-----------------------------------------------
                                                 <spontaneous>
[2]     77.8    0.00    0.21                 main [2]
                0.00    0.21       1/1           word_freq [1]
                0.00    0.00       7/7           add_int_option [15]
                0.00    0.00       1/1           add_string_option [16]
                0.00    0.00       1/1           parse_options [17]
                0.00    0.00       1/1           show_options [18]
-----------------------------------------------
                0.06    0.13  965027/965027      word_freq [1]
[3]     70.4    0.06    0.13  965027         insert_string [3]
                0.11    0.01  965027/965027      find_ele_iter_f [4]
                0.01    0.00  965027/965027      lower2 [7]
                0.00    0.00  965027/965027      h_xor [12]
-----------------------------------------------
                0.11    0.01  965027/965027      insert_string [3]
[4]     44.4    0.11    0.01  965027         find_ele_iter_f [4]
                0.01    0.00  363039/363039      new_ele [8]
                0.00    0.00  363039/363039      save_string [13]
-----------------------------------------------
                                                 <spontaneous>
[5]     18.5    0.05    0.00                 compare_ele [5]
-----------------------------------------------
                0.01    0.00  965028/965028      word_freq [1]
[6]      3.7    0.01    0.00  965028         get_token [6]
                0.00    0.00  965029/965029      get_word [11]
-----------------------------------------------
                0.01    0.00  965027/965027      insert_string [3]
[7]      3.7    0.01    0.00  965027         lower2 [7]
-----------------------------------------------
                0.01    0.00  363039/363039      find_ele_iter_f [4]
[8]      3.7    0.01    0.00  363039         new_ele [8]
-----------------------------------------------
                0.01    0.00       1/1           word_freq [1]
[9]      3.7    0.01    0.00       1         sort_words [9]
-----------------------------------------------
                                                 <spontaneous>
[10]     3.7    0.01    0.00                 h_add [10]
-----------------------------------------------
                0.00    0.00  965029/965029      get_token [6]
[11]     0.0    0.00    0.00  965029         get_word [11]
-----------------------------------------------
                0.00    0.00  965027/965027      insert_string [3]
[12]     0.0    0.00    0.00  965027         h_xor [12]
-----------------------------------------------
                0.00    0.00  363039/363039      find_ele_iter_f [4]
[13]     0.0    0.00    0.00  363039         save_string [13]
-----------------------------------------------
                0.00    0.00       8/8           parse_options [17]
[14]     0.0    0.00    0.00       8         find_option [14]
-----------------------------------------------
                0.00    0.00       7/7           main [2]
[15]     0.0    0.00    0.00       7         add_int_option [15]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[16]     0.0    0.00    0.00       1         add_string_option [16]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[17]     0.0    0.00    0.00       1         parse_options [17]
                0.00    0.00       8/8           find_option [14]
-----------------------------------------------
                0.00    0.00       1/1           main [2]
[18]     0.0    0.00    0.00       1         show_options [18]
-----------------------------------------------


Index by function name

  [15] add_int_option         [11] get_word               [17] parse_options
  [16] add_string_option      [10] h_add                  [13] save_string
   [5] compare_ele            [12] h_xor                  [18] show_options
   [4] find_ele_iter_f         [3] insert_string           [9] sort_words
  [14] find_option (options.c) [7] lower2                  [1] word_freq
   [6] get_token               [8] new_ele (dictionary.c)
```

### Zadanie 3

![](https://i.imgur.com/egoz39p.png)

![](https://i.imgur.com/JnupPS4.png)

strtok:
dzieli string na kolejne tokeny względem zadanych znaków oddzielających.
strtok_r:
tak jak strtok, ale nie korzysta ze statycznego bufora. Dzięki temu ta funkcja 
nadej się do wielowątkowości.
W zadaniu służy do wyciągania kolejnych słów z pliku tekstowego.

Optymalizować można zmniejszajać liczbe malloców alokujać odrazu duża tablice stringów zamiast kazdego stringa osobno.