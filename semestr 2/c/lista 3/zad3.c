#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *reverse(char *str)
{
    char res[1 + strlen(str)];
    int i = strlen(str);
    int k = 0;

    while (--i >= 0) {
        res[k++] = str[i];
    }
    
    res[k] = '\0';

    while (++i <= k) {
        str[i] = res[i];
    }
    
    return str;
}

long evaluate(char T[]) 
{
    int l = strlen(T);
    long stack[l];
    int i = -1;

    for (int j = 0; j < l; j++) 
    {
        char c = T[j];

        if ('0' <= c && c <= '9') 
        {
            i++;
            stack[i] = c - '0';
        } 
        else 
        {
            long val1 = stack[i];
            i--;
            long val2 = stack[i];
            switch (c) 
            {
                case '+':
                    stack[i] = val1 + val2;
                    break;
                case '-':
                    stack[i] = val1 - val2;
                    break;
                case '*':
                    stack[i] = val1 * val2;
                    break;
            }
        }
    }
    return stack[0];
}

int main() 
{
    int n;
    scanf("%d", &n);
    char T[n + 1];
    scanf("%s", T);
    reverse(T);
    printf("%li", evaluate(T));

    return 0;
}