def fei_bo(n):
    """生成斐波那契数列"""
    a,b =0, 1
    start_num = 0
    while start_num < n:
        yield a
        a,b =b,a+b
        start_num+=1

F1 = fei_bo(5)
try:
    while True:
        print(next(F1))
except StopIteration:
    print('bobo很骚气')



# for i in F1:
#     print(i)




















