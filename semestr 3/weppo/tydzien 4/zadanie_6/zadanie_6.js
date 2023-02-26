const fs = require('fs')
const readline = require('readline')

let count = {}

const rl = readline.createInterface(fs.createReadStream('log.txt'))

rl.on('line', function(line) 
{
    let ip = line.split(' ')[1]
    count[ip] = (count[ip] || 0) + 1
})

rl.on('close', function()
{
    let top3 = Object.keys(count).map(function(key) {return [key, count[key]]}).
    sort(function(first, second) {return second[1] - first[1]}).slice(0, 3)
      
    for (let k of top3) console.log(`${k[0]} ${k[1]}`)
})