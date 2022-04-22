#include <iostream>
#include <algorithm>
using namespace std;

const int N = 30;
int n, u, r;
int a[N], b[N], k[N], p[N], a2[N];
long long res = LLONG_MIN;


void f(int depth, bool op)
{
    if ((u - depth) % 2 == 0)
    {
        long long aux = 0;
        for (int i = 0; i < n; i++) aux += a[i] * k[i];
        res = max(res, aux);
    }

    if (depth == u) return;

    int temp[N];
    for (int i = 0; i < n; i++) temp[i] = a[i];

    if (op)
    {
        int temp2[N];
        for (int i = 0; i < n; i++) temp2[i] = a[i] = temp[p[i] - 1] + r;
        f(depth + 1, false);
        for (int i = 0; i < n; i++) a[i] = temp2[i];
        f(depth + 1, true);
    }
    else
    {
        for (int i = 0; i < n; i++) a[i] = temp[i] ^ b[i];
        f(depth + 1, true);
    }
}


int main()
{
    cin >> n >> u >> r;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
    for (int i = 0; i < n; i++) cin >> k[i];
    for (int i = 0; i < n; i++) cin >> p[i];

    for (int i = 0; i < n; i++) a2[i] = a[i];
    f(0, 0);
    for (int i = 0; i < n; i++) a[i] = a2[i];
    f(0, 1);
    cout << res;
}