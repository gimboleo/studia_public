> **Zadanie 7.** Przetłumacz, krok po kroku, poniższą procedurę napisaną w języku C na kod trójkowy:
>> ```c
>> void insertion_sort(int arr[], int length) {
>>     int j, temp;
>>     for (int i = 0; i < length; i++) {
>>         j = i;
>>         while (j > 0 && arr[j] < arr[j-1]) {
>>             temp = arr[j];
>>             arr[j] = arr[j-1];
>>             arr[j-1] = temp;
>>             j--;
>>         }
>>     }
>> }
>> ```
> Następnie oznacz **bloki podstawowe** i narysuj **graf przepływu sterowania** (ang. control flow graph).
>> **Wskazówka**: W języku C wyrażenia logiczne są obliczane w [uproszczony sposób](https://en.wikipedia.org/wiki/Short-circuit_evaluation).

```c
INSERT:     i = 0                       <<B0>>

L0:         if (i < length) goto L1     <<B1>>

            return                      <<B2>>

L1:         j = i                       <<B3>>

R0:         if (j > 0) goto R1          <<B4>>

L2:         i = i + 1                   <<B5>>
            goto L0

R1:         t1 = j * 4                  <<B6>>
            t2 = arr + j
            t3 = *t2
            t4 = j - 1
            t5 = t4 * 4
            t6 = arr + t5
            t7 = *t6
            if (t3 < t7) goto R2

            goto L2                     <<B7>>

R2:         temp = t3                   <<B8>>
            *t3 = t7
            *t7 = temp
            j = j - 1
            goto R0
```

```graphviz
digraph {
    graph [bgcolor=transparent]
    node [fillcolor=black fontcolor=white]
    START -> B0;
    B0 -> B1;
    B1 -> B2, B3;
    B2 -> END;
    B3 -> B4;
    B4 -> B5, B6;
    B5 -> B1;
    B6 -> B7, B8;
    B7 -> B5;
    B8 -> B4;
}
```