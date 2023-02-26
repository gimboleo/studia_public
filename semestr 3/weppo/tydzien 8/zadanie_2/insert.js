let mssql = require('mssql');



(async function main() {
    let conn = new mssql.ConnectionPool('server=localhost,1433;database=weppo;user id=foo;password=foo;trustServerCertificate=true')

    try {
        await conn.connect()
        let request = new mssql.Request(conn)
        let result = await request.query(`insert into OSOBA1 (Imie, Nazwisko, Plec) values ('Anna', 'Fistaszek', 'F') select scope_identity() as id`)

        console.log(result.recordset[0].id)

        await conn.close()
    }
    catch (err) {
        if (conn.connected) conn.close()
        console.log(err)
    }
})()