#include "double_array.cpp"
#include <iostream>
using namespace computations;

int main()
{
    double_array x = double_array();                            //As the maximum size turns out to be pretty big,
    std::cout << x.get_len() << "\n\n";                         //This function takes a while to execute
    for (int i = 0; i < 10; i++) std::cout << x[i] << "\n";     //(Assigning the random values is lengthy to be exact)

    double_array y = double_array(10);
    y[9] = 27;
    for (int i = 0; i < 10; i++) std::cout << y[i] << " "; std::cout << "\n";
    y[1] = 1.99;
    for (int i = 0; i < 10; i++) std::cout << y[i] << " "; std::cout << "\n";
    std::cout << y[9] << "\n\n";

    double_array z = y;
    for (int i = 0; i < 10; i++) std::cout << z[i] << " "; std::cout << "\n";
    for (int i = 0; i < 10; i++) std::cout << y[i] << " "; std::cout << "\n\n";

    double_array a = (std::move(z));
    for (int i = 0; i < 10; i++) std::cout << a[i] << " "; std::cout << "\n";
    std::cout << z.get_len() << "\n\n";   //The array is now nullptr as expected

    double_array b{1, 2, 3, 10.523, 987};
    for (int i = 0; i < b.get_len(); i++) std::cout << b[i] << " "; std::cout << "\n\n";

    std::cout << double_array{1, 2, 3, 4} * double_array{4, 3, 2, 1} << "\n\n";     //20
    //std::cout << double_array{1, 2, 3} * double_array{4, 3, 2, 1} << "\n";        //Assertion will fail here



    //Exception testing below
    
    try
    {
        new double_array(0);
    }
    catch(std::invalid_argument exc)
    {
        std::clog << exc.what() << "\n";
    }

    try
    {
        y[10];
    }
    catch(std::out_of_range exc)
    {
        std::clog << exc.what() << "\n";
    }

    try
    {
        y[-1];
    }
    catch(std::out_of_range exc)
    {
        std::clog << exc.what() << "\n";
    }
}