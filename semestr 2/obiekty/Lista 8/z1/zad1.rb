require 'set'

class Integer
    @@number_string = 
    {
        0 => "zero",
        1 => "one",
        2 => "two",
        3 => "three",
        4 => "four",
        5 => "five",
        6 => "six",
        7 => "seven",
        8 => "eight",
        9 => "nine"
    }

    
    #Ta metoda zwraca tylko dodatnie dzielniki liczby
    def divisors
        raise ArgumentError, 'All positive integers divide zero!' if self == 0
        return self.abs.divisors if self < 0

        res = Set[]

        for i in 1 .. (Math.sqrt(self) + 1) do
            if self % i == 0
                res.add(i) 
                res.add(self / i)
            end
        end

        return res.to_a
    end


    def ack(y)
        raise ArgumentError, "Ackermann's function arguments must be non-negative!" if self < 0 || y < 0
        return y + 1 if self == 0
        return (self - 1).ack(1) if y == 0
        return (self - 1).ack(self.ack(y - 1))
    end


    def perfect
        return false if self <= 0

        sum = 0
        self.divisors.each {|val| sum += val}
        return sum == 2 * self
    end

    
    def to_string
        return "zero" if self == 0

        temp = self
        res = ""
        arr = []

        if temp < 0
            res += "minus" 
            temp = temp.abs
        end

        while temp != 0
            arr.push(" " + @@number_string[temp % 10])
            temp /= 10
        end

        arr.reverse_each {|word| res += word}

        res[0] = '' if res[0] == ' '
        return res
    end
end