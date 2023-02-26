let fs = require('fs');
let https = require('https');


(async function () {
    let pfx = await fs.promises.readFile('zadanie_2.pfx')
    
    let server = https.createServer({
        pfx: pfx,
        passphrase: 'maslo'
    },
    (req, res) => {
        res.setHeader('Content-type', 'text/html; charset=utf-8')
        res.end(`hello world ${new Date()}`)
    })

    server.listen(3000)
    console.log('started')
})()