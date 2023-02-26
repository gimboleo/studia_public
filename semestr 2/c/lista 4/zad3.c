#include <stdio.h>
#include <stdlib.h>

void reverse(int *tab, int size);
void swap_pointers(int **tabs, int pos1, int pos2, int *sizes);
void swap_entries(int *entries, int e1, int e2);
void read_all(int **tab, int *sizes, int n);
void print_all(int **tab, int *sizes, int n);
void free_all(int **tab, int *sizes, int n);

int main() {
    char command;
    int n;
    int **tab;
    int *sizes;

    scanf("%d", &n);

    tab = malloc(n * sizeof(int *));
    sizes = malloc(n * sizeof(int));
    read_all(tab, sizes, n);

    scanf(" %command", &command);

    while (command != 'k') {
        if (command == 'z') {
            int m, k;
            scanf("%d %d", &m, &k);
            swap_pointers(tab, m, k, sizes);
        } else if (command == 'p') {
            int i, k, l;
            scanf("%d %d %d", &i, &k, &l);
            swap_entries(tab[i], k, l);
        } else if (command == 'o') {
            int o;
            scanf("%d ", &o);
            reverse(tab[o], sizes[o]);
        }

        scanf(" %command", &command);
    }

    print_all(tab, sizes, n);
    free_all(tab, sizes, n);

    return 0;
}

void swap_entries(int *entries, int e1, int e2) {
    int temp;
    temp = entries[e1];
    entries[e1] = entries[e2];
    entries[e2] = temp;
}

void swap_pointers(int **tabs, int pos1, int pos2, int *sizes) {
    int *temp = tabs[pos1];
    tabs[pos1] = tabs[pos2];
    tabs[pos2] = temp;
    swap_entries(sizes, pos1, pos2);
}

void reverse(int *tab, int size) {
    int temp;
    for (int i = 0; i < size/2; i++)
    {
        temp = tab[i];
        int x = size - i - 1;
        tab[i] = tab[x];
        tab[x] = temp;
    }
}

void read_all(int **tab, int *sizes, int n) {
    int s;
    for (int i = 0; i < n; i++) {
        scanf("%d", &s);

        sizes[i] = s;
        tab[i] = malloc(s * sizeof(int));

        for (int j = 0; j < s; j++) {
            scanf("%d", &(tab[i][j]));
        }
    }
}

void print_all(int **tab, int *sizes, int n) {
    for (int i = 0; i < n; i++) 
    {
        for (int k = 0; k < sizes[i]; k++) printf("%d ", tab[i][k]);
        printf("\n");
    }
}

void free_all(int **tab, int *sizes, int n) {
    for (int i = 0; i < n; i++) {
        free(tab[i]);
    }

    free(tab);
    free(sizes);
}