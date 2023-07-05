#include <stdbool.h>
#include <stdio.h>

void swap(int* xp, int* yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void bubbleSort(int arr[], int n) 
{
    int i, j;
    bool swapped;
    for (int i = 0; i < n-1; i++)
    {
        swapped = false;
        for (int j; j < n - i -  1; j++)    {
            if (arr[j] > arr[j+1]) {
                swap(&arr[j], &arr[j+1]);
                swapped = true;
            }
        }
        if (swapped == false)
        {
            break;
        }
    }
}

void printArr(int arr[], int size)
{
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
}

int main()
{
        int arr[] = { 10, 20, 30, 53, 32, 40, 4, 8, 3029, 3 };
        int n = sizeof(arr) / sizeof(arr[0]);

        bubbleSort(arr, n);
        printArr(arr, n);
}