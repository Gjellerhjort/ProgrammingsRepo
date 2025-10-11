#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int size;

    printf("Enter the size of array: ");
    scanf("%d", &size);
    // allocate memory for array size given by user
    int *array = (int *)malloc(size * sizeof(int));
    if (array == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }
    // user array input
    printf("Enter %d integers:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &array[i]);
    }

    // display elements in array
    printf("The array elements are: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    // free allocated memory
    free(array);

    // trying to access free'd memory
    printf("%d", array[0]);

    array = NULL; // avoid dangling pointer
    return 0;
}
