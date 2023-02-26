let mssql = require('mssql');



(async function main() {
    let conn = new mssql.ConnectionPool('server=localhost,1433;database=weppo;user id=foo;password=foo;trustServerCertificate=true')

    try {
        await conn.connect()
        let request = new mssql.Request(conn)
        let response = await request.query(`insert into MIEJSCE_PRACY4 (Nazwa) values ('Nowa firma') 
        declare @id_1 as int = scope_identity()
        insert into OSOBA4 (Imie, Nazwisko, Plec) values ('Marcin', 'Marcinkowski', 'M') 
        declare @id_2 as int = scope_identity()
        insert into OSOBA_MIEJSCE_PRACY4 (ID_OSOBA, ID_MIEJSCE_PRACY) values (@id_1, @id_2)`)

        await conn.close()
    }
    catch (err) {
        if (conn.connected) conn.close()
        console.log(err)
    }
})()