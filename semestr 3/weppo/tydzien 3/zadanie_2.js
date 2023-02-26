function memoize(f)
{
    let cache = {}

    return (...args) =>
    {
        let k = JSON.stringify(args)
        if (!(k in cache)) cache[k] = f(...args)
        return cache[k]
    }
}



function fib(n) {return n < 1 ? 0 : n == 1 ? 1 : fib(n - 1) + fib(n - 2)}


function fib_2(n) {return n < 1 ? 0 : n == 1 ? 1 : fib_2(n - 1) + fib_2(n - 2)}
fib_2 = memoize(fib_2)


function fib_iter(n)
{
    let a = 0
    let b = 1

    if (n < 1) return a

    for (let i = 2; i <= n; i++) [a, b] = [b, a + b]

    return b
}


let time, res, stamp

for (let i = 0; i <= 40; i += 5)
{
    time = performance.now()
    res = fib(i)
    stamp = performance.now() - time
    console.log(`fib(${i}) = ${res} took ${stamp}ms`)

    time = performance.now()
    res = fib_2(i)
    stamp = performance.now() - time
    console.log(`fib_2(${i}) = ${res} took ${stamp}ms`)

    time = performance.now()
    res = fib_iter(i)
    stamp = performance.now() - time
    console.log(`fib_iter(${i}) = ${res} took ${stamp}ms`)

    console.log()
}
// Funkcja zmemoizowana radzi sobie dużo lepiej od zwykłej rekursywnej, ale wersja iteracyjna ciągle jest najlepsza.