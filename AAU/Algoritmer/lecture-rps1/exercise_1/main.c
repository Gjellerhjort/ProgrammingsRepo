#define _POSIX_C_SOURCE 199309L
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int l_search(int* arr, int n, int v){
    for (int i = 0; i < n; i++){
        if (arr[i] == v){
            return i;
        }
    }
    return -1;
}

int b_search(int* arr, int left, int right, int target){
    while (left <= right){
        int mid = (left + right) / 2;
        if (arr[mid] == target){
            return mid;
        } else if(arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int quad_search(int* arr, int left, int right, int target){
    while (left <= right){
        int mid_1 = left + (right - left) / 4;
        int mid_2 = left + 2 * (right - left) / 4;
        int mid_3 = left + 3 * (right - left) / 4;

        if (arr[mid_1] == target) return mid_1;
        if (arr[mid_2] == target) return mid_2;
        if (arr[mid_3] == target) return mid_3;

        if(target < arr[mid_1]) {
            right = mid_1 - 1;
        } else if (target < arr[mid_2]) {
            left = mid_1 + 1;
            right = mid_2 - 1;
        } else if (target < arr[mid_3]) {
            left = mid_2 + 1;
            right = mid_3 -1;
        } else {
            left = mid_3 + 1;
        }
    }
    return -1;
}

void print_arr(int arr[], int length){
    for (int i = 0; i < length; i++) {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}

void insertionsort(int* A, int length){
    int num, i;
    for (int j = 1; j <= length - 1; j++) {
        num = A[j];
        i = j - 1;

        while (i >= 0 && A[i] > num) {
            A[i + 1] = A[i];
            i -= 1;
        }
        A[i + 1] = num;
    }
}

void generate_arr(int* arr, int length){
    for (int i = 0; i < length; i++) {
        arr[i] = (rand() % 100) + 1;
    }
}

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main(void){
    srand((unsigned int)time(NULL));
    int length = 10000000; // 10 million
    int target = 105;
    double sum = 0;
    struct timespec start, end;
    double ms;

    int *A = malloc(length * sizeof(int));
    if (A == NULL) {
        fprintf(stderr, "Memory allocation failed!\n");
        return 1;
    }

    for (int i = 0; i < 100; i++){
        printf("Iteration %d\n", i);
        generate_arr(A, length);
        qsort(A, length, sizeof(int), compare);

        clock_gettime(CLOCK_MONOTONIC, &start);
        int result = b_search(A, 0, length - 1, target);
        clock_gettime(CLOCK_MONOTONIC, &end);

        ms = (end.tv_sec - start.tv_sec) * 1000.0 +
                 (end.tv_nsec - start.tv_nsec) / 1e6;

        sum += ms;
        printf("found at index %d\n", result);
        printf("search took %f ms\n", ms);
    }

    sum /= 100.0;
    printf("Average time: %f ms\n", sum);

    free(A);
    return 0;
}
