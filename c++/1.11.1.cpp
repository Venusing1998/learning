#include <iostream>

int main()
{
    int i = 10;
    while (i > -1)
    {
        std::cout << i << "\n";
        --i;
    }
    std::cout << std::endl;
    return 0;
}