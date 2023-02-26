> **Zadanie 1.** Intencją procedury `«swap»` jest zamiana wartości przechowywanych w komórkach pamięci o adresie `«xp» i «yp»`. Odwołując się do pojęcia **aliasingu pamięci** (ang. *memory aliasing*) wytłumacz czemu kompilator nie może zoptymalizować poniższej procedury do procedury `«swap2»`? Pomóż mu zoptymalizować `«swap»` posługując się słowem kluczowym `«restrict»` i wyjaśnij jego znaczenie.
>> ```c
>> void swap(long *xp, long *yp) {
>>     *xp = *xp + *yp; /* x+y */
>>     *yp = *xp - *yp; /* x+y-y = x */
>>     *xp = *xp - *yp; /* x+y-x = y */
>> }
>> ```
>
>> ```c
>> void swap2(long *xp, long *yp) {
>>     long x = *xp, y = *yp;
>>     x = x + y, y = x - y, x = x - y;
>>     *xp = x, *yp = y;
>> }
>> ```

Kompilator nie może zoptymalizować procedury `«swap»` do procedury `«swap2»`, ponieważ wskaźniki `«xp»` i `«yp»` mogą wskazywać na ten sam obszar w pamięci. W tej sytuacji procedury te dają 2 różne wyniki - pierwsza zawsze zmieni wartość pod wskaźnikami na 0, druga 'zamieni' liczby wpisując pod wskaźniki tą samą wartość, która już tam była.

Słowo kluczowe `«restrict»` mówi kompilatorowi, że dany wskaźnik przez czas jego życia jest jedynym sposobem na uzyskanie dostępu do wskazywanej przez niego pamięci. Dostęp przez inny wskaźnik skutkuje niezdefiniowanym zachowaniem. Po jego użyciu kompilator wykorzystałby powyższą optymalizację:
```c
void swap(long restrict *xp, long restrict *yp) {
	*xp = *xp + *yp; /* x+y */
	*yp = *xp - *yp; /* x+y-y = x */
	*xp = *xp - *yp; /* x+y-x = y */
}
```