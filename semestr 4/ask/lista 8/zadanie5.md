> **Zadanie 5.** Rozważmy poniższy program składający się z dwóch jednostek translacji. Po uruchomieniu kończy się on z błędem dostępu do pamięci. Przy pomocy debuggera `gdb` zatrzymaj się w miejscu wystąpienia awarii i wyjaśnij jej przyczynę. Gdzie została umieszczona stała znakowa `«Hello, world!»`? Popraw program tak, by zakończył się poprawnie. **Nie wolno** modyfikować sygnatury procedury `«somestr»` i pliku `«str-a.c»`, ani korzystać z dodatkowych procedur. Gdzie umieszczono ciąg znaków po poprawce?
>> ```c
>> /* str-a.c */
>> #include <stdio.h>
>>
>> char *somestr(void);
>>
>> int main(void) {
>>   char *s = somestr();
>>   s[5] = '\0';
>>   puts(s);
>>   return 0;
>> }
>> ```
>
>> ```c
>> /* str-b.c */
>> char *somestr(void) {
>>   return "Hello, world!";
>> }
>> ```

Program nie działa, ponieważ w funkcji `«main»` próbujemy zmodyfikować dane tylko do odczytu (umieszczone w sekcji `«.rodata»`).

```c
/* str-b.c */
char *somestr(void) {
  static char aux[] = "Hello, world!";
  return aux;
}
```

Po powyższej modyfikacji napis zostanie umieszczony w sekcji `«.data»`, więc może zostać zmodyfikowana.