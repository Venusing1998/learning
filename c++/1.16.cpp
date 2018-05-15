#include <iostream>

int main()
{
    std::cout << "Enter two numbers: " << std::endl;
    int v1, v2;
    std::cin >> v1 >> v2;
    if (v1 >= v2)
    {
        std::cout << "The upper number of two numbers is " << v1 << std::endl;
    }
    else
    {
        std::cout << "The upper number of two numbers is " << v2 << std::endl;
    }
    return 0;
}