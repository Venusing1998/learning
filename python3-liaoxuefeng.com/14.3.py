"""利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

from functools import reduce

def str2float(s):
"""
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(c):
    return DIGITS[c]


def str2float(s):
    s = s.split('.')
    s1 = s[0]
    s2 = s[1:] or ['0']
    s2 = s2[0] or '0'
    s2 = s2[::-1]
    return (reduce(lambda x, y: x * 10 + y, map(char2num, s1))) + (reduce(lambda x, y: x / 10 + y, map(char2num, s2))) / 10
