> **Zadanie 6.** Zapoznaj się z [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), §5.11.2] i na podstawie [[1](https://github.com/Sorosliu1029/CSAPP-Labs/blob/master/Computer%20Systems%20A%20Programmers%20Perspective%20(3rd).pdf), §5.7.1] wyjaśnij jak procesor przetwarza skoki warunkowe. W jakim celu procesor używa **predyktora skoków**? Co musi zrobić, jeśli skok zostanie źle przewidziany? Które skoki warunkowe warto zoptymalizować do instrukcji `«cmov»`? Posługując się narzędziem *Compiler Explorer* z opcją `«-O1»` przepisz poniższą funkcję tak, żeby w wierszu 4 kompilator nie wygenerował skoku warunkowego.
>> ```c
>> void merge1(long src1[], long src2[], long dest[], long n) {
>>     long i1 = 0, i2 = 0;
>>     while (i1 < n && i2 < n)
>>         *dest++ = src1[i1] < src2[i2] ? src1[i1++] : src2[i2++];
>> }
>> ```
>> [Godbolt](https://godbolt.org/z/GM4nMGTqq)
>
>> **Wskazówka:** W kodzie po optymalizacji mogą wystąpić tylko dwa skoki warunkowe.

Współczesne procesory działają z dużym paralelizmem obsługując jednocześnie wiele instrukcji. Działa to bardzo dobrze, o ile instrukcje programu mają być wykonane w prostej sekwencji. Sprawa komplikuje się, gdy program zawiera rozgałęzienia. Procesor przy napotkaniu rozgałęzienia musi zgadnąć, w którą stronę pójdzie. W przypadku skoku warunkowego oznacza to zgadnięcie, czy skok zostanie wykonany. W skoku pośrednim lub powrocie z procedury oznacza to przewidywanie adresu docelowego. Po zgadnięciu odnogi w którą pójdzie program, procesor zacznie wykonywać z niej instrukcje. Robi to jednak w sposób, który nie modyfikuje rzeczywistych rejestrów ani miejsc w pamięci dopóki nie zostanie określony rzeczywisty wynik rozgałęzienia.

Jeśli okaże się, że branch został poprawnie przewidziany, procesor może 'zacommitować' odroczone wyniki obliczeń w rejestrach i pamięci. W przeciwnym przypadku musi on odrzucić wszystkie 'spekulacyjne' wyniki i zacząć proces pobierania instrukcji z poprawnej lokalizacji.

Podstawową ideą używania instrukcji `cmov` jest obliczenie danej wartości w obu branchach rozgałęzienia, a następnie wybraniu tej odpowiedniej przy 'resolvovaniu' rozgałęzienia. Pozwala to uniknąć płacenia kary za niepoprawne przewidywanie.

Przewidywanie rozgałęzień sprawuje się dobrze w przypadku występowania regularnych wzorców. Zawodzi, gdy uwarunkowanie skoku jest nieprzewidywalne (chociażby zależne od arbitralnych cech danych, takich jak nieujemność liczby). Wtedy opłaca się szukać sposobu na użycie `cmov`.

[merge1 bez skoków warunkowych](https://godbolt.org/z/qKWT8KWc4)