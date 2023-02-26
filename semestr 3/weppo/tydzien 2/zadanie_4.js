console.log(typeof 7)
console.log(typeof 'bubu')
console.log(typeof true)
console.log(typeof undefined)
console.log(typeof {})
console.log(typeof new String("elo"))
console.log(typeof function() {})
console.log(typeof (typeof 1), "\n")
//typeof zwraca string opisujacy typ obiektu; nazywa go dokladnie jesli jest typu prostego, w innym wypadku zwraca "object" / "function"
//Ma zastosowanie raczej w typach prostych

console.log(7 instanceof Number)
console.log(new Number(7) instanceof Number)
console.log({} instanceof Object)
console.log([1, 2] instanceof Array)
console.log(function() {} instanceof Function)
//instanceof w duzym uproszczeniu¹ sprawdza, czy obiekt jest instancja okreslonego typu (konstruktora)
//Ma zastosowanie raczej w typach zlozonych



/*
¹Dokladniej sprawdza lancuch prototypow obiektu i sprawdza, czy jest tam wzmianka o danym konstruktorze
Zazwyczaj zwroci true, jesli obiekt zostal stworzony danym konstruktorem lub jego potomkiem,
jednakze teoretycznie da sie zaingerowac w ten proces, przykladowo metoda Object.setPrototypeOf()
*/