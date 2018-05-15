#include <iostream>
using namespace std;

int main()
{
    cout << "Enter the numbers.\n";
    int amount = 0, value;
    while (cin >> value)
    {
        if (value <= 0)
        {
            amount++;
        }
    }
    cout << "Amount of all negative values read is " << amount << endl;
    return 0;
}