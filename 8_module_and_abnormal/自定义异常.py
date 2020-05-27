#之前的都是python的原生异常类
#自定义异常类
#子类》》》父类Exception
#自定义异常类继承了父类Exception，也可以作为
class NameIsError(Exception):
    pass
class AgeIsError(Exception):
    pass

name="傻逼沙雕"
age=23
# def check_name_and_age(name,age):
#     if name.find("傻")>=0:
#         raise NameIsError("这个人很傻")
#     if age>=20:
#         raise AgeIsError("这个人是个老男人")

# check_name_and_age(name,age)
#如果不写到try里，由于raise抛出异常，会出现红色异常文字，所以需要try检测异常，并输出一般的提示性文字

def check_name_and_age(name,age):
    if name.find("傻")>=0:
        raise NameIsError("这个人很傻")
    if age>20:
        raise AgeIsError("这个人是老男人")

try:
    check_name_and_age(name,age)
except NameIsError as e:
    print(e)
except AgeIsError as e:
    print(e)
#由于try发现异常就停止后续操作，如何把写有两个异常的函数，正常运行。。。
#问题所在。。。。。。这种情况只能print，或者拆分函数吗？？？？？？？？？？PROBLEM









