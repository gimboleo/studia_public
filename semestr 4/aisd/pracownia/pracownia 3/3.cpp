#include <stdio.h>
#include <algorithm>

// preprocessing generated in python
bool compability[8][8][8] = { { {true, true, true, true, true, true, true, true}, {true, true, true, true, false, false, false, false}, {true, true, true, true, true, true, true, true}, {true, true, true, true, false, false, false, false}, {true, false, true, false, true, false, true, false}, {true, false, true, false, false, false, false, false}, {true, false, true, false, true, false, true, false}, {true, false, true, false, false, false, false, false} },
                              { {true, true, false, false, true, true, false, false}, {true, true, false, false, false, false, false, false}, {true, true, false, false, true, true, false, false}, {true, true, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false} },
                              { {true, false, true, false, false, false, false, false}, {true, false, true, false, false, false, false, false}, {true, false, true, false, false, false, false, false}, {true, false, true, false, false, false, false, false}, {true, false, true, false, false, false, false, false}, {true, false, true, false, false, false, false, false}, {true, false, true, false, false, false, false, false}, {true, false, true, false, false, false, false, false} },
                              { {true, false, false, false, false, false, false, false}, {true, false, false, false, false, false, false, false}, {true, false, false, false, false, false, false, false}, {true, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false} },
                              { {true, true, false, false, true, true, false, false}, {false, false, false, false, false, false, false, false}, {true, true, false, false, true, true, false, false}, {false, false, false, false, false, false, false, false}, {true, false, false, false, true, false, false, false}, {false, false, false, false, false, false, false, false}, {true, false, false, false, true, false, false, false}, {false, false, false, false, false, false, false, false} },
                              { {true, true, false, false, true, true, false, false}, {false, false, false, false, false, false, false, false}, {true, true, false, false, true, true, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false} },
                              { {true, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {true, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {true, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {true, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false} },
                              { {true, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {true, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false}, {false, false, false, false, false, false, false, false} } };

short int set_bits[8] = {0, 1, 1, 2, 1, 2, 2, 3};





int main() {
    int n, temp, temp2, temp3;
    char input[2000000][3];
    char masks[2000000];
    int dp[2][8][8] = {0};
    char prev[2000000][8][8];

    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        scanf("%s", input[i]);
        temp = 0;
        for (short j = 0; j < 3; j++) {
            temp <<= 1;
            if (input[i][j] == 'x') temp |= 1;
        }
        masks[i] = temp;
    }



    for (int i = n - 1; i >= 0; i--) {
        for (short j = 0; j < 8; j++) {
            for (short k = 0; k < 8; k++) {
                for (short l = 0; l < 8; l++) {
                    if (!(masks[i] & l) && compability[j][k][l]) {
                        temp = dp[i % 2][j][k] + set_bits[l];
                        if (temp > dp[(i + 1) % 2][k][l]) {
                            dp[(i + 1) % 2][k][l] = temp;
                            prev[i][k][l] = j; 
                        }
                    }
                }
            }
        }
        for (short x = 0; x < 8; x++) {
            for (short y = 0; y < 8; y++) dp[i % 2][x][y] = 0;
        }
    }
    
    int res = 0;
    for (short i = 0; i < 8; i++) {
        for (short j = 0; j < 8; j++) {
            if (dp[1][i][j] >= res) {
                res = dp[1][i][j];
                temp = i;
                temp2 = j;
            }
        }
    }



    printf("%d\n", res);

    int i = 0;
    do {
        for (short j = 2; j >= 0; j--) {
            if (masks[i] & (1 << j)) printf("%c", 'x');
            else if (temp2 & (1 << j)) printf("%c", 'S');
            else printf("%c", '.');
        }
        printf("\n");
        temp3 = temp;
        temp = prev[i][temp][temp2];
        temp2 = temp3;
    } while (i++ < n - 1);

    return 0;
}