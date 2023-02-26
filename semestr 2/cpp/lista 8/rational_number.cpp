#include "rational_exception.hpp"
#include "rational_number.hpp"
#include <stdlib.h>
#include <math.h>
#include <map>

namespace computations
{
    int rational_number::gcd(int a, int b) noexcept
    {
        if (!b) return a;
        return gcd(b, a%b);
    }

    void rational_number::simplify() noexcept
    {
        if (this->denum < 0)
        {
            this->num *= -1;
            this->denum *= -1;
        }

        int d = gcd(abs(this->num), abs(this->denum));
        this->num /= d;
        this->denum /= d;
    }



    bool rational_number::did_addition_overflow(int a, int b, int res) noexcept
    {
        if (a > 0 && b > 0 && res < 0) return 1;
        if (a < 0 && b < 0 && res > 0) return 1;
        return 0;
    }

    bool rational_number::did_multiplication_overflow(int a, int b, int res) noexcept
    {
        if (a == 0 || b == 0) return 0;
        if (a == res / b) return 0;
        return 1;
    }



    rational_number::rational_number(int num, int denum)
    {
        if (!denum) throw division_by_zero("Denumerator can't be set to 0!");

        this->num = num;
        this->denum = denum;
        this->simplify();
    }

    rational_number::rational_number(int num) noexcept
    {
        this-> num = num;
        this->denum = 1;
    }



    int rational_number::get_num() const noexcept
    {
        return this->num;
    }

    int rational_number::get_denum() const noexcept
    {
        return this->denum;
    }



    rational_number operator +(const rational_number& n1, const rational_number& n2)
    {
        int d = rational_number::gcd(n1.denum, n2.denum);
        int d1 = n1.denum / d;
        int d2 = n2.denum / d;
        int dnew = d1 * d2;

        if (rational_number::did_multiplication_overflow(d1, d2, dnew)) throw out_of_range("Denumerator's multiplication overflow!");

        int num1 = n1.num * dnew / n1.denum;
        int num2 = n2.num * dnew / n2.denum;
        int numnew = num1 + num2;

        if (rational_number::did_addition_overflow(num1, num2, numnew)) throw out_of_range ("Numerator's addition overflow!");

        return rational_number(numnew, dnew);
    }

    rational_number operator -(const rational_number& n1, const rational_number& n2)
    {
        return n1 + (-n2);
    }

    rational_number operator *(const rational_number& n1, const rational_number& n2)
    {
        int numnew = n1.num * n2.num;
        int dnew = n1.denum * n2.denum;

        if (rational_number::did_multiplication_overflow(n1.num, n2.num, numnew)) throw out_of_range ("Numerator's multiplication overflow!");
        if (rational_number::did_multiplication_overflow(n1.denum, n2.denum, dnew)) throw out_of_range ("Denumerator's multiplication overflow!");

        return rational_number(numnew, dnew);
    }

    rational_number operator /(const rational_number& n1, const rational_number& n2)
    {
        if (n2.num == 0) throw division_by_zero("Can't divide by 0!");
        return n1 * (!n2);
    }

    rational_number operator -(const rational_number& n)
    {
        return rational_number(-n.num, n.denum);
    }

    rational_number operator !(const rational_number& n)
    {
        return rational_number(n.denum, n.num);
    }



    rational_number& rational_number::operator +=(const rational_number& n)
    {
        *this = *this + n;
        return *this;
    }

    rational_number& rational_number::operator -=(const rational_number& n)
    {
        *this = *this - n;
        return *this;
    }

    rational_number& rational_number::operator *=(const rational_number& n)
    {
        *this = *this * n;
        return *this;
    }

    rational_number& rational_number::operator /=(const rational_number& n)
    {
        *this = *this / n;
        return *this;
    }
    


    rational_number::operator double() const noexcept
    {
        return double(this->num) / double(this->denum);
    }

    rational_number::operator int() const noexcept
    {
        return round(double(this->num) / double(this->denum));
    }



    std::ostream& operator <<(std::ostream &out, const rational_number &n) noexcept
    {
        if (n.num == 0)
        {
            out << 0;
            return out;
        }

        if (n.denum == 1)
        {
            out << n.num;
            return out;
        }

        int d = n.denum;
        while (d % 2 == 0) d /= 2;
        while (d % 5 == 0) d/= 5;
        if (d == 1)
        {
            out << double(n);
            return out;
        }

        std::string res = "";
        if (n.num < 0) res += "-";

        int num = abs(n.num);
        int den = n.denum;
        
        res += std::to_string(num / den);
        res += ".";

        int remainder = num % den;
        std::map <int, int> m;
        bool repeating;
        int index;

        while (remainder > 0)
        {
            if (m.find(remainder) != m.end())
            {
                index = m[remainder];
                repeating = true;
                break;
            }

            m[remainder] = res.size();
            remainder *= 10;
            int temp = remainder / den;
            res += std::to_string(temp);
            remainder = remainder % den;
        }

        if (repeating)
        {
            res.insert(index, "(");
            res += ")";
        }

        out << res;
        return out;
    }

    std::string rational_number::to_string()
    {
        return std::to_string(this->get_num()) + "/" + std::to_string(this->get_denum());
    }
}
