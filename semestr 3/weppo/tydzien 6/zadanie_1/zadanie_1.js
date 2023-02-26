let http = require('http');
let express = require('express');
let multer = require('multer');

let app = express()
app.set('view engine', 'ejs')
app.set('views', './views')

let upload = multer({dest: 'uploads/'})



app.get('/', (req, res) => {res.render('index')})

app.post('/upload', upload.single('uploadedFile'), (req, res) => {console.log(req.file)})



http.createServer(app).listen(3000)
console.log('started')