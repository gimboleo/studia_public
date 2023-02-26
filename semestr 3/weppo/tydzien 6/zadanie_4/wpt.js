let http = require('http');
let express = require('express');



let app = express()



app.get('/', (req, res) => {res.end('Not much to see here')})

app.get('/new', (req, res) => {
    let id = '' + Math.floor(Math.random() * 1000000) + 1
    res.redirect(`/faktura/${id}`)
})

app.get('/faktura/:id', (req, res) => {res.end(`faktura: ${req.params.id}`)})



http.createServer(app).listen(3000)
console.log('started')