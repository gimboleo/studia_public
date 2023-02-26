function fib_it()
{
    let [a, b] = [0, 1]
    return {next: () => {return {value: a, done: ([a, b] = [b, a + b]) && false}}}
}

function *fib()
{
    let [a, b] = [0, 1]
    while (true)
    {
        yield a;
        [a, b] = [b, a + b]
    }
}


var foo = {[Symbol.iterator]: fib_it}

for (let i of foo)
{
    if (i > 200) break
    console.log(i)
}

console.log()

for (let i of fib())
{
    if (i > 200) break
    console.log(i)
}