"""
字典参数
def 函数名（**形参）
    函数体
调用格式
   函数名（未被定义的关键字参数=实参1，。。。。）
"""
# def demo(a,b,*args,c,d=2):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)
#
# demo(1,2,3,4,5,c=6,d=7)
#参数的顺序：位置参数，可变参数，关键字参数。如果位置参数在可变参数之后，必须必须使用关键字参数，传递实参

def demo(a,** kwargs):#字典参数必须定义在关键字参数之后
    print(a)
    print(kwargs)
demo(b=2,a=1,c=3)#调用时关键字参数如果声明了，传到关键字参数，如果没声明，全部传给字典参数，调用时，顺序可以打乱


#位置参数，可变参数，关键字参数，字典参数   函数定义时，函数传值顺序。









































































































