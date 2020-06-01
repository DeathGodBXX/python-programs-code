"""
  当类中含有__call__方法，可以使用类名（实参）调用类里的call方法。相当于定义了一个类名（）的函数
   函数和对象的区别不大。。
"""


class Fib(object):
    def __init__(self):
        pass

    def __call__(self, num):
        # 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
        a, b = 0, 1
        self.l = []

        for i in range(num):
            self.l.append(a)
            a, b = b, a + b
        # return self.l

    def __str__(self):  # 碰到print对象操作，自动执行。
        return str(self.l)

    __rept__ = __str__


f = Fib()
f(10)
print(f)  # 碰到print对象操作，自动执行。
