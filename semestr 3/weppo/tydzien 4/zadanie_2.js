//Metode prywatna Qux() implementujemy przez domkniecie
let Foo = (function()
{
    function F(name) {this.name = name}

    function Qux() {return `Calling private method Qux() for ${this.name}`}

    F.prototype.Bar = function() {console.log(`${this.name}: ${Qux.call(this)}`)}

    return F
}())


let f1 = new Foo("A")
let f2 = new Foo("B")

f1.Bar()
f2.Bar()
console.log()

console.log(f1.Bar)
console.log(f1.Qux)
console.log(Foo.Qux)