load "Function2D.rb"    

one = Function2D.new(lambda {|x, y| x**2 + y**2})
two = Function2D.new(lambda {|x, y| x + y})

puts one.value(1, -4)
puts two.value(1, -4)

puts one.volume(1, 3, 2, 4) #54.667
puts two.volume(1, 2, 3, 4) #5

print one.contour_line(1, 3, 2, 4, 5)
puts
print two.contour_line(-1, 1, -1, 1, 0)