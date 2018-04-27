# 1.识别下面字符串:’ben’,’hit’或者’ hut’
import re
pattern = re.compile('^\w*$')
result = pattern.findall('ben')
print(result)

# 2.匹配用一个空格分隔的任意一对单词,比如你的姓 名

pattern2 = re.compile('\w* \w*')
result2 = pattern2.findall('Chris Zhu')
print(result2)

# 3.匹配用一个逗号和一个空格分开的一个单词和一个字母
pattern3 = re.compile('\w*, \w*')
result3 = pattern3.findall('hello, world!')
print(result3)

# 4.匹配简单的以’www’开头,以’com’结尾的web域名,比如:www.baidu.com
pattern4 = re.compile('^www.*com$')
result4 = pattern4.findall('www.baidu.com')
print(result4)