> **Zadanie 10**. Być może jest to zaskakujące, ale poniższy kod jest poprawny i w dodatku czasami korzysta się z tej niskopoziomowej techniki optymalizacji. Co robi procedura `«secret»`?
>> ```c
>> void secret(uint8_t *to, uint8_t *from, size_t count) {
>>     size_t n = (count + 7) / 8;
>>     switch (count % 8) {
>>     case 0: do { *to++ = *from++;
>>     case 7: *to++ = *from++;
>>     case 6: *to++ = *from++;
>>     case 5: *to++ = *from++;
>>     case 4: *to++ = *from++;
>>     case 3: *to++ = *from++;
>>     case 2: *to++ = *from++;
>>     case 1: *to++ = *from++;
>>           } while (--n > 0);
>>     }
>> }
>> ```
> Kompilator GCC dopuszcza by instrukcja `«goto»` przyjmowała wyrażenie obliczające adres skoku. Dodatkowo umożliwia definiowanie [tablic etykiet](https://gcc.gnu.org/onlinedocs/gcc/Labels-as-Values.html). Przetłumacz powyższą procedurę tak, by korzystała wyłącznie z instrukcji `«goto»`.

### Wstęp

Wyobraźmy sobie, że chcemy skopiować $count$ bajtów, spod jednego adresu na drugi, gdzie $count$ jest podzielny przez $8$ i większy od $0$.

#### Najprostsze podejście

```c
void simple(uint8_t *to, uint8_t* from, size_t count) {
    do {
        *to++ = *from++;
       } while(--count > 0);
}
```

#### Lepsze podejście

Możemy jednak skorzystać z tego, że liczba bajtów jest podzielna przez $8$ i wykonywać po $8$ kopiowań w jednym obrocie pętli, wtedy zaoszczędzimy wielokrotne, niepotrzebne sprawdzanie warunku.

```c
void better(uint8_t *to, uint8_t* from, size_t count) {
    int n = count / 8;
    do {
        *to++ = *from++;
        *to++ = *from++;
        *to++ = *from++;
        *to++ = *from++;
        *to++ = *from++;
        *to++ = *from++;
        *to++ = *from++;
        *to++ = *from++;
       } while(--n > 0);
}
```

#### Podejście z treści zadania

Jak uogólnić takie rozwinięcie pętli na dowolną liczbę elementów tablicy? Wykonać najpierw $modulo \space 8$ takich operacji, a później analogicznie do powyższego sposobu, już dla podzielnej przez $8$ liczby elementów.


```c
void secret(uint8_t *to, uint8_t* from, size_t count)
{
    size_t n = (count + 7) / 8;
    switch(count%8) {
       case 0: do { *to++ = *from++;
       case 7:      *to++ = *from++;
       case 6:      *to++ = *from++;
       case 5:      *to++ = *from++;
       case 4:      *to++ = *from++;
       case 3:      *to++ = *from++;
       case 2:      *to++ = *from++;
       case 1:      *to++ = *from++;
                  } while (--n > 0);
    }
}
```

### Zapis za pomocą goto

```c
void secret_goto(uint8_t *to, uint8_t* from, size_t count)
{
    static void* labels[] = {&&label0, &&label1, &&label2, &&label3, &&label4, &&label5, &&label6, &&label7};
    size_t n = (count + 7) / 8;
    goto *labels[count % 8];
    label0:      *to++ = *from++;
    label7:      *to++ = *from++;
    label6:      *to++ = *from++;
    label5:      *to++ = *from++;
    label4:      *to++ = *from++;
    label3:      *to++ = *from++;
    label2:      *to++ = *from++;
    label1:      *to++ = *from++;
    if (--n > 0) goto label0;
}
```