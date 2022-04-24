> **Zadanie 1.** Posługując się `ABI` dla architektury `x86-64` wyznacz rozmiar struktury `«node»`. Dla każdej składowej typu `«node»` podaj: wymaganie na wyrównanie (funkcja `alignof`), przesunięcie względem początku struktury node (funkcja `offsetof`), rozmiar (funkcja `sizeof`). Następnie zoptymalizuj rozmiar struktury zmieniając kolejność pól. Wyznacz rozmiar struktury po optymalizacji.
>> **Wskazówka:** Zapoznaj się z dodatkowymi slajdami do wykładu 7.

# [C - unions](https://www.tutorialspoint.com/cprogramming/c_unions.htm)
# [Dodatkowe slajdy do wykładu 7.](https://skos.ii.uni.wroc.pl/pluginfile.php/48978/mod_resource/content/0/wyklad_7.pdf)

>> ```c
>> struct node {
>>     char id[2];                     // 1 * 2 bajty
>>                                     // 6 bajtów
>>     int (*hashfn)(char *);          // 8 bajtów
>>     short flags;                    // 2 bajty
>>                                     // 2 bajty
>>     union {
>>         struct {
>>             short n_key;                    // 2 bajty
>>                                             // 2 bajty
>>             int n_data[2];                  // 2 * 4 bajtów
>>             unsigned char n_type;           // 1 bajt
>>                                             // 3 bajty
>>         } s;                            // 16 bajtów
>>         unsigned l_value[2];            // 2 * 4 bajtów
>>     } u;                            // 16 bajtów
>>                                     // 4 bajty
>>                                   // = 40 bajtów
>> };
>> ```
>> ```
>>  +0 |  id[0]  |  id[1]  |         |         |         |         |         |         |
>>
>>  +8 | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn |
>>
>> +16 |  flags  |  flags  |         |         |  union  |  union  |  union  |  union  |
>> 
>> +24 |  union  |  union  |  union  |  union  |  union  |  union  |  union  |  union  |
>>
>> +32 |  union  |  union  |  union  |  union  |         |         |         |         |
>> ```
>
>> ```c
>> struct node1 {
>>     union {
>>         struct {
>>             int n_data[2];                  // 2 * 4 bajtów
>>             short n_key;                    // 2 bajty
>>             unsigned char n_type;           // 1 bajt
>>                                             // 1 bajt
>>         } s;                            // 12 bajtów                            
>>         unsigned l_value[2];            // 2 * 4 bajtów
>>     } u;                            // 12 bajtów     
>>     short flags;                    // 2 bajty
>>     char id[2];                     // 1 * 2 bajty             
>>     int (*hashfn)(char *);          // 8 bajtów
>>                                   // = 24 bajty
>> };
>> ```
>> ```
>>  +0 |  union  |  union  |  union  |  union  |  union  |  union  |  union  |  union  |
>>
>>  +8 |  union  |  union  |  union  |  union  |  flags  |  flags  |  id[0]  |  id[1]  |
>>
>> +16 | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn | *hashfn |
>> ```