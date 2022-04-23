> **Zadanie 3.** Podaj rozmiar w bajtach poniższych struktur przyjmując, że wskaźnik jest 64-bitowy (architektura x86-64). Pod jakim przesunięciem, względem początku struktury, znajdują się poszczególne pola? Jak zreorganizować pola struktury, by zajmowała mniej miejsca? Z czego wynika takie zachowanie kompilatora?
>> **Wskazówka**: Użyj kompilatora, aby się dowiedzieć jaki jest rozmiar powyższych struktur – przyda się słowo kluczowe `«sizeof»`.

![Zapamiętywanie structa](https://i.imgur.com/6Axbnt6.png)

>> ```c
>> struct A {
>>     int8_t a;  // 1 bajt
>>                // 7 bajtów
>>     void *b;   // 8 bajtów 
>>     int8_t c;  // 1 bajt
>>                // 1 bajt
>>     int16_t d; // 2 bajty
>>                // 4 bajty
>>              // = 24 bajty
>> };
>> ```
>> ```
>>  +0 | a |   |   |   |   |   |   |   |
>>
>>  +8 | b | b | b | b | b | b | b | b |
>>
>> +16 | c |   | d | d |   |   |   |   |
>> ```
>
>> ```c
>> struct A {
>>     int8_t a;  // 1 bajt
>>     int8_t c;  // 1 bajt
>>     int16_t d; // 2 bajty
>>                // 4 bajty
>>     void *b;   // 8 bajtów 
>>              // = 16 bajtów
>> };
>> ```
>> ```
>>  +0 | a | c | d | d |   |   |   |   |
>>
>>  +8 | b | b | b | b | b | b | b | b |
>> ```

>> ```c
>> struct B {
>>     uint16_t a; // 2 bajty
>>                 // 6 bajtów
>>     double b;   // 8 bajtów
>>     void *c;    // 8 bajtów
>>              // =  24 bajty
>> };
>> ```
>> ```
>>  +0 | a | a |   |   |   |   |   |   |
>>
>>  +8 | b | b | b | b | b | b | b | b |
>>
>> +16 | c | c | c | c | c | c | c | c |
>> ```
>>
>> Tej struktury nie da się zoptymalizować.