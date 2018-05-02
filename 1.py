# 遵循上下文管理协议,自己编写一个类,去创建一个上下文管理器,然后自己使用看看  
#    方式1:普通方式
#    方式2:使用contextmanager
class Myclass():
    def __init__(self):
        print('init the data.')
    def __enter__(self):
        print('enter the context.')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit the context.')
    def run(self):
        print('instance.')

with Myclass() as f:
    f.run()
    print('print me first.')
    print('print mre second.')

from contextlib import contextmanager
class Myclass():
    def __init__(self):
        print('init the data')
    def run(self):
        print('instance')

@contextmanager
def work():
    print('first')
    my_c = Myclass()
    yield my_c
    print('second')

with work() as f:
    f.run()