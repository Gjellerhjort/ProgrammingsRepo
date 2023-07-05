#include <stdio.h>

int main() {
    int num1;
    int num2;

    printf("Enter number 1: ");

    if (scanf("%d", &num1) != 1) {
        printf("Invalid input for number 1. Exiting...\n");
        return 1;
    }

    printf("Enter number 2: ");

    if (scanf("%d", &num2) != 1) {
        printf("Invalid input for number 2. Exiting...\n");
        return 1;
    }
    int sum = num1 + num2;
    printf("Result is: %d", sum);
    return 0;
}