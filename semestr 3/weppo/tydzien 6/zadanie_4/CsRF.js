let http = require('http');
let express = require('express');



let app = express()
app.use(express.urlencoded({extended: true}))
app.set('view engine', 'ejs')
app.set('views', './views')



app.get('/', (req, res) => {res.end('Not much to see here')})

app.get('/form', (req, res) => {res.render('send')})

app.post('/process', (req, res) => {res.end(`Email changed to ${req.body.mail}.`)})



http.createServer(app).listen(3000)
console.log('started')