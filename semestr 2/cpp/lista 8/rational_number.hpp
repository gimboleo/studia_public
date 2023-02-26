#ifndef rational_number_hpp
#define national_number_hpp
#include <iostream>
#include <string>

namespace computations
{
    class rational_number
    {
        private:
            int num;
            int denum;

            static int gcd(int a, int b) noexcept;
            void simplify() noexcept;               //Simplifies the fraction using gcd and makes sure that denominator is positive

            static bool did_addition_overflow(int a, int b, int res) noexcept;
            static bool did_multiplication_overflow(int a, int b, int res) noexcept;

        public:
            rational_number(int num, int denum);
            rational_number(int num) noexcept;

            inline int get_num() const noexcept;
            inline int get_denum() const noexcept;

            friend rational_number operator +(const rational_number& n1, const rational_number& n2);
            friend rational_number operator -(const rational_number& n1, const rational_number& n2);
            friend rational_number operator *(const rational_number& n1, const rational_number& n2);
            friend rational_number operator /(const rational_number& n1, const rational_number& n2);
            friend rational_number operator -(const rational_number& n);
            friend rational_number operator !(const rational_number& n);

            rational_number& operator +=(const rational_number& n);
            rational_number& operator -=(const rational_number& n);
            rational_number& operator *=(const rational_number& n);
            rational_number& operator /=(const rational_number& n);

            operator double() const noexcept;
            explicit operator int() const noexcept;

            friend std::ostream& operator <<(std::ostream &out, const rational_number &n) noexcept;
            std::string to_string();
    };
}

#endif