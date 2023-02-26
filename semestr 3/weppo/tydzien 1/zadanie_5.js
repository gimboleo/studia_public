function fib_iter(n)
{
    let a = 0
    let b = 1

    if (n < 1) return a

    for (let i = 2; i <= n; i++) [a, b] = [b, a + b]

    return b
}

function fib(n) {return n < 1 ? 0 : n == 1 ? 1 : fib(n - 1) + fib(n - 2)}

for (let i = 0; i <= 10; i++) console.log(fib_iter(i), fib(i))  

console.time("Iterative")
for (let i = 10; i <= 40; i++) fib_iter(i)
console.timeEnd("Iterative")

console.log()

console.time("Recursive")
for (let i = 10; i <= 40; i++) fib(i)
console.timeEnd("Recursive")