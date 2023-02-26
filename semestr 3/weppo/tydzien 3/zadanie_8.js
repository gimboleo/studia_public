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



function *take(it, top)
{
    for (let i = 0; i < top; i++)
    {
        let next = it.next()
        if (next.done) break
        yield next.value
    }
}


for (let i of take(fib_it(), 10)) console.log(i)
console.log()
for (let i of take(fib(), 10)) console.log(i)