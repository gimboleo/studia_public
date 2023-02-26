#Dla obu klas znaki nie wystepujace w podanym slowniku odpowiednio jako klucz/wartosc zostana po prostu przepisane

class Sub_cipher
    def initialize(string)
        @text = string
    end

    def to_s
        return @text
    end
end

class Plaintext < Sub_cipher
    def encrypt(dict)
        res = ""
        @text.each_char {|char| if dict[char] then res += dict[char] else res += char end}
        return Ciphertext.new(res)
    end
end

class Ciphertext < Sub_cipher
    def decrypt(dict)
        res = ""
        @text.each_char {|char| if dict.index(char) then res += dict.index(char) else res += char end}
        return Plaintext.new(res)
    end
end