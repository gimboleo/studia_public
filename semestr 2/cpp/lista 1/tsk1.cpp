using namespace std;
#include <iostream>
#include <vector>
#include <string>

string arabic2roman (int x)
{
    const vector<pair<int, string>> rome = {
        {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"}, {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
    };

    int n = x;
    int temp;
    int i = 0;
    string res = "";
    
    while(n > 0)
    {
        temp = n / rome[i].first;
        for (int j = 0; j < temp; j++) {
            res.append(rome[i].second);
            n = n - rome[i].first;
        }
        i++;
    }
    return res;
}

int main(int argc, const char* argv[])
{
    int x;

    for (int i = 1; i < argc; i++)
    {
        try
        {
            x = stoi(argv[i]);
        }
        catch (invalid_argument)
        {
            clog << "Invalid argument" << endl;
            continue;
        }
        catch (out_of_range)
        {
            clog << "Argument out of range" << endl;
            continue;
        }
        if (x < 1 || x > 3999)
        {
            clog << "Argument out of range" << endl;
            continue;
        }

        cout << arabic2roman(x) << endl;
    }

    return 0;
}
