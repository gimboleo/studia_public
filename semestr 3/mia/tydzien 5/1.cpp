#include <iostream>
using namespace std;


int n, m, l;
int aux[500001] = {0};
int res[500001], parent[500001], group[500001];


int find(int p)
{
    if (parent[p] == p) return p;
    parent[p] = find(parent[p]);
    return parent[p];
}


int main()
{
    cin >> n >> m;

    for (int i = 1; i <= n; i++) parent[i] = i;
    
    for (int i = 0; i < m; i++)
    {
        cin >> l;
        for (int j = 0; j < l; j++) cin >> group[j];
        for (int j = 1; j < l; j++) parent[find(group[j])] = find(group[0]);
    }

    for (int i = 1; i <= n; i++) aux[find(i)]++;
    for (int i = 1; i <= n; i++) cout << aux[find(i)] << " ";
}