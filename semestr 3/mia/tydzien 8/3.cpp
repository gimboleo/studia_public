#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")


#include <algorithm>
#include <iostream>
using namespace std;


int n, g, res, aux;
int a[300001], c[15000001];
int nn[15000001] = {0};


int main()
{
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
        g = __gcd(a[i], g);
    }

    for (int i = 1; i <= n; i++) c[a[i] / g]++;

    for (int i = 2; i < 15000001; i++)
    {
        if (!nn[i])
        {
            aux = 0;
            for (int j = i; j < 15000001; j += i)
            {
                nn[j] = 1;
                aux += c[j];
            }
            res = max(res, aux);
        }
    }

    cout << (res != 0 ? n - res : -1);
}