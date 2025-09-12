#include <stdio.h>
#include "insert_sort.h"

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++) {
        printf("%d",arr[i]);
        if (i < size - 1) {
            printf(",");
        }
    }
    printf("\n");
}

int main() 
{
    int arr[] = {10,2,3,4,1,5,6};
    insertionSort(arr, sizeof(arr)/sizeof(arr[0]));
    printArray(arr, sizeof(arr)/sizeof(arr[0]));
}
