//Uzycie operatorow . oraz [] do odwolywania sie do skladowych obiektu
let a =
{
    sample: "text"
}

//Nazwa klucza po . jest traktowana doslownie, nazwa klucza w [] jest obliczana do stringa
//Korzystajac z [] mozemy uzyc zmiennych albo spacji, gdzie w przypadku . nie jest to mozliwe
//Klucze w przypadku . musza byc alfanumeryczne (z dodatkiem _ i $) i nie zaczynac sie od cyfry
const le_str = "le"
console.log(a.sample, a["sample"], a["samp" + le_str], "\n")



//Uzycie argumentow innego typu niz string dla operatora [] dostepu do skladowej obiektu

//W JavaScripcie wszystkie klucze to stringi: zarowno liczba jak i objekt sa poddane konwersji do stringa
let b = {}
b[5] = "ala"                                        //W przypadku liczb programista kontroluje wartosc klucza przez dobor liczby
b[a] = "ma"                                         //Domyslnie obiekt oblicza sie do stringa "[object Object]"

let c = {toString: () => "My object stringified"}   //Lecz programista moze nadpisac metode toString aby zmienic ta wartosc
b[c] = "kota"
console.log(b, "\n", 5+'', a+'', c+'', "\n")



//Uzycie argumentow innego typu niz number dla operatora [] dostepu do tablicy
let arr = [0, 1, 2]
arr["tekst"] = 3                                    //W obu przypadkach w tablicy pojawiaja sie nowe atrybuty powiazane z kluczami
arr[c] = 4                                          //Obiekt zostaje obliczony do stringa
console.log(arr)                                    
for (const i of arr) console.log(i)                 //Jednakze wartosci te nie sa trzymane razem z normalnie indeksowanymi wartosciami
console.log(arr.length)                             //W szczegolnosci dlugosc tablicy sie nie zmienia
arr.length = 5
console.log(arr, arr[4])                            //Zwiekszenie dlugosci tablicy wypelni pustke wartosciami niezdefiniowanymi
arr.length = 2
console.log(arr)                                    //Zmniejszenie dlugosci tablicy utnie elementy o najwiekszych indeksach
arr.length = 0                                      //Jednak nawet przy calkowitym wyczyszczeniu tablicy
console.log(arr)                                    //argumenty nienumeryczne pozostaja nienaruszone