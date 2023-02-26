#ifndef polynomial_hpp
#define polynomial_hpp
#include <iostream>
using namespace std;

class polynomial
{
    private:
        int n;
        double *a;

    public:
        polynomial();
        polynomial(int d, const double c[]);
        polynomial(initializer_list<double> c);
        polynomial(const polynomial &p);
        polynomial(polynomial &&p);
        polynomial& operator = (const polynomial &p);
        polynomial& operator = (polynomial &&p);
        ~polynomial();

        friend istream& operator >> (istream &in, polynomial &p);
        friend ostream& operator << (ostream &out, polynomial &p);

        friend polynomial operator + (const polynomial &p1, const polynomial &p2);
        friend polynomial operator - (const polynomial &p1, const polynomial &p2);
        friend polynomial operator * (const polynomial &p1, const polynomial &p2);
        friend polynomial operator * (double c, const polynomial &p);
        friend polynomial operator * (const polynomial &p, double c);

        polynomial& operator += (const polynomial &p);
        polynomial& operator -= (const polynomial &p);
        polynomial& operator *= (const polynomial &p);
        polynomial& operator *= (double c);

        double operator () (double x) const;
        const double& operator [] (int i) const;

        void set_coefficient(int index, double x);
        int get_degree() const;

        void print() const;
};

#endif