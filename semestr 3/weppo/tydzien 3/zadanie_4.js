function createFs(n) { // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    for ( var i=0; i<n; i++ ) {
        fs[i] =
            function() {
                return i;
            };
    };
    return fs;
}

var myfs = createFs(10);

console.log( myfs[0]() ); // zerowa funkcja miała zwrócić 0
console.log( myfs[2]() ); // druga miała zwrócić 2
console.log( myfs[7]() );

// 10 10 10
//Dzieje sie tak, poniewaz zasieg zmiennej var obejmuje cala funkcje
//W kazdej iteracji petli mamy do czynienia z ta sama zmienna i, ktorej wartosc po zakonczeniu petli wynosi 10

//Alternatywnym rozwiazaniem jest owiniecie przypisania do fs[i] w natychmiastowo wywolana funkcje, tworzac domkniecie
//Babel : https://babeljs.io/repl#?browsers=ie%206&build=&builtIns=false&corejs=3.6&spec=false&loose=false&code_lz=GYVwdgxgLglg9mABBATgUwIZTQMQM4AUYAlIgN6ID0liUA7nCgF4CetGARgDYwSCYgIiSgwAawgArGAChEsxADcMKRMDyIAvIgDaAXQDcVGjAC0UDCvBjx5pu2682AWxt0UAZ4gxA4ICJpclYyIBIhcaFC-6gAMBjAAPGAxANSJiKRkMv5yqlowOhoZmZnC0PBgBGkFhVXoUCAoSDB6lVWIAL5N_u2VNXVCeE2tUlKKyo4sqhrI6Fi4hACMkcRNUhAIeHChAHRccADmwWPZkTrlqQbUiExoKHB05sJW5o4wGIBCgC7unj6RK2sbaNs9gdxngtAAmE6kJaGRAAExQIF2Txe70urg83kQYN-YHWWx2-0Qh1BAHZIWcgA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Creact%2Cstage-2&prettier=false&targets=&version=7.16.4&externalPlugins=&assumptions=%7B%7D
function createFs2(n) { // tworzy tablicę n funkcji
    var fs = []; // i-ta funkcja z tablicy ma zwrócić i
    for ( var i=0; i<n; i++ ) {
        fs[i] =
            function (i) {
                return function() {
                    return i;
                };
            }(i);
    };
    return fs;
}

var myfs2 = createFs2(10);

console.log( myfs2[0]() ); // zerowa funkcja miała zwrócić 0
console.log( myfs2[2]() ); // druga miała zwrócić 2
console.log( myfs2[7]() );