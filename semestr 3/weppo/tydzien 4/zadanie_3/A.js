//Cyklicznosc mozna osiagnac ustawiajac exports przed ustawieniem require
module.exports = a
const b = require('./b')

function a(n)
{
    if (n > 0)
    {
        console.log(`a: ${n}`)
        b(n - 1)
    }
}