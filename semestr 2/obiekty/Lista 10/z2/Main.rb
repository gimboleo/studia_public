load "Collection.rb"
load "Search.rb"

x = Collection.new
x.push(10)
x.push(15)
x.push(5)
x.push(19)
x.push(6)
x.push(-7)

x.prnt
puts
puts Search.linear(x, 10)
puts Search.binary(x, 19)
puts Search.linear(x, -999)
puts Search.binary(x, -999)
puts Search.linear(x, -7)
puts Search.binary(x, 5)