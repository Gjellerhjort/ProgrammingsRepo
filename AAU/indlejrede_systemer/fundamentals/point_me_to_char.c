#include <stdio.h>

int main() {
    char *chrPtr;
    char myChar;
    printf("Give me a char: ");
    myChar = getchar();
    chrPtr = &myChar;
    printf("The addres where char is stored: %X\n", chrPtr);
    return 0;
}
