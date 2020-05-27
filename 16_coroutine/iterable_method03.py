from collections.abc import Iterator
class A():
    def __iter__(self):
        print('A类的__iter__()方法被调用')
        return B()
class B():
    def __iter__(self):
        print('B类的__iter__()方法被调用')
        return self
    def __next__(self):
        pass
a = A()
print('对A类对象调用iter()方法前，a是迭代器吗：', isinstance(a, Iterator))
# a1 = iter(a)
a1 = a.__iter__()
print('对A类对象调用iter()方法后，a1是迭代器吗：', isinstance(a1, Iterator)) #调用iter()方法，返回迭代器对象，迭代器

b = B()
print('对B类对象调用iter()方法前，b是迭代器吗：', isinstance(b, Iterator))  #B()自身就是迭代器 ，
# 上面的a1.__iter__()等价于这里的B（）
b1 = iter(b)
print('对B类对象调用iter()方法后，b1是迭代器吗：', isinstance(b1, Iterator))