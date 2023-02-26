let http = require('http');

let file = 'zadanie_3.txt';

let server = http.createServer((req, res) => {
    res.setHeader('Content-Disposition', 'attachment; filename=' + file)
    res.end('Sample file contents')
})

server.listen(3000)
console.log('started')