import multiprocessing

# import time

# 子进程与主进程之间的共享全局变量
# 不可变类型 必须添加global （内存地址改变）
# 可变类型，不需要添加global （内存地址不变）
# from multiprocessing import Process

list1 = [1, 2, 3]
num1 = 9


def demo1():
    """demo1,demo2,main中list1内存地址各不相同，但是在每个函数内部list1即使修改，内存地址也不会改变，即使传参也不能共享全局变量。总之，global在多进程之间作用很小，要么是可变类型，要么不可变类型，需要消息传递"""
    # print(id(list1))
    # global num1
    # print(id(list1))
    list1.append(4)
    print('在子进程A的demo1,list1的值是:', list1)
    # print(num1)
    # print(id(num1))
    # num1 = 10
    # print(num1)
    # print(id(num1))


def demo2():
    # global num1
    print('在子进程B的demo1,list1的值是：', list1)
    # num1 = 13
    # print(num1)
    # print(id(num1))


def main():
    p1 = multiprocessing.Process(target=demo1)
    p2 = multiprocessing.Process(target=demo2)
    p1.start()
    p1.join(1)
    p2.start()
    p2.join()
    list1.append(5)
    print('在主进程,list1的值是:', list1)
    # print(num1)
    # print(id(num1))


if __name__ == '__main__':
    main()

# 不共享全局变量
