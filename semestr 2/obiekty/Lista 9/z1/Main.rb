load 'Function.rb'

square = Function.new(lambda {|x| x**2})
s = Function.new(lambda {|x| Math.sin(x)})

puts square.value(5)
puts square.deriv(11)

puts s.value(1)
puts s.deriv(1)

puts square.field(1,1)
puts s.field(-5,5)

print s.zero(-10, 10, 0.01)
puts
print square.zero(-199, 100, 1)