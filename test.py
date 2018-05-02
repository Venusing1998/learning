def sum1():
    result = []
    for x in range(10):
        yield(x ** 2)
        result.append(x ** 2)


for y in sum1():
    print(y)
