#include "rational_number.cpp"
#include <iostream>
using namespace computations;

int main()
{
    rational_number yy(5);
    rational_number y = yy;
    std::cout << y.to_string() << "\n\n";               //5 / 1

    rational_number x(14, -30);
    std::cout << x.to_string() << "\n\n";               //-7 / 15

    std::cout << (x + y).to_string() << "\n";           //68 / 15
    std::cout << (y - x).to_string() << "\n";           //82 / 15
    std::cout << (x * y).to_string() << "\n";           //-7 / 3
    std::cout << (x / y).to_string() << "\n\n";         //-7 / 75

    y += y;
    std::cout << y.to_string() << "\n";                 //10 / 1
    std::cout << (-y).to_string() << "\n";              //-10 / 1
    std::cout << (!y).to_string() << "\n\n";            //1 / 10

    std::cout << double(x) << "\n";                     //-0.4(6)
    std::cout << int(x) << "\n";                        //0
    std::cout << int(rational_number(8, 9)) << "\n\n";  //1

    std::cout << rational_number(8,9) << "\n";          //0.(8)
    std::cout << y << "\n";                             //10
    std::cout << x << "\n";                             //-0.4(6)
    std::cout << rational_number(1, 13) << "\n";        //0.(076923)
    std::cout << rational_number(5, 11) << "\n";        //0.(45)
    std::cout << rational_number(214, 900) << "\n\n";   //0.23(7)



    //Exception testing below

    try
    {
        new rational_number(5, 0);
    }
    catch(division_by_zero exc)
    {
        std::clog << exc.what() << "\n";
    }

    try
    {
        rational_number(2147483647, 1) + rational_number(1, 1);
    }
    catch(out_of_range exc)
    {
        std::clog << exc.what() << "\n";
    }

    try
    {
        rational_number(2147483647, 1) * rational_number(2, 1);
    }
    catch(out_of_range exc)
    {
        std::clog << exc.what() << "\n";
    }

    try
    {
        rational_number(5, 1) / rational_number(0, 5);
    }
    catch(division_by_zero exc)
    {
        std::clog << exc.what() << "\n";
    }
}