class Function2D
    def initialize(p)
        raise ArgumentError, 'Argument has to be an binary Proc object' if (!p.instance_of? Proc or p.arity != 2)
        @p = p
    end


    def value(x, y)
        raise ArgumentError, 'Arguments have to be numeric' unless x.kind_of? Numeric and y.kind_of? Numeric
        return @p.call(x, y)
    end


    def volume(a, b, c ,d)
        @@length = 1e-3
        raise ArgumentError, "Arguments have to be numeric" unless a.kind_of? Numeric and b.kind_of? Numeric and c.kind_of? Numeric and d.kind_of? Numeric
        return 0 if a >= b or c >= d

        sum = 0
        cc = c

        while a <= b do
            while cc <= d do
                sum += value(a, cc) * @@length ** 2
                cc += @@length
            end
            cc = c
            a += @@length
        end

        return sum
    end


    def contour_line(a, b, c, d, height)
        @@length = 1e-1
        @@e = 1e-10
        raise ArgumentError, "Arguments have to be numeric" unless a.kind_of? Numeric and b.kind_of? Numeric and c.kind_of? Numeric and d.kind_of? Numeric and height.kind_of? Numeric
        
        arr = []
        cc = c

        while a <= b do
            while cc <= d do
                arr.push([a, cc]) if (height - value(a, cc)).abs < @@e
                cc += @@length
            end
            cc = c
            a += @@length
        end

        return arr
    end
end