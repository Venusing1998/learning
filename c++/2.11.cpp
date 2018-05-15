#include <iostream>
using namespace std;

int main()
{
    int value, pow, result = 1;
    cout << "Enter value: " << endl;
    cin >> value;
    cout << "Enter pow: " << endl;
    cin >> pow;
    for (int cnt = 0; cnt != pow; ++cnt)
    {
        result *= value;
    }
    cout << value << " raised to the power of " << pow << ": " << result << endl;
    return 0;
}