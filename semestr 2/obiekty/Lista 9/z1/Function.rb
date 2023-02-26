class Function
    def initialize(p)
        raise ArgumentError, 'Argument has to be an unary Proc object' if (!p.instance_of? Proc or p.arity != 1)
        @p = p
    end


    def value(x)
        raise ArgumentError, 'Argument has to be numeric' unless x.kind_of? Numeric
        return @p.call(x)
    end


    def zero(a, b, e)
        raise ArgumentError, 'Argument has to be numeric' unless a.kind_of? Numeric and b.kind_of? Numeric and e.kind_of? Numeric
        raise ArgumentError, 'e has to be positive' unless e > 0

        arr = []

        while a <= b do
            arr.push(a) if value(a) * value(a + e) < 0 or value(a) == 0
            a += e
        end

        return nil if arr.empty?
        return arr
    end


    def field(a, b)
        @@height = 1e-5
        raise ArgumentError, "Arguments have to be numeric" unless a.kind_of? Numeric and b.kind_of? Numeric
        return 0 if a >= b
        
        sum = 0
        y2 = value(a)
        
        while a <= b - @@height do
            a += @@height
            y1 = y2
            y2 = value(a)
            sum += (y1 + y2) * @@height / 2
        end
        
        return sum
    end


    def deriv(x)
        @@h = 1e-10
        raise ArgumentError, 'Argument has to be numeric' unless x.kind_of? Numeric
        return (value(x + @@h) - value(x)) / @@h
    end
end