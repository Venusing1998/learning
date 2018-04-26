"""以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：

def product(x, y):
    return x * y
"""


def product(x, *args):
    num = 1
    for i in args:
        num = num * i
    return num * x


print(product(2, 5, 7))
