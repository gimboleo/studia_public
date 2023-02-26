console.log( (![]+[])[+[]]+(![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]] );   //"fail"

/*
console.log( (![]+[])[+[]]  +  (![]+[])[+!+[]]  +  ([![]]+[][[]])[+!+[]+[+[]]]  +  (![]+[])[!+[]+!+[]] )
console.log(     "f"        +       "a"         +              "i"              +          "l"         )



f: (![]+[])[+[]]
Przez negacje [] jako obiekt obliczy sie do booleana (true), wiec ![] oblicza sie do false

+ binarny ewaluuje obie strony rownania do wartosci prostych i jezeli ktoras jest stringiem to zwraca konkatenacje stringow
[] obliczy sie do ""¹, wiec false+"" => "false"

+ unarny wymusza koercje do liczby, zatem +[] => 0, bo Number([]) == 0

"false"[0] => "f"



a: (![]+[])[+!+[]]
![]+[] => "false"

+[] => 0; !+[] => true; +!+[] => 1; "false"[1] => "a"



i: ([![]]+[][[]])[+!+[]+[+[]]]
![] = false; [![]] = [false]

[[]] -- Zewnetrzna tablica zmusi wewnetrzna do obliczenia sie do ''; [[]] => ['']; [][''] => undefined

[false] + undefined => "falseundefined"

[+[]] => [0]; !+[] => true; +true => 1; [1+[0]] => ["10"]; "falseundefined"["10"] => "falseundefined"[10] => "i"



l: (![]+[])[!+[]+!+[]]
![]+[] => "false"; !+[] => true; [true + true] => [1 + 1] => [2]; "false"[2] = "l"



¹wewnetrzna metoda toPrimitive zwraca valueOf() albo toString() obiektu, valueOf() tablicy nie obliczy sie do typu prostego,
wiec zwracany jest string
*/