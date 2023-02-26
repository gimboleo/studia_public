class Collection
    class Node
        attr_accessor :val, :prv, :nxt

        def initialize(val, prv = nil, nxt = nil)
            @val = val
            @prv = prv
            @nxt = nxt
        end
    end

    def initialize
        @head = nil
    end

    def length
        ptr = @head
        res = 0

        until ptr.nil?
            res += 1
            ptr = ptr.nxt
        end

        return res
    end

    def push(v)
        e = Node.new(v)

        if @head.nil?
            @head = e
            return
        end

        if e.val < @head.val
            @head.prv = e
            e.nxt = @head
            @head = e
            return
        end

        ptr = @head
        ptr = ptr.nxt while !ptr.nxt.nil? && e.val >= ptr.nxt.val

        if ptr.nxt.nil?
            e.prv = ptr
            ptr.nxt = e
        else
            e.prv = ptr
            e.nxt = ptr.nxt
            ptr.nxt.prv = e
            ptr.nxt = e
        end
    end

    def prnt
        ptr = @head

        until ptr.nil?
            print ptr.val
            print ", " unless ptr.nxt.nil?
            ptr = ptr.nxt
        end
    end

    def get_val(i)
        raise IndexError, "Index out of bounds!" unless i < self.length && i >= 0

        ptr = @head
        c = 0

        until ptr.nil?
            return ptr.val if c == i
            c += 1
            ptr = ptr.nxt
        end
        return -1
    end
end