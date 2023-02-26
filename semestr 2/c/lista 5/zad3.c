#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char* sorting(char* order, char* word, int order_len, int word_len)
{
    int counter[26] = {0};
    
    for (int i = 0; i < word_len; i++)
    {
        counter[*word - 'a']++;
        word++;
    }

    char *result = malloc(word_len + 1);
    int index = 0;

    for (int i = 0; i < order_len; i++)
    {
        for (int j = 0; j < counter[*order - 'a']; j++)
        {
            result[index] = *order;
            index++;
        }
        order++;
    }

    result[index] = '\0';
    return result;
}

int main()
{   
    char order[27];
    int order_length;
    scanf("%d %s", &order_length, order);

    char word[1000001];
    int word_length;
    scanf("%d %s", &word_length, word);

    char* result = sorting(order, word, order_length, word_length);
    printf("%s", result);

    return 0;
}