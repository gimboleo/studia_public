> **Zadanie 5.** Zmienne `«a»`, `«b»` i `«c»` to wskaźniki na tablice elementów typu `«uint32_t»`. Przetłumacz, krok po kroku, poniższe dwie instrukcje złożone zapisane w języku C na **kod trójkowy**:
>> **Wskazówka**: Przyjmujemy, że wszystkie wyrażenia są obliczane od lewej do prawej.

> `s += b[j+1] + b[--j];` 
>> ```c
>> t1 = j + 1
>> t2 = t1 * 4
>> t3 = b + t2
>> t4 = *t3
>>
>> j = j - 1
>> t5 = j * 4
>> t6 = b + t5
>> t7 = *t6
>>
>> t8 = t4 + t7
>> s = s + t8
>> ```

> `a[i++] -= *b * (c[j*2] + 1);`
>> ```c
>> t1 = *b
>> 
>> t2 = j * 2
>> t3 = t2 * 4
>> t4 = c + t3
>> t5 = *t4
>> 
>> t6 = t5 + 1
>> 
>> t7 = t5 * t6
>> 
>> t8 = i * 4
>> t9 = a + t8
>> t10 = *t9
>> t11 = t10 - t7
>> *t9 = t11
>> 
>> i = i + 1
>> ```