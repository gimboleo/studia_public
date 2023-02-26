let mssql = require('mssql');



(async function main() {
    let conn = new mssql.ConnectionPool('server=localhost,1433;database=weppo;user id=foo;password=foo;trustServerCertificate=true')

    try {
        await conn.connect()
        let request = new mssql.Request(conn)
        let result = await request.query(`update OSOBA1 set Imie='Izabela' where id=9`)

        console.log(result.rowsAffected[0])

        await conn.close()
    }
    catch (err) {
        if (conn.connected) conn.close()
        console.log(err)
    }
})()