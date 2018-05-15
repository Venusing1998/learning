#include <iostream>

int main()
{
    int sum = 0;
    for(int i = 10; i > -1; --i)
    {
        sum += i;
    }
    std::cout << "Sum of 10 to 0 inclusive is " << sum << std::endl;
    return 0;    
}