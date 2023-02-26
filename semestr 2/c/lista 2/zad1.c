#include <stdio.h>
#include <assert.h>

void rotate(int arr[], size_t n, size_t k) {
    int i;
    int temp[n];
    for (i = 0; i < n; i++)
    {
        temp[i] = arr[(i+k)%n]; 
    }
    for (i = 0; i < n; i++)
    {
        arr[i] = temp[i];
    }
}

void print(int arr[], size_t n) {
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d", arr[i]);
    }
    printf("\n");
}


int main() {
    int arr1[] = {1};
    rotate(arr1, 1, 20);
    assert(arr1[0] == 1);
    
    int arr[] = {1, 2, 3, 4};
    rotate(arr, 4, 1);
    assert(arr[0] == 2 && arr[1] == 3 && arr[2] == 4 && arr[3] == 1);

    rotate(arr, 4, 0);
    assert(arr[0] == 2 && arr[1] == 3 && arr[2] == 4 && arr[3] == 1);

    rotate(arr, 4, 4);
    assert(arr[0] == 2 && arr[1] == 3 && arr[2] == 4 && arr[3] == 1);

    rotate(arr, 4, 9);
    assert(arr[0] == 3 && arr[1] == 4 && arr[2] == 1 && arr[3] == 2); 
}