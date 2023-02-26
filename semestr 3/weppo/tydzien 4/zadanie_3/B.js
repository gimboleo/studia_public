//Cyklicznosc mozna osiagnac ustawiajac exports przed ustawieniem require
module.exports = b
const a = require('./a')

function b(n)
{
    if (n > 0)
    {
        console.log(`b: ${n}`)
        a(n - 1)
    }
}