load "zad1.rb"

print 36.divisors.sort, "\n"
print -36.divisors.sort, "\n"
print 50.divisors.sort, "\n"
print 37.divisors.sort, "\n"

begin
    print 0.divisors
rescue => error
    puts error.inspect
end

print 1.divisors.sort, "\n"
print 2.divisors.sort, "\n"
print 6.divisors.sort, "\n"
puts


puts 0.ack(10)              #11
puts 4.ack(0)               #13
puts 2.ack(3)               #9

begin
    puts 2.ack(-1)
rescue => error
    puts error.inspect
end
puts


puts -6.perfect
puts 0.perfect
puts 1.perfect
puts 2.perfect
puts 3.perfect
puts 4.perfect
puts 5.perfect
puts 6.perfect              #t
puts 28.perfect             #t
puts 496.perfect            #t
puts


puts -1.to_string
puts -45.to_string
x = -5576
puts x
puts x.to_string
puts x
puts 9000.to_string