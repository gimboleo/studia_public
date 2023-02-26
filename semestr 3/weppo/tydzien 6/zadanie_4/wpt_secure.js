let http = require('http');
let express = require('express');
let crypto = require('crypto');



let secret = 'secret password'

let app = express()



app.get('/', (req, res) => {res.end('Not much to see here')})

app.get('/new', (req, res) => {
    let id = '' + Math.floor(Math.random() * 1000000) + 1
    let hmac = encodeURIComponent(crypto.createHmac('sha256', secret).update(id).digest('hex'))
    res.redirect(`/faktura/${id}?mac=${hmac}`)
})

app.get('/faktura/:id', (req, res) => {
    let hmac = crypto.createHmac('sha256', secret).update(req.params.id).digest('hex')
    res.end(decodeURIComponent(req.query.mac) == hmac ? `faktura: ${req.params.id}` : 'Authentication failed!')
})



http.createServer(app).listen(3000)
console.log('started')