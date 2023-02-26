console.log("Podaj imię: ")

process.stdin.on('data', function(data) 
{
    console.log()
    console.log(`Witaj ${data.toString().trim()}`)
    process.exit()
})