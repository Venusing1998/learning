#include <iostream>
using namespace std;

int main()
{
    cout << "Enter two numbers: " << endl;
    int v1, v2;
    cin >> v1 >> v2;
    int lower, upper;
    lower = v1;
    upper = v2;
    if (v1 >= v2)
    {
        upper = v1;
        lower = v2;
    }
    cout << "Values of " << lower << " to " << upper << " inclusive are: " << endl;
    for (; lower <= upper; ++lower)
    {
        cout << lower << " ";
    }
    cout << endl;
    return 0;
}
