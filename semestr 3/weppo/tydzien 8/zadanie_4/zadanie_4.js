let mssql = require('mssql');



(async function main() {
    let conn = new mssql.ConnectionPool('server=localhost,1433;database=weppo;user id=foo;password=foo;trustServerCertificate=true')

    try {
        await conn.connect()
        let request = new mssql.Request(conn)
        let response = await request.query(`insert into MIEJSCE_PRACY3 (Nazwa) values ('Fajna firma')
        insert into OSOBA3 (Imie, Nazwisko, Plec, ID_MIEJSCE_PRACY) values ('Marcin', 'Marcinkowski', 'M', scope_identity())`)

        await conn.close()
    }
    catch (err) {
        if (conn.connected) conn.close()
        console.log(err)
    }
})()