class Search
    class << self

        def linear(c, v)
            raise ArgumentError, "Invalid collection" unless valid?(c)

            i = 0
            while i < c.length
                return i if c.get_val(i) == v
                i += 1
            end

            return nil
        end

        def binary(c, v)
            raise ArgumentError, "Invalid collection" unless valid?(c)
            b_search(c, v, 0, c.length)
        end


        private

        def valid?(c)
            return true if c.respond_to?("length") && c.respond_to?("get_val")
            return false
        end

        def b_search(c, v, l, r)
            return nil if l > r
            
            m = (l + r) / 2

            return b_search(c, v, m+1, r) if c.get_val(m) < v
            return b_search(c, v, l, m-1) if c.get_val(m) > v
            return m
        end
    end
end
