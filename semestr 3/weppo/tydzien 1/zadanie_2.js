let res = []

for (let i = 1; i <= 100000; i++)
{
    let flag = false
    let sum = 0

    const digits = (i + '').split('').map(Number)

    for (const digit of digits) 
    {
        if (!digit || i % digit)
        {
            flag = true
            break
        }

        sum += digit
    }

    if (flag) continue

    //sum = digits.reduce((a, b) => a + b, 0)
    if (i % sum) continue

    res.push(i)
}

console.log(res)