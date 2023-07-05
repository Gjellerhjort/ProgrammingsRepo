#include <stdio.h>

FILE *fptr;

int main()
{
    fptr = fopen("file.txt", "w");

    fprintf(fptr, "jeg skrev lige det her i filen");

    fprintf(fptr, "\nNy linje ja tak");

    fclose(fptr);
}