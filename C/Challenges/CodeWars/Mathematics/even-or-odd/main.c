#include <stdio.h>
#include<stdlib.h>

const char* even_or_odd(int number)
{
    // return a statically allocated string,
    // for example a string literal
    /*
    return number%2==1 ? "Odd" : "Even";
    */
    if (number%2==1)
    {
        return "Even";
    } else
    {
        return "Odd";
    }

}

static void do_test (int number, const char *expected)
{
	const char *actual = even_or_odd(number);
    printf("Number: %d Expected: %s Returned: %s\n", number,expected,actual);
    if (expected != actual)
    {
        printf("Failed:(");
        exit(1);
    }
}

int main()
{
    do_test(  0, "Even");
    do_test(  1, "Odd");
	do_test( 21, "Odd");
    do_test(  2, "Even");
	do_test(100, "Even");
    do_test(  -1, "Odd");
	do_test( -21, "Odd");
    do_test(  -2, "Even");
	do_test(-100, "Even");
}

