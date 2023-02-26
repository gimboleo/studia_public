class Sorter
    class << self

        #O(n^2) - wolniejsza
        def bubble(c)
            raise ArgumentError, "Invalid collection" unless valid?(c)

            res = c.deep_copy
            return res if res.length == 1
            
            for i in 0 ... res.length
                for j in 1 ... res.length - i
                    res.swap(j, j-1) if (res.get(j) < res.get(j - 1))
                end
            end

            return res
        end

        #O(n*log(n)) - szybsza
        def merge(c)
            raise ArgumentError, "Invalid collection" unless valid?(c)

            res = c.deep_copy
            return res if res.length == 1

            merge_sort(res, 0, res.length - 1)
            return res
        end


        private

        def valid?(c)
            return true if c.respond_to?('length') && c.respond_to?('get') && c.respond_to?('set') && c.respond_to?('swap') && c.respond_to?('deep_copy')
            return false
        end

        def merge_sort(c, b, e)
            return if b == e

            m = (b + e) / 2
            merge_sort(c, b, m)
            merge_sort(c, m+1, e)
            merging(c, b, m, m+1, e)
        end

        def merging(c, b1, e1, b2, e2)
            temp = Array.new(e2 - b1 + 1)
            p1 = b1
            p2 = b2
            i = 0

            while (p1 <= e1 && p2 <= e2)
                if c.get(p1) < c.get(p2)
                    temp[i] = c.get(p1)
                    p1 += 1
                else
                    temp[i] = c.get(p2)
                    p2 += 1
                end
                i += 1
            end

            while (p1 <= e1)
                temp[i] = c.get(p1)
                p1 += 1
                i += 1
            end

            while (p2 <= e2)
                temp[i] = c.get(p2)
                p2 += 1
                i += 1
            end

            j = b1
            for e in temp
                c.set(j, e)
                j += 1
            end
        end
    end
end