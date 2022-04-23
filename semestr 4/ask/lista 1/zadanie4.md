> **Zadanie 4.** Rozważamy słowa kluczowe ze standardu C11 (a nie C++). Jakie jest działanie `«volatile»` w stosunku do zmiennych? Kiedy programiści muszą go użyć, by program zachowywał się poprawnie? Jaki jest skutek użycia `«static»` w stosunku do zmiennych globalnych, zmiennych lokalnych i procedur? Kiedy należy go używać? Jaką rolę pełni `«restrict»` odnośnie typów wskaźnikowych?
>> **Wskazówka**: W przypadku `«volatile»` nie chodzi o wyłączenie optymalizacji!

## `volatile`
### Działanie
Modyfikator `volatile` dodany do zmiennej jest informacją dla kompilatora, że jej zawartość może się zmienić w nieznanych momentach nawet jeśli kod danej funkcji jej nie zmienia. Konsekwencją jest niestosowanie optymalizacji dla zmiennej volatile. Oznacza to, że kompilator przy każdym użyciu odczytuje jej wartość z pamięci zamiast przechowywać ją w rejestrze jeśli wykonuje na niej kilka operacji. Poza tym kompilator nie zmienia kolejności działań wykonywanych przy użyciu tej zmiennej.
### Użytkowanie
- Jest on używany do deklaracji zmiennych współdzielonych przez różne wątki. W każdym momencie wykonywania danego wątku może nastąpić zmiana kontekstu i wywołanie drugiego wątku korzystającego z tej zmiennej.
- Pojawia się także przy dostępie do sprzętu, gdzie pamięć jest wykorzystywana do komunikacji pomiędzy urządzeniami.

---

## `static`
### Działanie
Dla zmiennych globalnych i procedur `static` mówi kompilatorowi, aby nie udostępniał zmiennej innym plikom źródłowym. Dla zmiennych lokalnych `static` powoduje, że zmienna jest inicjalizowana tylko raz i zachowuje swoją wartość między wywołaniami funkcji.
### Użytkowanie
- Pozwala stworzyć prywatne zmienne globalne i procedury.
- Statyczna zmienna lokalna może przykładowo zliczać ilość wywołań funkcji.

---

## `restrict`
Słowo kluczowe informujące kompilator, że dany wskaźnik jest jedynym sposobem na dostanie się do obiektu, na który wskazuje. Dysponując tą informacją kompilator może poczynić stosowne optymalizacje. Niezastosowanie się do tego ograniczenia przez programistę skutkuje działaniem niezdefiniowanym.