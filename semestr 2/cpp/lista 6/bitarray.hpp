#ifndef bitarray_hpp
#define bitarray_hpp
#include <cstdint>
#include <initializer_list>
#include <iostream>

namespace computations
{
    class bitarray
    {
        private:
            typedef uint64_t word;
            static const int word_size = sizeof(word) * 8;      //64 bits

            class ref
            {
                private:
                    word* w;                                    //Word that contains a given bit
                    int i;                                      //The index of this bit in the word

                public:
                    ref(word* w, int i);
                    explicit operator bool() const;             //Converting ref object back to boolean
                    ref& operator =(bool val);
                    ref& operator =(const ref& r);
            };


        protected:
            int len;
            word *arr;


        public:
            explicit bitarray(int size);
            explicit bitarray(word w);
            bitarray(std::initializer_list<bool> l);
            bitarray(const bitarray &arr);
            bitarray(bitarray &&arr);
            bitarray& operator =(const bitarray &arr);
            bitarray& operator =(bitarray &&arr);
            ~bitarray();

            bool operator [](int i) const;
            ref operator [](int i);
            inline int size() const;

            friend std::istream& operator >>(std::istream &in, bitarray &arr);
            friend std::ostream& operator <<(std::ostream &out, const bitarray &arr);

            friend bitarray operator |(const bitarray &a1, const bitarray &a2);         //or
            friend bitarray operator &(const bitarray &a1, const bitarray &a2);         //and
            friend bitarray operator ^(const bitarray &a1, const bitarray &a2);         //xor
            friend bitarray operator !(const bitarray &arr);                            //not

            bitarray& operator |=(const bitarray &arr);                                 //or
            bitarray& operator &=(const bitarray &arr);                                 //and
            bitarray& operator ^=(const bitarray &arr);                                 //xor
    };
}

#endif