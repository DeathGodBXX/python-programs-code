# a=1
# b=a
# b=2
# print(id(a))
# print(id(b))

#引用 闭包 装饰器
#装饰器，生成器，迭代器

"""
演示闭包
两个函数嵌套，内部函数用到外部函数的变量的现象称为闭包

"""

"""
def test1():
    print("---在test1中----")

test1()

#调用引用，函数两个名字
test2=test1

print(id(test1))
print(id(test2))

test2()
test1()

"""

# def a(c,d):
#     def b():
#         return c+d;
#     return b
#
# demo1=a(1,2)
# demo2=a(3,4)
# print(demo1)
# print(demo2)

# def a(c,d):
#     def b():
#         return c+d;
#     return b()
#
# demo1=a(1,2)
# demo2=a(3,4)
# print(demo1)
# print(demo2)



















































