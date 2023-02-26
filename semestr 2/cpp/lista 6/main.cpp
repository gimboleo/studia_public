#include "bitarray.cpp"
#include <iostream>
using namespace computations;

int main()
{
    std::cout << bitarray(10) << "\n";
    bitarray t = bitarray(45ull);
    std::cout << t << "\n";
    std::cout << bitarray(t) << "\n";
    bitarray w(bitarray{1, 0, 1, 1, 0, 0, 0, 1});
    std::cout << bitarray(w) << "\n\n";
    
    bitarray a(10);
    a[1] = 1;
    a[5] = a[7] = a[1];
    std::cout << a << "\n\n";

    bitarray b(10);
    std::cin >> b;
    std::cout << b << "\n\n";

    bitarray c(4);
    for (int i = 0; i <= 3; i++) c[i] = i % 2;
    std::cout << c << "\n\n";

    bitarray d{0, 1, 0, 1};
    bitarray e{0, 0, 1, 1};
    std::cout << (d | e) << "\n";
    std::cout << (d & e) << "\n";
    std::cout << (d ^ e) << "\n";
    std::cout << !d << "\n\n";

    d |= e;
    std::cout << d;
}