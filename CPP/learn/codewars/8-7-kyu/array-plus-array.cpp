#include <vector>
#include <iostream>

int arrayPlusArray(std::vector<int> a, std::vector<int> b) {
    int total{};

    for( int i : a ) total += i;
    for( int i : b ) total += i;

    return total;
}

int main()
{
    std::vector<int> vector1{1, 2, 3};
    std::vector<int> vector2{3, 2, 1};

    std::cout << arrayPlusArray(vector1, vector2) << '\n';

    return 0;
}

