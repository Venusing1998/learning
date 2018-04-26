#include <stdio.h>
#include <float.h>

int main()
{
    printf("the largest of byte is: %lu\n", sizeof(float));
    printf("the min value of float is: %E\n", FLT_MIN);
    printf("the max value of float is: %E\n", FLT_MAX);
    printf("the accuracy is: %d\n", FLT_DIG);

    return 0;
}