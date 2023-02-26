let http = require('http');
let express = require('express');
let cookieParser = require('cookie-parser');

let app = express()
app.set('view engine', 'ejs')
app.set('views', './views')
app.use(cookieParser())



app.get('/', (req, res) => {res.render('index', {cookies: Object.keys(req.cookies)})})

app.get('/add/:cookie', (req, res) => {
    let cookieValue = new Date().toString()
    res.cookie(req.params.cookie, cookieValue, {maxAge: 360000})
    res.redirect('/')
  })
  
  app.post('/delete/:cookie', (req, res) => {
    let cookie = req.params.cookie
    res.clearCookie(cookie)
    res.redirect('/')
  })



http.createServer(app).listen(3000)
console.log('started')