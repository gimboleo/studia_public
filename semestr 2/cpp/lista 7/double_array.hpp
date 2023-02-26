#ifndef double_array_hpp
#define double_array_hpp
#include <initializer_list>

namespace computations
{
    class double_array
    {
        private:
            double *arr;
            int len;

        public:
            explicit double_array(int size);
            double_array(std::initializer_list<double> l);
            double_array();
            double_array(const double_array &arr);
            double_array(double_array &&arr);
            double_array& operator =(const double_array &arr);
            double_array& operator =(double_array &&arr);
            ~double_array();

            double& operator [](int index);
            const double operator [](int index) const;

            friend double operator *(const double_array &a1, const double_array &a2);

            const int get_len() const;
    };
}

#endif