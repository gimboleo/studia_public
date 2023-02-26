let http = require('http');
let express = require('express');

let app = express()
app.set('view engine', 'ejs')
app.set('views', './views')



app.get('/', (req, res) => {
    let data = {
        options: [
            {name: '1', text: 'first text'},
            {name: '2', text: 'second text'},
            {name: '3', text: 'third text'}
    ]}

    res.render('index', data)
})



http.createServer(app).listen(3000)
console.log('started')