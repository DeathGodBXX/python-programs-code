class Score:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("integer must be int")
        if not 0 <= value <= 100:
            raise ValueError("value must in [0,100]")
        # must use this method,since self._score=value will be shared by every example.
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Student:
    """三个数据描述器,类变量"""
    math = Score('math')
    chinese = Score('chinese')
    english = Score('english')

    def __init__(self, name='xiaoming'):
        """
            实列变量修改了类变量math,chinese,english,
           看着像是描述器自动装饰了同名的实例变量，使其具备描述器的功能，
           但是同时具备类属性的性质。
           看着像是实例化的类变量
           或许这句话更准确：如果实例字典与数据描述符有同名的属性，优先使用数据描述符；
                          如果实例字典与非数据描述符有同名的属性，优先使用非数据描述符；
        """
        self.name = name

    def __repr__(self):
        return f"math={self.math},chinese={self.chinese},english={self.english},name={self.name}"


std1 = Student('大黄')
std2 = Student('小白')
std1.math = 79
std1.english = 91
std1.chinese = 93
std2.math = 99
std2.english = 90
std2.chinese = 100
print(std1)
print(std2)


# conclude:whether you define init func,
# the same result only if using instance.__dict[self.name] to visit value
