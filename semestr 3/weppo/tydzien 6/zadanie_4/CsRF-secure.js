let http = require('http');
let express = require('express');
let cookieParser = require('cookie-parser');
let csrf = require('csurf');



let csrfProtection = csrf({cookie: true})

let app = express()
app.use(express.urlencoded({extended: true}))
app.set('view engine', 'ejs')
app.set('views', './views')
app.use(cookieParser())



app.get('/', (req, res) => {res.end('Not much to see here')})

app.get('/form', csrfProtection, (req, res) => {res.render('send-secure', {csrfToken: req.csrfToken()})})

app.post('/process', csrfProtection, (req, res) => {res.end(`Email changed to ${req.body.mail}.`)})



http.createServer(app).listen(3000)
console.log('started')