#include <stdio.h>
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

char int_to_str(int val) {
    if (val >= 0 && val <= 9)
    {
        return '0' + val;
    }

    else if (val >= 10 && val <= 15)
    {
        return 'A' - 10 + val;
    }

    return '0';
}

int str_to_int(char ch) {
    if (ch >= '0' && ch <= '9')
    {
        return ch - '0';
    }
    
    else if (ch >= 'A' && ch <= 'F')
    {
        return 10 + ch - 'A';
    } 

    return 0;
}

char *add(char *res, char *arg1, char *arg2, int n) {
    int len1 = strlen(arg1);
    int len2 = strlen(arg2);
    int reszta = 0;
    int ind1 = 0;
    int ind2 = 0;
    int temp1;
    int temp2;
    int x;
    int i;

    reverse(arg1);
    reverse(arg2);

    for (i = 0; i <= n; i++)
    {
        if (ind1 < len1)
        {
            temp1 = str_to_int(arg1[ind1]);
            ind1++;
        }
        else temp1 = 0;

        if (ind2 < len2)
        {
            temp2 = str_to_int(arg2[ind2]);
            ind2++;
        }
        else temp2 = 0;

        x = temp1 + temp2 + reszta;
        reszta = x / 16;
        x = x % 16;
        res[i] = int_to_str(x);

        if (ind1 >= len1 && ind2 >= len2) break;
    }

    if (reszta > 0 && i >= n - 1)
    {
        res[0] = '\0';
        return res;
    }

    if (reszta != 0)
    {   
        i++;
        res[i] = int_to_str(reszta);
    }
    
    while (res[i] == '0' && i > 0) i--;
    res[i+1] = '\0';

    return reverse(res);
}

char *sub(char *res, char *arg1, char *arg2, int n) {
    int len1 = strlen(arg1);
    int len2 = strlen(arg2);
    int reszta = 0;
    int ind1 = 0;
    int ind2 = 0;
    int temp1;
    int temp2;
    int x;
    int i;

    reverse(arg1);
    reverse(arg2);

    for (i = 0; i <= n; i++)
    {
        if (ind1 < len1)
        {
            temp1 = str_to_int(arg1[ind1]);
            ind1++;
        }
        else temp1 = 0;

        if (ind2 < len2)
        {
            temp2 = str_to_int(arg2[ind2]);
            ind2++;
        }
        else temp2 = 0;

        x = temp1 - temp2 - reszta;
        if (x < 0) 
        {
            res[i] = int_to_str(16 + x);
            reszta = 1;
        }
        else 
        {
            res[i] = int_to_str(x);
            reszta = 0;
        }

        if (x < 0 && ind1 >= len1)
        {
            res[0] = '\0';
            return res;
        }

        if (ind1 >= len1 && ind2 >= len2) break;
    }

    while (res[i] == '0' && i > 0) i--;
    res[i+1] = '\0';

    return reverse(res);
}

int main() {
    int n;
    int m;
    char operator[4];

    scanf("%d %d", &n, &m);

    char arg1[n+1];
    char arg2[n+1];
    char res[n+1];

    for (int i = 0; i < m; i++)
    {
        scanf("%s %s %s", operator, arg1, arg2);

        if (!strcmp(operator, "ADD"))
        {
            add(res, arg1, arg2, n);

            if (!strcmp(res, "")) printf("OVERFLOW\n");
            else printf("%s\n", res);
        }
        else if (!strcmp(operator, "SUB"))
        {
            sub(res, arg1, arg2, n);

            if (!strcmp(res, "")) printf("UNDERFLOW\n");
            else printf("%s\n", res);
        }
    }

    return 0;
}