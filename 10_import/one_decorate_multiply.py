"""
装饰器
不修改原函数的情况下，对其增加功能>>装饰器

"""
"""******一个装饰器装饰多个函数******"""


def a(c):  # 此处c是函数名
    def b():
        print("中华人民共和国", end=":")
        c()  # 调用执行

    return b  # 装饰后的函数重命名


# 增加功能  添加:中华人民共和国
@a  # >>>demo1=a(demo1) a()返回值为函数b()指向b的内存地址
def demo1():
    print("湖南省")


@a  # >>>demo2=a(demo2)
def demo2():
    print("河南省")


@a  # >>>demo3=a(demo3)
def demo3():
    print("台湾省")


demo1()
demo2()
demo3()

# 一个函数被多个装饰器装饰？？？？？？？操作
