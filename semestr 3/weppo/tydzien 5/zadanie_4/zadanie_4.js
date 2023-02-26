let http = require('http');
let express = require('express');



let app = express()
app.use(express.urlencoded({extended: true}))
app.use(express.static('./static'))
app.set('view engine', 'ejs')
app.set('views', './views')



app.get('/', (req, res) => {
    res.render('index', {course: '', name: '', group: '', date: '', points: new Array(15).fill(''), sum: '0', errorMessage: ''})
})


app.post('/', (req, res) => {
    let course = req.body.course
    let name = req.body.name
    let group = req.body.group
    let date = req.body.date
    let points = req.body.points
    let sum = req.body.sum

    if (course && name && group && date) {
        res.render('print', {course: course, name: name, group: group, date: date, points: points.map(v => v || 0), sum: sum})
    }
    else {
        res.render('index', {course: course, name: name, group: group, date: date, points: points, sum: sum, errorMessage: 'Brakuje danych!'})
    }
})



http.createServer(app).listen(3000)
console.log('started')