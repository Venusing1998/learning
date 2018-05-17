#include <iostream>
using namespace std;

int main()
{
    int base, exponent, result = 1;
    cout << "Enter base: " << endl;
    cin >> base;
    cout << "Enter exponent: " << endl;
    cin >> exponent;
    for (int cnt = 0; cnt != exponent; ++cnt)
    {
        result *= base;
    }
    cout << base << " raised to the power of " << exponent << ": " << result << endl;
    return 0;
}
