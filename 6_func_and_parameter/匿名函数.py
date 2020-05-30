"""
匿名函数
函数名=lambda 形参：返回值    简化定义  适用于较为简单的函数

"""
# def add2(a,b):
#     return a+b
# i=add2(1,2)
# print(i)


# adds=lambda a,b:a+b
# c=adds(1,3)
# print(c)

# c=(lambda a,b:a+b)(2,3)
# print(c)

# print((lambda a,b:a+b)(1,3))


# 注意事项
# 如果不传实参,会报错，如果没有形参，不传参数，不会报错
# c = (lambda: 10)()
# print(c)
# 多返回值,不可以
# a = (lambda: 4, 5)()
# print(type(a))
# print(a)
# a = (lambda: (4, 5))()
# print(a)

# print((lambda a,b:a*b)(2,3))
