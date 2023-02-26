#include <stdio.h>
#include <assert.h>

int my_strcmp(const char *str1, const char *str2) 
{
    const char *s1 = str1;
    const char *s2 = str2;
    int difference;

    while (*s1 || *s2) 
    {
        difference = *s1 - *s2;
        if (difference != 0) return difference;
        s1++;
        s2++;
    }

    return 0;
}

int my_strncmp(const char *str1, const char *str2, size_t num)
{
    const char *s1 = str1;
    const char *s2 = str2;
    int difference;
    int i = 0;

    while ((*s1 || *s2) && i < num)
    {
        difference = *s1 - *s2;
        if (difference != 0) return difference;
        s1++;
        s2++;
        i++;
    }

    return 0;
}

int main()
{
    assert(my_strcmp("", "") == 0);
    assert(my_strcmp("string", "string") == 0);
    assert(my_strcmp("abcd", "bcde") == 'a' - 'b');
    assert(my_strcmp("string", "strinh") == 'g' - 'h');
    assert(my_strcmp("", "string") == -'s');

    assert(my_strncmp("abcd", "abcd", 4) == 0);
    assert(my_strncmp("stringa", "stringb", 6) == 0);
    assert(my_strncmp("strinha", "stringb", 6) == 'h' - 'g');
    assert(my_strncmp("abc", "cde", 0) == 0);
    assert(my_strncmp("", "", 5) == 0);
}