#include <stdio.h>
#include <string.h>
#include <assert.h>

char *my_strcpy(char *destination, const char *source)
{
    char *d = destination;
    const char *s = source;

    while (*s) 
    {
        *d = *s;
        d++;
        s++;
    } 
    *d = '\0';

    return destination;
}

char *my_strcat(char *destination, const char *source)
{
    char *d = destination;
    const char *s = source;

    while (*d) d++;
    while (*s)
    {
        *d = *s;
        d++;
        s++;
    }
    *d = '\0';

    return destination;
}

int main()
{
    char str[100] = "";
    assert(!strcmp(my_strcpy(str, ""), ""));
    assert(!strcmp(my_strcpy(str, "xd"), "xd"));
    assert(!strcmp(my_strcpy(str, "abecadlo z nieba spadlo"), "abecadlo z nieba spadlo"));

    char str1[100] = "";
    assert(!strcmp(my_strcat(str1, ""), ""));
    assert(!strcmp(my_strcat(str1, "xd "), "xd "));
    assert(!strcmp(my_strcat(str1, "dx "), "xd dx "));
    assert(!strcmp(my_strcat(str1, "abc"), "xd dx abc"));

    return 0;
}