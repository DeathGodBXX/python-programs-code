"""
多线程共享全局变量

"""
"""1111111"""

# import threading
# import time
#
# num1 = 1
#
#
# # 修改全局变量，global
# # 可变类型和不可变类型   global添加在不可变类型前 可变类型前不加global，也是全局变量
#
# def demo1():
#     global num1
#     num1 += 1
#     print("在demo1中，num1的值是:", num1)
#
#
# def demo2():
#     global num1
#     num1 += 1
#     print("在demo2中，num1的值是:", num1)
#
#
# def main():
#     t1 = threading.Thread(target=demo1)
#     t2 = threading.Thread(target=demo2)
#     t1.start()
#     time.sleep(0.8)
#     t2.start()
#     time.sleep(0.9)
#     print("在main函数中，num1的值为:", num1)
#
#
# if __name__ == "__main__":
#     main()

"""222222222"""
# import time
# import threading
#
# list1 = [1, 2, 3]
#
#
# def demo1(a):
#     list1.append(a)
#     print("在demo1中，list1是：", list1)
#
#
# def demo2():
#     print("在demo2中，list1是：", list1)
#
#
# def main():
#     t1 = threading.Thread(target=demo1, args=(4,))
#     # 实例传参，元组的形式
#     t2 = threading.Thread(target=demo2)
#     t1.start()
#     time.sleep(0.8)
#     t2.start()
#     time.sleep(1)
#     print("在main函数中，list1是：", list1)
#
#
# if __name__ == "__main__":
#     main()

"""
共享变量num1

"""
import threading
import time

num1 = 0


def demo1(a):
    global num1
    for i in range(a):
        num1 += 1
    print("在demo1中，num1的数值为:", num1)


def demo2(a):
    global num1
    for i in range(a):
        num1 += 1
    print("在demo2中，num1的数值为:", num1)


def main():
    a = 1000000
    t1 = threading.Thread(target=demo1, args=(a,))  # 实例方法，传参
    t2 = threading.Thread(target=demo2, args=(a,))
    t1.start()
    t2.start()
    time.sleep(2)
    print("在main函数中，num1的数值为:", num1)


if __name__ == "__main__":
    main()

# question:为何数值a较小，不会出现错误的结果？
# 快速切换，每次切换的位置不一样，有可能还没写入num1，就进行另一个函数的下一次循环操作，再次切换回来的时候，接着写入，但是由于全局变量，写入等于没写。
# 数值较小时，很有可能demo1运行完了，之后才有demo1运行，基本等价于串行算法。自动实现为串行，单-线程的操作。
