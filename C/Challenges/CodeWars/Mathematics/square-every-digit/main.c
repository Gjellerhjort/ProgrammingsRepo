#include <stdio.h>
#include <limits.h>

unsigned long long square_digits (unsigned n)
{
    long long int digit;
    long long int sum;
    long long int i = 1;
    while (n)
    {
        digit = n % 10;
        n =  n / 10;
        
    }
	return sum;
}

static void do_test (unsigned n, unsigned long long expected)
{
  unsigned long long actual = square_digits(n);
  printf("for n = %u, expected %llu, but got %llu\n",n,expected,actual);
}

int main()
{
    do_test(      3212u,                9414ull);
	do_test(      2112u,                4114ull);
	do_test(         0u,                   0ull);
	do_test(       999u,              818181ull);
	do_test(     10001u,               10001ull);
	do_test(3210987654u,    9410816449362516ull);
	do_test(3999999999u, 9818181818181818181ull); // :p
	do_test(   UINT_MAX,  164811681364948125ull);
}