#include <iostream>
using namespace std;

int main()
{
    int v1 = 1000, v2 = 2000;
    cout << "Values of " << v1 << " to " << v2 << " inclusive are: " << endl;
    for (; v1 < 2001; ++v1)
    {
        cout << v1 << " ";
        if (v1 % 10 == 9)
        {
            cout << endl;
        }
    }
    cout << endl;
    return 0;
}
