//Sprawdzamy i in a, poniewaz natywna metoda forEach nie bierze pod uwage niezdefiniowanych wartosci w tablicy
function forEach(a, f) {for (let i = 0; i < a.length; i++) if (i in a) f(a[i])}

function map(a, f)
{
    let res = new Array(a.length)
    for (let i = 0; i < a.length; i++) if (i in a) res[i] = f(a[i])
    return res
}

function filter(a, f)
{
    let res = []
    for (let i = 0; i < a.length; i++) if (i in a && f(a[i])) res.push(a[i])
    return res
}


let a = [2, 5, 9, 11]
a[10] = 28

a.forEach(function(x) {console.log(x + 1)})
console.log('------')
forEach(a, function(x) {console.log(x + 1)})
console.log()

console.log(a.map(x => x * 2))
console.log(map(a, x => x * 2))
console.log()

console.log(a.filter(() => true))
console.log(filter(a, () => true))
console.log(a.filter(x => x % 2))
console.log(filter(a, x => x % 2))
console.log()