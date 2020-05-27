"""
装饰器
不修改原函数的情况下，对其增加功能>>装饰器

"""
# def a(c):
#     def b():
#         print("中华人民共和国",end=":")
#         c() #调用执行
#     return b

#增加功能  添加:中华人民共和国
# @a      #>>>demo1=a(demo1) a()返回值为函数b()指向b的内存地址
# def demo1():
#     print("湖南省")
#
# @a      #>>>demo2=a(demo2)
# def demo2():
#     print("河南省")
#
# @a      #>>>demo3=a(demo3)
# def demo3():
#     print("台湾省")

# demo1()
# demo2()
# demo3()

#包的导入
# import 10_import.demo1  #导入子模块，必须全名访问
# 10_import.demo1.demo1()

# from 10_import import demo1 #from 包  import 模块名，就利用模块名.函数名访问
# demo1.demo1()

# from 10_import.demo1 import demo1 #from 包.模块 import 函数名 ，可以直接函数名掉用
# demo1()

#import xx，后面只能写道模块，不能写到函数
#from xx import xxx ,import后面能写到函数，包，模块等

# from 10_import import *
# demo1.demo1()

# from 1_type import type  #可以直接导入模块，不是函数也可以，在另一个。py中执行
# type



















