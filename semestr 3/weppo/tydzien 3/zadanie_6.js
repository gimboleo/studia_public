function createGenerator() {
    var _state = 0;
    return {
        next: function() {
            return {
                value : _state,
                done : _state++ >= 10
            }
        }
    }
}

var foo = {
    [Symbol.iterator] : createGenerator
};

for ( var f of foo )
    console.log(f);

console.log()



function createGenerator2(n) {
    return function() {
        var _state = 0;
        return {
            next: function() {
                return {
                    value : _state,
                    done : _state++ >= n
                }
            }
        }
    }
}

var foo1 = {
    [Symbol.iterator] : createGenerator2(40)
};

var foo2 = {
    [Symbol.iterator] : createGenerator2(3)
}

for ( var f of foo1 )
    console.log(f);    

console.log()

for ( var f of foo2 )
    console.log(f);    