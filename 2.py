# 1. PKCS#5(选择一种hash算法)加密算法加密你的中文名字,写出代码
import hashlib
md_5 = hashlib.md5()
md_5.update('chris zhu'.encode('utf-8'))
print(md_5.hexdigest())

# 2. 创建文件test.py,写入一些数据,并计算该文件的md5值
import os
if not os.path.exists('./test.py'):
    with open('test.py','w') as f:
        f.write('ok')
md_5_1 = hashlib.md5()
md_5_1.update('test.py'.encode('utf-8'))
print(md_5_1.hexdigest())