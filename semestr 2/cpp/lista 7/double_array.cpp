//#define NDEBUG                   //Uncomment to disable assert()
#include "double_array.hpp"
#include <stdexcept>
#include <stdlib.h>
#include <time.h>
#include <cassert>

namespace computations
{
    double_array::double_array(int size)
    {
        if (size <= 0) throw std::invalid_argument("Array's size has to be positive!");

        this->len = size;
        this->arr = new double[size]();
    }

    double_array::double_array(std::initializer_list<double> l)
    {
        //if (l.size() <= 0) throw std::invalid_argument("Array's size has to be positive!");
        //This seems to be unnecessary, as apparently c++ syntax doesn't allow empty initalizer lists

        this->len = l.size();
        this->arr = new double[l.size()];

        int i = 0;
        for (double d: l)
        {
            this->arr[i] = d;
            i++;
        }
    }

    double_array::double_array()
    {
        this->arr = nullptr;
        long long int i = 1;
        int size_allowed = 0;

        while(true)
        {
            delete[] this->arr;
            if (!(this->arr = new (std::nothrow) double[i])) break;
            size_allowed = i;
            i *= 2;
        }

        this->len = size_allowed;
        this->arr = new double[size_allowed];

        srand(time(NULL));
        for(int i = 0; i < this->len; i++) this->arr[i] = (double)rand() / (double)RAND_MAX;
    }

    double_array::double_array(const double_array &arr)
    {
        this->len = arr.len;
        this->arr = new double[this->len];
        for (int i = 0; i < this->len; i++) this->arr[i] = arr.arr[i];
    }

    double_array::double_array(double_array &&arr)
    {
        this->len = arr.len;
        this->arr = arr.arr;

        arr.len = 0;
        arr.arr = nullptr;
    }

    double_array& double_array::operator =(const double_array &arr)
    {
        if (&arr != this)
        {
            delete[] this->arr;

            this->len = arr.len;
            this->arr = new double[this->len];
            for (int i = 0; i < this->len; i++) this->arr[i] = arr.arr[i];
        }

        return *this;
    }

    double_array& double_array::operator =(double_array &&arr)
    {
        if (&arr != this)
        {
            delete[] this->arr;

            this->len = arr.len;
            this->arr = arr.arr;

            arr.len = 0;
            arr.arr = nullptr;
        }

        return *this;
    }

    double_array::~double_array()
    {
        delete[] this->arr;
    }



    double& double_array::operator [](int index)
    {
        if (index < 0) throw std::out_of_range("Index can't be negative!");
        if (index >= this->len) throw std::out_of_range("Index out of bounds!");

        return this->arr[index];
    }

    const double double_array::operator[](int index) const
    {
        if (index < 0) throw std::out_of_range("Index can't be negative!");
        if (index >= this->len) throw std::out_of_range("Index out of bounds!");

        return this->arr[index];
    }



    double operator *(const double_array &a1, const double_array &a2)
    {
        assert(a1.len == a2.len);

        double res = 0;
        for (int i = 0; i < a1.len; i++) res += a1.arr[i] * a2.arr[i];
        
        return res;
    }



    const int double_array::get_len() const
    {
        return this->len;
    }
}