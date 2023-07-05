#include <stdio.h>

FILE *fptr;

int main()
{
    fptr = fopen("file.txt", "r");
    
    char myString[100];

    fgets(myString, 100, fptr);

    printf("%s", myString);

    fclose(fptr);
}