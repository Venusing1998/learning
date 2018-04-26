#include <stdio.h>

int main()
{
    int a = 21;
    int b = 10;
    int c;

    c = a + b;
    printf("The value of line1 - c is %d\n", c);
    c = a - b;
    printf("The value of line2 - c is %d\n", c);
    c = a * b;
    printf("The value of line3 - c is %d\n", c);
    c = a / b;
    printf("The value of line4 - c is %d\n", c);
    c = a % b;
    printf("The value of line5 - c is %d\n", c);
    c = a++;
    printf("The value of line6 - c is %d\n", c);
    c = a--;
    printf("The value of line7 - c is %d\n", c);
}