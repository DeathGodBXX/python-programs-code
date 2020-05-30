"""
可变参数（接收多余的位置参数，如果想让后面的参数得到赋值，必须使用关键字参数,也就是来说调用的时候，必须顺序传值）
def 函数名（*形参，...)  *形参，这是可变参数在函数中的定义
    函数体
调用格式
   函数名（实参1，....)
"""
# def sum_3(a,b,c):
#     sum0=a+b+c
#     print(sum0)
# sum_3(1,2,3)

# def sum_3(*args):#默认名称为args
#     for i in args:
#         print(i)
#     print(args)#元组，组包
#
# sum_3(1,2,3,4,5)

# def demo(*args,*args2):
#     for i in args:
#         print(i)
#     for i in args2:
#         print(i)
# demo(1,2,3,4,5) #无效语法


# 可变参数存在的情况下，普通的位置参数还能存在吗？ok
# 顺序，可变参数前面是位置形参,可变参数之后必须要由关键字参数传值
# def demo(a,*args,c):
#     print(a)
#     print(args)
#     print(c)
# demo(1,2,3,4,c=5)#关键字参数
