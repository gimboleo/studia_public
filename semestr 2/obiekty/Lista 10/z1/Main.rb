load "Collection.rb"
load "Sorter.rb"

arr = Collection.new
arr2 = Collection.new

for i in 0 ... 20
    arr.push(rand(0 .. 100))
    arr2.push(rand(0 .. 100))
end

s = Time.now
bb1 = Sorter.bubble(arr)
bb2 = Sorter.bubble(arr2)
t1 = Time.now - s

s = Time.now
mg1 = Sorter.merge(arr)
mg2 = Sorter.merge(arr2)
t2 = Time.now - s

puts 'Bubble: (' + t1.to_s + ')'
puts bb1.to_s
puts bb2.to_s
puts

puts 'Merge: ('+ t2.to_s + ')'
puts mg1.to_s
puts mg2.to_s

#Testy potwierdzaja, ze merge sort jest zwykle szybszy