#include <iostream>
using namespace std;

int main()
{
    cout << "Enter two numbers: " << endl;
    int v1, v2;
    cin >> v1 >> v2;
    if (v1 >= v2)
    {
        cout << "The upper number of two numbers is " << v1 << endl;
    }
    else
    {
        cout << "The upper number of two numbers is " << v2 << endl;
    }
    return 0;
}