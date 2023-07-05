#include <stdio.h>

int main(int argc, char *argv[]) {
    if ( argc == 2) {
        printf("The argument is %s", argv[1]);
    }
    else if (argc > 3){
        printf("Too many arguments\n");
    }
    else {
        printf("one argument expected.\n");
    }
}