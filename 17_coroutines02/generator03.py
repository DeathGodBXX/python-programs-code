def fei_bo(n):
    """生成斐波那契数列"""
    a, b = 0, 1
    start_num = 0
    while start_num < n:
        name = yield a
        print(name)
        a, b = b, a + b
        start_num += 1
    # while循环结束，抛出StopIteration ，再return
    return "波霸在秀波"


data = fei_bo(5)
while True:
    try:
        f1 = next(data)
        print(f1, end=',')
    except Exception as e:  # 接收异常,同时将传出return值
        print()
        print(e)
        break

# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
