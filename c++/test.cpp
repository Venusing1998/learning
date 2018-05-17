#include <iostream>

int gcd(int v1, int v2)
{
	while (v2)
		{
			int temp = v2;
			v2 = v1 % v2;
			v1 = temp;
		}
	return v1;
}

int main()
{
	std::cout << "Enter two values: \n";
	int i, j;
	std::cin >> i >> j;
	std::cout << "gcd: " << gcd(i, j) << std::endl;
}
