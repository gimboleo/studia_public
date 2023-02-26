load "zad3.rb"

key = 
{
    'a' => 'b',
    'b' => 'r',
    'r' => 'y',
    'y' => 'u',
    'u' => 'a'
}

plain = Plaintext.new("ruby efg")
cipher = plain.encrypt(key)
plain_again = cipher.decrypt(key)

puts plain.to_s
puts cipher.to_s
puts plain_again.to_s
puts

alphabet = ('a' .. 'z').to_a

puts "Enter shift for the Caesar's cipher: "
a = gets.chomp.to_i
dic = alphabet.zip(alphabet.rotate(a)).to_h
puts "Enter phrase to encode / decode: "
b = gets.chomp
print "Encoded: ", Plaintext.new(b).encrypt(dic).to_s, "\n"
print "Decoded: ", Ciphertext.new(b).decrypt(dic).to_s, "\n"