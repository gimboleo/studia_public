#include <stdbool.h>
#include <stdio.h>
#include <ctype.h>

bool check_vovels(int c)
{
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y');
}

bool check_punctuation(int c)
{
    return (c == ',' || c == '.' || c == ':' || c == '!' || c == '?');
}

int main()
{
    int characters = 0;
    int letters = 0;
    int digits = 0;
    int words = 0;
    int whitespaces = 0;
    int vowels = 0;
    int consonants = 0;
    int uppercases = 0;
    int lowercases = 0;
    int punctuation_marks = 0;
    bool word = false;
    int c;

    while((c = getchar()) != EOF)
    {
        characters++;

        if (isalpha(c))
        {
            letters++;

            if (islower(c)) lowercases++;
            else uppercases++;

            c = tolower(c);
            if (check_vovels(c)) vowels++;
            else consonants++;

            if(!word)
            {
                word = true;
                words++;
            }
        }
        else
        {
            word = false;

            if (isdigit(c)) digits++;
            else if (isspace(c)) whitespaces++;
            else if (check_punctuation(c)) punctuation_marks++;
        }
    }


    printf("Characters: %d\n", characters);
    printf("Letters: %d\n", letters);
    printf("Digits: %d\n", digits);
    printf("Words: %d\n", words);
    printf("Whitespaces: %d\n", whitespaces);
    printf("Vowels: %d\n", vowels);
    printf("Consonants: %d\n", consonants);
    printf("Uppercases: %d\n", uppercases);
    printf("Lowercases: %d\n", lowercases);
    printf("Punctuation marks: %d\n", punctuation_marks);

    return 0;
}