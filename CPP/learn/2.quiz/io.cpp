#include <iostream>
#include "io.h"

int readNumber()
{
    std::cout << "Number: ";
    int number {};
    std::cin >> number;
    return number;
}

void writeAnswer(int number)
{
    std::cout << "The answer is "  << number << '\n';
}