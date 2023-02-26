# ZGUBIŁEM GDZIEŚ ROZWIĄZANIE, ALE CAŁE ROZUMOWANIE JEST W [KSIĄŻCE](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf)

> **Zadanie 7.** Skompiluj poniższą funkcję i na podstawie wynikowego kodu maszynowego skonstruuj **graf przepływu danych** jak w [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), §5.7.3]. Wskaż w nim **ścieżkę krytyczną** na podstawie **czasu opóźnienia** przetwarzania instrukcji z tabeli [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), 5.12].
>> ```c
>> void nonsense(long a[], long k, long *dp, long *jp) {
>>     long e = a[2];
>>     long g = a[3];
>>     long m = a[4];
>>     long h = k - 1;
>>     long f = g * h;
>>     long b = a[f];
>>     long c = e * 8;
>>     *dp = m + c;
>>     *jp = b + 4;
>> }
>> ```