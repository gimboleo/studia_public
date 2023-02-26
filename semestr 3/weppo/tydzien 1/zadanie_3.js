let res = []

for (let i = 2; i <= 100000; i++)
{
    let prime = true
    for (let j = 2; j <= Math.floor(Math.sqrt(i)); j++)
    {
        if (!(i % j))
        {
            prime = false
            break
        }
    }

    if (!prime) continue
    res.push(i)
}

console.log(res)