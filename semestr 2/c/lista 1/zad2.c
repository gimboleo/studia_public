#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

#define n 5

int kolejka[n];
int l = 0;          //Wskaznik na pierwszy element z lewej
int p = 0;          //Wskaznik na pierwsze wolne miejsce z prawej

bool isEmpty()
{
    if(l == p) return true;
    else return false;
}

int pop()
{
    if(isEmpty()) return 100;
    else
    {
        int x = kolejka[l];
        l = (l + 1) % n;
        return x;
    }
}

void push(int v)
{
    if((p + 1) % n != l)
    {
        kolejka[p] = v;
        p = (p + 1) % n;
    }
}

int main()
{
    assert(pop() == 100);
    assert(isEmpty() == true);
    
    push(1);
    assert(isEmpty() == false);

    push(2);
    push(3);
    push(4);
    pop();
    push(5);
    pop();
    pop();
    pop();
    printf("%d", pop());

    assert(isEmpty() == true);

    return 0;
}