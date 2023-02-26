#include "polynomial.cpp"
#include <fstream>

int main()
{   
    polynomial d = polynomial();
    d.print();
    cout << "\n";
    
    double a[3] = {1, 5, 9};
    polynomial k(2, a);
    k.print();

    polynomial k2 = k;
    k2.print();

    polynomial k3 = move(k2);
    k3.print();
    cout << "\n";

    polynomial p{-1.5, 2, -3, 4, -5.6};
    p.print();

    ifstream test;
    test.open("test.txt");
    test >> p;
    test.close();
    p.print();

    ofstream test2;
    test2.open("test2.txt");
    test2 << p;
    test2.close();
    cout << "\n";

    polynomial k4{1, 5, -9};
    polynomial res = k + k4;
    res.print();                             //10x + 2

    k4 = polynomial{1, 5, -9, 10};
    res = k + k4;
    res.print();                            //10x^3 + 10x + 2
    cout << "\n";

    res = k - k4;
    res.print();                            //-10x^3 + 18x^2
    cout << "\n";

    k4 = polynomial{2};
    res = k * k4;
    res.print();                            //18x^2 + 10x + 2
    res = k * 2;
    res.print();                            //18x^2 + 10x + 2
    k4 = polynomial{2, 5, -1, 3};
    res = k4 * k;
    res.print();                            //27x^5 + 6x^4 + 43x^3 + 42x^2 + 15x + 2
    cout << "\n";
    
    k4 += k;
    k4.print();                             //3x^3 + 8x^2 + 10x + 3
    k4 -= k;
    k4.print();                             //3x^3 - x^2 + 5x + 2;
    k4 *= k;
    k4.print();                             //27x^5 + 6x^4 + 43x^3 + 42x^2 + 15x + 2
    k4 *= 10;
    k4.print();                             //270x^5 + 60x^4 + 430x^3 + 420x^2 + 150x + 20
    cout << "\n";

    cout << k(5) << "\n";                   //251
    cout << k4[2] << "\n\n";                //420s

    k4.set_coefficient(2, 5);
    k4.print();                             //270x^5 + 60x^4 + 430x^3 + 5x^2 + 150x + 20    
    cout << k4.get_degree() << "\n\n";      //5

    return 0;
}