#include <iostream>
using namespace std;

int main()
{
    int sum = 0;
    for (int i = 50; i < 101; ++i)
    {
        sum += i;
    }
    cout << "Sum of 50 to 100 inclusive is " << sum << "." << endl;
    return 0;
}