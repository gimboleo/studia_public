#Stos
class Collection
    def initialize
        @arr = []
    end

    def push(element)
        @arr.push(element)
    end

    def pop()
        raise RangeError, 'Array is empty!' unless length > 0
        return @arr.pop
    end

    def peek()
        raise RangeError, 'Array is empty!' unless length > 0
        return @arr[-1]
    end

    def length()
        return @arr.size
    end

    def get(i)
        raise IndexError, "Index out of bounds!" unless i < length and i >= 0
        return @arr[i]
    end

    def set(i, v)
        raise IndexError, "Index out of bounds!" unless i < length and i >= 0
        @arr[i] = v
    end

    def swap(i, j)
        raise IndexError, "Index out of bounds!" unless i < length and i >=0 and j < length and j >=0
        temp = @arr[j]
        @arr[j] = @arr[i]
        @arr[i] = temp
    end

    def to_s
        return @arr.to_s
    end

    def deep_copy
        n = Collection.new
        @arr.each {|e| n.push(e)}
        return n
    end
end