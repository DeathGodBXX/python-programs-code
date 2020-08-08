class Score:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("integer must be int")
        if not 0 <= value <= 100:
            raise ValueError("value must in [0,100]")
        self._score = value

    def __get__(self, instance, owner):
        return self._score

    def __delete__(self, instance):
        del self._score


class Student:
    """三个数据描述器,类变量"""
    math = Score()
    chinese = Score()
    english = Score()

    def __init__(self, math, chinese, english, name='xiaoming'):
        """
            实列变量修改了类变量math,chinese,english,
           看着像是描述器自动装饰了同名的实例变量，使其具备描述器的功能，
           但是同时具备类属性的性质。
           看着像是实例化的类变量
           或许这句话更准确：如果实例字典与数据描述符有同名的属性，优先使用数据描述符；
                          如果实例字典与非数据描述符有同名的属性，优先使用非数据描述符；
        """
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return f"math={self.math},chinese={self.chinese},english={self.english}"


std1 = Student(20, 50, 90)
std2 = Student(39, 40, 40)
print(std1)
print(std2)
print(Student.__dict__)
print(std2.__getattribute__)
std1.math = 79
std1.english = 91
std1.chinese = 80
print(std1)
