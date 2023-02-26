#include "bitarray.hpp"
#include <stdexcept>
#include <cmath>
#include <string>
#include <algorithm>

namespace computations
{
    bitarray::ref::ref(word *w, int i)
    {
        this->w = w;
        this->i = i;
    }

    bitarray::ref::operator bool() const
    {
        return (bool)(*this->w & (word(1) << this->i));
    }

    bitarray::ref& bitarray::ref::operator =(bool val)
    {
        *this->w ^= (-val ^ *this->w) & (word(1) << this->i);
        return *this;
    }

    bitarray::ref& bitarray::ref::operator =(const ref& r)
    {
        *this = (bool)r;
        return *this;
    }



    bitarray::bitarray(int size)
    {
        if (size <= 0) throw std::invalid_argument("Array's size must be positive!");

        this->len = size;
        int words = size % word_size ? size / word_size + 1 : size / word_size;
        this->arr = new word[words]();
    }

    bitarray::bitarray(word w)
    {
        this->len = word_size;
        this->arr = new word[1];
        this->arr[0] = w;
    }

    bitarray::bitarray(std::initializer_list<bool> l) : bitarray((int)l.size())
    {
        int i = this->len - 1;
        for (bool bit : l)
        {
            (*this)[i] = bit;
            i--;
        }
    }

    bitarray::bitarray(const bitarray &arr)
    {
        this->len = arr.len;
        int x = (int)(sizeof(arr.arr) / 8);
        this->arr = new word[x];
        for (int i = 0; i < x; i++) this->arr[i] = arr.arr[i];
    }

    bitarray::bitarray(bitarray &&arr)
    {
        this->len = arr.len;
        this->arr = arr.arr;

        arr.len = 0;
        arr.arr = nullptr;
    }

    bitarray& bitarray::operator =(const bitarray &arr)
    {
        if (&arr != this)
        {
            delete[] this->arr;

            this->len = arr.len;
            int x = (int)(sizeof(arr.arr) / 8);
            this->arr = new word[x];
            for (int i = 0; i < x; i++) this->arr[i] = arr.arr[i];
        }

        return *this;
    }

    bitarray& bitarray::operator =(bitarray &&arr)
    {
        if (&arr != this)
        {
            this->len = arr.len;
            this->arr = arr.arr;
            
            arr.len = 0;
            arr.arr = nullptr;
        }

        return *this;
    }

    bitarray::~bitarray()
    {
        delete this->arr;
    }



    bool bitarray::operator [](int i) const
    {
        if (i < 0 || i >= this->len) throw std::invalid_argument("Index out of bounds!");

        word a = i / word_size;
        word b = i % word_size;
        return (bool)ref(&(this->arr[a]), b);
    }

    bitarray::ref bitarray::operator [](int i)
    {
        if (i < 0 || i >= this->len) throw std::invalid_argument("Index out of bounds!");

        word a = i / word_size;
        word b = i % word_size;
        return ref(&(this->arr[a]), b);
    }

    int bitarray::size() const
    {
        return this->len;
    }



    std::istream& operator >>(std::istream &in, bitarray &arr)
    {
        std::string words;
        in >> words;
        if (words.find_first_not_of("01") != std::string::npos) throw std::invalid_argument("Only '0' and '1' are allowed characters!");

        delete arr.arr;

        int word_size = bitarray::word_size;
        arr.len = words.size();
        int word_count = arr.len % word_size ? arr.len / word_size + 1 : arr.len / word_size;
        arr.arr = new bitarray::word[word_count]();

        int i = arr.len - 1;
        for (char& c : words) arr[i--] = (c - '0');

        return in;
    }

    std::ostream& operator <<(std::ostream &out, const bitarray &arr)
    {
        for (int i = arr.len - 1; i >= 0; i--) out << arr[i];
        return out;
    }



    bitarray operator |(const bitarray &a1, const bitarray &a2)
    {
        bitarray res(std::max(a1.len, a2.len));
        int smaller = std::min(a1.len, a2.len);

        for (int i = 0; i < smaller; i++) res[i] = a1[i] || a2[i];
        return res;
    }

    bitarray operator &(const bitarray &a1, const bitarray &a2)
    {
        bitarray res(std::max(a1.len, a2.len));
        int smaller = std::min(a1.len, a2.len);

        for (int i = 0; i < smaller; i++) res[i] = a1[i] * a2[i];
        return res;
    }

    bitarray operator ^(const bitarray &a1, const bitarray &a2)
    {
        bitarray res(std::max(a1.len, a2.len));
        int smaller = std::min(a1.len, a2.len);

        for (int i = 0; i < smaller; i++) res[i] = (a1[i] + a2[i]) % 2;
        return res;
    }

    bitarray operator !(const bitarray &arr)
    {
        bitarray res(arr.len);

        for (int i = 0; i < arr.len; i++) res[i] = !arr[i];
        return res;
    }



    bitarray& bitarray::operator |=(const bitarray &arr)
    {
        *this = *this | arr;
        return *this;
    }

    bitarray& bitarray::operator &=(const bitarray &arr)
    {
        *this = *this & arr;
        return *this;
    }

    bitarray& bitarray::operator ^=(const bitarray &arr)
    {
        *this = *this ^ arr;
        return *this;
    }
}