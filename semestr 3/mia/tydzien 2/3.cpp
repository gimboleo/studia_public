#include <iostream>
using namespace std;


int main()
{
    int vs[4001], ds[4001], ps[4001];
    int res[4001];
    int n;
    int total = 0;
    int hall_screams;
    int scream;
    int calm_flag;


    cin >> n;    
    for (int i = 1; i <= n; i++) cin >> vs[i] >> ds[i] >> ps[i];


    for (int i = 1; i <= n; i++)
    {
        if (ps[i] < 0) continue;

        res[total++] = i;
        hall_screams = 0;
        scream = vs[i];

        for (int j = i + 1; j <= n; j++)
        {
            calm_flag = 0;

            if (ps[j] >= 0)
            {
                calm_flag = 1;
                if (scream > 0) ps[j] -= scream--;
            }

            if (ps[j] >= 0) ps[j] -= hall_screams;
            if (ps[j] < 0 && calm_flag == 1) hall_screams += ds[j];
        }
    }


    cout << total << "\n";
    for (int i = 0; i < total; i++) cout << res[i] << " ";
}