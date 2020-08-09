class TestProperty(object):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        # 定义三个实例变量接收传进来的函数名称
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):  # obj或许为math,由python解释器自动提供
        print('in __get__')
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError
        print(obj)
        return self.fget(obj)

    def __set__(self, obj, value):
        print('in __set__')
        if self.fset is None:
            raise AttributeError
        print(obj)
        self.fset(obj, value)

    def __delete__(self, obj):
        print('in __del__')
        if self.fdel is None:
            raise AttributeError
        self.fdel(obj)

    """装饰器入口，返回的是Testproperty的实例，自动调用set,del,get"""

    def getter(self, fget):
        print('in getter')
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        print('in setter')
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        print('in deleter')
        return type(self)(self.fget, self.fset, fdel, self.__doc__)


class Student:
    def __init__(self):
        # self.math = default
        ...

    @TestProperty
    def math(self):
        return self._math

    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError

    @math.deleter
    def math(self):
        del self._math


std1 = Student()
std1.math = 30
print(std1.math)

# in setter
# in deleter
# in __set__
# <__main__.Student object at 0x036717C0>
# in __get__
# <__main__.Student object at 0x036717C0>
# 30
# why not in getter message,even if std1.math,maybe print message be ignored before going into the function


