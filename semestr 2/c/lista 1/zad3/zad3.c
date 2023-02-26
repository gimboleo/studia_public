#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

char *reverse(char *str)
{
    char res[81];
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


int main()
{
    char test1[] = "bat man";
    assert(!strcmp("nam tab", reverse(test1)));

    char test2[] = "";
    assert(!strcmp("", reverse(test2)));

    char test3[] = "Kocham C";
    assert(!strcmp("C mahcoK", reverse(test3)));


    char T[81];

    while (gets(T)) {
        printf("%s\n", reverse(T));
    }

    return 0;
}
