# UWAGA, NIE MOŻNA KOMPLETNIE UFAĆ GODBOLTOWI W KWESTII LICZBY CYKLI! W SZCZEGÓLNOŚCI `llvm-mca` ZAKŁADA, ŻE ZAWSZE JEST CACHE HIT!

> **Zadanie 4.** Na wykładzie została zaprezentowana funkcja `«compute»` i na jej przykładzie wyjaśniono optymalizacje transformacji pętli, tj. **zamiany pętli** (ang. *loop interchange*), **łączenia pętli** (ang. *loop fusion*) oraz **usuwania zmiennych indukcyjnych** (ang. *induction variable elimination*). Czy kompilator był w stanie przeprowadzić te optymalizacje na poniższej funkcji? Jeśli nie, to zoptymalizuj ją krok po kroku. Przeanalizuj dokładnie działanie funkcji, czy jesteś w stanie poczynić jakieś obserwacje, które pozwalają Ci wykonać dodatkowe optymalizacje, np. **ponowne wyliczanie wartości** (ang. [*rematerialization*](https://en.wikipedia.org/wiki/Rematerialization))?
>> ```c
>> void compute2(long *a, long *b, long k) {
>>  long n = 1 << k;
>>  for (long i = 0; i < n; i++)
>>      a[i * n] = a[i] = 0;
>>  for (long i = 1; i < n; i++)
>>      for (long j = 1; j < n; j++)
>>          a[j * n + i] = i * j;
>>  for (long i = 1; i < n; i++)
>>      for (long j = 1; j < n; j++)
>>          b[i * n + j] = a[i * n + j]
>>                       + a[(i - 1) * n + (j - 1)];
>> }


[Goldbolt (original)](https://godbolt.org/z/drPEY3j61)  
Kompilatorowi nie udało się wykonać żadnej z powyższych optymalizacji.

[Optymalizacja](https://godbolt.org/z/dff6r3sb6)  
W drugiej pętli `a[j * n + i]` można zamienić na `a[i * n + j]`, co skutkuje przechodzeniem tablicy w bardziej *cache-friendly* sposób. Można także wtedy zmergować drugą i trzecią pętlę. Odczyt z pamięci `a[(i - 1) * n + (j - 1)]` można zamienić na obliczenie równoważnej wartości `(i - 1) * (j - 1)`.
