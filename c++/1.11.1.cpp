#include <iostream>

int main()
{
    int sum = 0;
    int i = 10;
    while (i > -1)
    {
        sum += i;
        --i;
    }
    std::cout << "Sum of 10 to 0 incluvise is " << sum << std::endl;
    return 0;
}