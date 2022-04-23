> **Zadanie 6.** Z punktu widzenia procesora wszystkie wskaźniki są tożsame z liczbami całkowitymi. W trakcie generowania kodu wynikowego kompilator musi przetłumaczyć instrukcje wyboru pola struktury lub wariantu unii `«x->k»` i `«x.k»` oraz indeksowania tablic `«a[i]»` na prostsze instrukcje.
>
> Przetłumacz, krok po kroku, poniższą instrukcję zapisaną w języku C na kod trójkowy. Trzeba pozbyć się typów złożonych, wykonać odpowiednie obliczenia na wskaźnikach, a wszystkie dostępy do pamięci realizować wyłącznie instrukcjami `«x:=*y»` lub `«*x:=y»`. Zmienne `«us»` i `«vs»` są typu `«struct A *»` (patrz zad. 3).
>> ```c
>> struct A {
>>     int8_t a;  // 1 bajt
>>                // 7 bajtów
>>     void *b;   // 8 bajtów 
>>     int8_t c;  // 1 bajt
>>                // 1 bajt
>>     int16_t d; // 2 bajty
>>                // 5 bajtów
>>              // = 24 bajty
>> };
>> ```

>`vs->d = us[1].a + us[j].c;`
>> ```c
>> t1 = us + 24
>> t2 = *t1
>> 
>> t3 = j * 24
>> t4 = t3 + 16
>> t5 = us + t4
>> t6 = *t5
>>  
>> t7 = t6 + t2
>>  
>> t8 = vs + 18
>> *t8 = t7
>> ```