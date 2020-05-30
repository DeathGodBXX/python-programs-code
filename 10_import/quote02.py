# 引用 闭包 装饰器
# 装饰器，生成器，迭代器

"""
演示闭包
两个函数嵌套，内部函数用到外部函数的变量的现象称为闭包

"""


# def a(c, d):
#     def b():
#         return c + d
#
#     return b
#
#
# demo1 = a(1, 2)
# demo2 = a(3, 4)
# print(demo1)
# print(demo2)
# # 由于参数a和b不同，可以视demo1,demo2为不同的函数
# print(demo1())
# print(demo2())
# print(id(3))
# print(id(7))

# def a(c, d):
#     def b():
#         return c + d
#
#     return b()
#
#
# demo1 = a(1, 2)
# demo2 = a(3, 4)
# print(demo1)
# print(demo2)
