#  创建两个协程函数对象,分别完成1,3,5…99,   2,4,6…,100
#  然后让两个协程函数对象分别交替执行.在每一个协程函数对象的内部先打印输出
#  每一个数字,然后执行完一轮之后打印提示信息,已经交替执行完毕一轮
#  等所有的协程函数对象执行完毕之后,分析一下数据信息

from types import coroutine


async def run1():
    for i in range(1, 100, 2):
        print(i)
        await work()


async def run2():
    for i in range(2, 102, 2):
        print(i)
        await work()


@coroutine
def work():
    yield


def manager(a_list):
    b_list = list(a_list)
    while b_list:
        for item in b_list:
            try:
                item.send(None)
            except StopIteration as e:
                b_list.remove(item)


if __name__ == '__main__':
    r1 = run1()
    r2 = run2()
    c_list = [r1, r2]
    manager(c_list)
