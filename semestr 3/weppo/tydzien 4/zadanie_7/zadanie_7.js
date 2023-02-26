const fs = require('fs')
const util = require('util')


//Klasyczny interfejs - callback
fs.readFile('text.txt', 'utf8', function(err, data) 
{
    if (err) console.log(err)
    else console.log(data)
})


//Recznie napisana funkcja z Promise
function fspromise(path, enc)
{
    return new Promise((resolve, reject) =>
    {
        fs.readFile(path, enc, (err, data) =>
        {
            if (err) reject(err)
            resolve(data)
        })
    })
}

fspromise('text.txt', 'utf-8')
    .then(data => {console.log(data)})
    .catch(err => {console.log(err)})


//Promisisifikacja za pomoca util.promisify
const fspromise2 = util.promisify(fs.readFile)

fspromise2('text.txt', 'utf-8')
    .then(data => {console.log(data)})
    .catch(err => {console.log(err)});


//Wykorzystanie fs.promises (i 'nowa' metoda obslugi Promise poprzez async/await)
(async function() 
{
    try
    {
        let data = await fs.promises.readFile('text.txt', 'utf-8')
        console.log(data)
    }
    catch(e) {console.log(e)}
})()