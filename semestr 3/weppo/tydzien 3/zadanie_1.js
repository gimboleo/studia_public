let obj =
{
    field: 5,
    method: function() {console.log("Method.")},
    get val() {return this.field},
    set val(x) {this.field = x}
}


console.log(obj)
obj.method()
console.log(obj.val)
obj.val = 25
console.log(obj.val)
console.log()


//Nowe pola/metody można dodawać za pomocą []/. lub za pomocą metody Object.defineProperty
obj['a'] = true
obj.b = false
obj['c'] = () => true
obj.d = () => false
Object.defineProperty(obj, 'e', {value: true, enumerable: true})
Object.defineProperty(obj, 'f', {value: () => true, enumerable: true})
console.log(obj)
console.log()


//Gettery / settery można dodawać tylko za pomocą Object.defineProperty
Object.defineProperty(obj, 'val2', {get: function() {return this.a}, set: function(x) {this.a = x}})
console.log(obj.val2)
obj.val2 = 478
console.log(obj.val2)