#include "polynomial.hpp"
#include <stdexcept>
#include <string>
#include <cmath>
#include <algorithm>

polynomial::polynomial()
{
    this->n = 0;
    this->a = new double[1];
    this->a[0] = 1;
}

polynomial::polynomial(int d, const double c[])
{
    if (d < 0) throw invalid_argument("Polynomial's degree can't be smaller than 0!");
    if (c[d] == 0 && d > 0) throw invalid_argument("The highest coefficient can't be set to 0!");

    this->n = d;
    this->a = new double[this->n + 1];

    for (int i = 0; i <= d; i++) this->a[i] = c[i];
}

polynomial::polynomial(initializer_list<double> c)
{
    if (c.size() - 1 < 0) throw invalid_argument("Polynomial's degree can't be smaller than 0!");
    if (c.end() - 1 == 0) throw invalid_argument("The highest coefficient can't be set to 0!");
    
    this->n = c.size() - 1;
    this->a = new double[c.size()];

    int i = 0;
    for (double d: c)
    {
        this->a[i] = d;
        i++;
    }
}

polynomial::polynomial(const polynomial &p)
{
    this->n = p.n;
    this->a = new double[this->n + 1];
    for (int i = 0; i <= this->n; i++) this->a[i] = p.a[i];
}

polynomial::polynomial(polynomial &&p)
{
    this->n = p.n;
    this->a = p.a;

    p.n = 0;
    p.a = nullptr;
}

polynomial& polynomial::operator=(const polynomial &p)
{
    if (&p != this)
    {
        delete[] this->a;

        this->n = p.n;
        this->a = new double[this->n + 1];
        for (int i = 0; i <= this->n; i++) this->a[i] = p.a[i];
    }

    return *this;
}

polynomial& polynomial::operator=(polynomial &&p)
{
    if (&p != this)
    {
        delete[] this->a;

        this->n = p.n;
        this->a = p.a;
        p.n = 0;
        p.a = nullptr;
    }

    return *this;
}
        
polynomial::~polynomial()
{
    delete this->a;
}

istream& operator>>(istream &in, polynomial &p)
{
    double x;
    int i = 0;
    double* temp = new double[p.n + 1];

    while (in >> x && i <= p.n) temp[i++] = x;
    if (i - 1 == p.n && temp[i - 1] == 0) throw invalid_argument("Highest coefficient can't be set to 0!");
    for (int j = 0; j < i; j++) p.a[j] = temp[j];

    return in;
}

ostream& operator<<(ostream &out, polynomial &p)
{
    int i = 0;
    while (i <= p.n) out << p.a[i++] << " ";

    return out;
}

polynomial operator+(const polynomial &p1, const polynomial &p2)
{   
    const int m = max(p1.n, p2.n);
    double* array = new double[m + 1];
    int i = 0;
    int non_zero = -1;
    double sum;

    while (i <= p1.n && i <= p2.n)
    {   
        sum = p1.a[i] + p2.a[i];
        if (sum) non_zero = i;
        array[i] = sum;
        i++;
    }

    while (i <= p1.n)
    {
        sum = p1.a[i];
        if (sum) non_zero = i;
        array[i] = sum;
        i++;
    }

    while (i <= p2.n)
    {
        sum = p2.a[i];
        if (sum) non_zero = i;
        array[i] = sum;
        i++;
    }

    if (non_zero == -1) return polynomial{0};
    return polynomial(non_zero, array);
}

polynomial operator-(const polynomial &p1, const polynomial &p2)
{   
    int m = max(p1.n, p2.n);
    double* array = new double[m + 1];
    int i = 0;
    int non_zero = -1;
    double sum;

    while (i <= p1.n && i <= p2.n)
    {   
        sum = p1.a[i] - p2.a[i];
        if (sum) non_zero = i;
        array[i] = sum;
        i++;
    }

    while (i <= p1.n)
    {
        sum = p1.a[i];
        if (sum) non_zero = i;
        array[i] = sum;
        i++;
    }

    while (i <= p2.n)
    {
        sum = -p2.a[i];
        if (sum) non_zero = i;
        array[i] = sum;
        i++;
    }

    if (non_zero == -1) return polynomial{0};
    return polynomial(non_zero, array);
}

polynomial operator*(const polynomial &p1, const polynomial &p2)
{
    if (p1.n == 0 && p2.n == 0) return polynomial{p1.a[0] * p2.a[0]};
    if (p1.n == 0) return p1.a[0] * p2;
    if (p2.n == 0) return p2.a[0] * p1;

    int m = p1.n + p2.n;
    double* array = new double[m + 1]();

    for (int i = 0; i <= p1.n; i++)
    {
        for (int j = 0; j <= p2.n; j++) array[i + j] += p1.a[i] * p2.a[j];
    }

    return polynomial(m, array);
}

polynomial operator*(double c, const polynomial &p)
{
    if (!c) return polynomial{0};

    polynomial temp(p);
    for (int i = 0; i <= temp.n; i++) temp.a[i] *= c;
    return temp;
}

polynomial operator*(const polynomial &p, double c)
{
    return c * p;
}

polynomial& polynomial::operator+=(const polynomial &p)
{
    *this = *this + p;
    return *this;
}

polynomial& polynomial::operator-=(const polynomial &p)
{
    *this = *this - p;
    return *this;
}

polynomial& polynomial::operator*=(const polynomial &p)
{
    *this = *this * p;
    return *this;
}

polynomial& polynomial::operator*=(double c)
{
    *this = *this * c;
    return *this;
}

double polynomial::operator()(double x) const
{
    double res = 0;
    for (int i = this->n; i >= 0; i--) res = x * res + this->a[i];
    return res;
}

const double& polynomial::operator[](int i) const
{
    if (i < 0) throw invalid_argument("Degree can't be negative!");
    if (i > this->n) throw invalid_argument("Given index is bigger than polynomial's degree!");
    return this->a[i];
}

void polynomial::set_coefficient(int index, double x)
{
    if (index < 0) throw invalid_argument("Degree can't be negative!");
    if (index > this->n) throw invalid_argument("Given index is bigger than polynomial's degree!");
    if (this->n > 0 && index == this->n && x == 0) throw invalid_argument("Highest coefficient can't be set to 0!");
    this->a[index] = x;
}

int polynomial::get_degree() const
{
    return this->n;
}

void polynomial::print() const
{
    string res = "";
    double x;
    int y;
    string op;

    if (this->n == 0)
    {   
        x = this->a[0];
        if (floor(abs(x)) == abs(x))
        {
            y = x;
            cout << y << endl;
        } 
        else cout << x << endl;
        return;
    }

    x = this->a[this->n];
    if (floor(abs(x)) == abs(x))
    {
        y = x;
        res.append(to_string(y) + "x^" + to_string(this->n));
    } 
    else res.append(to_string(x) + "x^" + to_string(this->n));

    for (int i = this->n-1; i > 0; i--)
    {
        x = this->a[i];

        if (!x) continue;

        if (x < 0)
        {
            op = " - ";
            x = abs(x);
        }
        else op = " + ";

        if (floor(abs(x)) == abs(x))
        {
            y = x;
            res.append(op + to_string(y) + "x^" + to_string(i));
        } 
        else res.append(op + to_string(x) + "x^" + to_string(i));
    }

    x = this->a[0];

    if (!x)
    {
        cout << res << endl;
        return;
    }

    if (x < 0)
    {
        op = " - ";
        x = abs(x);
    }
    else op = " + ";

    if (floor(abs(x)) == abs(x))
    {
        y = x;
        res.append(op + to_string(y));
    } 
    else res.append(op + to_string(x));

    cout << res << endl;
}