let mssql = require('mssql');



(async function main() {
    let conn = new mssql.ConnectionPool('server=localhost,1433;database=weppo;user id=foo;password=foo;trustServerCertificate=true')

    try {
        await conn.connect()
        let request = new mssql.Request(conn)

        let start = performance.now()
        let result = await request.query(`select * from OSOBA5 where Nazwisko='Kowalski'`)
        let end = performance.now()

        result.recordset.forEach(r => {console.log(r)})
        console.log(`\n${end - start} ms`)

        await conn.close()
    }
    catch (err) {
        if (conn.connected) conn.close()
        console.log(err)
    }
})()

//https://stackoverflow.com/a/6593813