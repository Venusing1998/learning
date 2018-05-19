"""汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如:

def move(n, a, b, c):
    if n == 1:
    print(a, '-->', c)
"""

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    if n == 2:
        print(a, '-->', b)
    if n ==3 :
        print(c,'-->', b)
    