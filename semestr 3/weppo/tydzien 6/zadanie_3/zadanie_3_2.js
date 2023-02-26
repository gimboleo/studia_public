let http = require('http');
let express = require('express');
let cookieParser = require('cookie-parser');
let session = require('express-session');
let fileStore = require('session-file-store')(session);

let app = express()
app.set('view engine', 'ejs')
app.set('views', './views')
app.use(cookieParser())

app.use(session({
  store: new fileStore,
  secret: 'secret password',
  resave: true,
  saveUninitialized: true
}))



app.get("/delete", (req, res) => {
  try {req.session.destroy()} 
  catch (e) {console.error(e)} 
  finally {res.redirect('/')}
})

app.get('/', (req, res) => {
  req.session.views ? req.session.views++ : req.session.views = 1
  res.setHeader('Content-Type', 'text/html')
  res.end(`<p>Wyświetlenia: ${req.session.views}</p>`)
})



http.createServer(app).listen(3000)
console.log('started')