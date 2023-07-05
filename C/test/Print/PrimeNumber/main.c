#include <stdio.h>

void checkPrime(int num)
{
    if (num == 2 || num % 2 != 0 && num > 1)
    {
        printf("The number %d is a prime number\n", num);
    }
    else  {
        printf("The number %d is not a prime number\n", num);
    }
}

int main(int argc, char *argv[]) {
    int num;
    /*
    printf("Write a number:");
    scanf("%d", &num);
    */
    for (int i = 0; i<100; i++)
    {
        checkPrime(i);
    }

    return 0;
}