#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

bool isTriangular(int n)
{
    int sum = 0;
    int i;

    for(i = 0; i <= n; i++)
    {
        sum = sum + i;
        if(sum == n) return true;
    }
    return false;
}

int nearestTriangular(int n)
{
    int dist = 0;
    int smaller = 0;
    int bigger = 0;
    int i = 1;
    int result;

    if(isTriangular(n) == true) return n;

    while(bigger < n)
    {
        smaller = bigger;
        bigger = bigger + i;
        i++;
    }

    dist = n - smaller;
    if(dist > bigger - n) result = bigger;
    else result = smaller;

    return result;
}

int main() 
{
    assert(isTriangular(0) == true);
    assert(isTriangular(1) == true);
    assert(isTriangular(2) == false);
    assert(isTriangular(3) == true);
    assert(isTriangular(4) == false);
    assert(isTriangular(5) == false);
    assert(isTriangular(6) == true);
    assert(isTriangular(210) == true);

    assert(nearestTriangular(0) == 0);
    assert(nearestTriangular(1) == 1);
    assert(nearestTriangular(2) == 1);
    assert(nearestTriangular(3) == 3);
    assert(nearestTriangular(4) == 3);
    assert(nearestTriangular(5) == 6);
    assert(nearestTriangular(6) == 6);
    assert(nearestTriangular(8) == 6);

    return 0;
}