"""
如果实例字典与数据描述符有同名的属性，优先使用数据描述符；
如果实例字典与非数据描述符有同名的属性，优先使用非数据描述符；
"""


class DataDes:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        self._score = value

    def __get__(self, instance, owner):
        print('调用数据描述符里的__get__方法')
        return self._score


class NoDataDes:
    def __init__(self, default=0):
        self._score = default

    def __get__(self, instance, owner):
        print('调用非数据描述符里的__get__方法')
        return self._score


class Student:
    math = DataDes()
    english = NoDataDes()

    def __init__(self, math, english):
        self.math = math
        self.english = english

    def __getattribute__(self, item):
        print('调用__getattribute__')
        return super(Student, self).__getattribute__(item)

    def __repr__(self):
        return f'math={self.math},english={self.english}'


std = Student(48, 39)
print(std.math)
print(std.english)
print(Student.__dict__)
# 调用__getattribute__
# 调用数据描述符里的__get__方法
# 48

# 调用__getattribute__
# 39   # 隐式的Student的get方法
