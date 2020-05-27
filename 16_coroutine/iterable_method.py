"""迭代器"""
"""只要具备iter()方法，就是可迭代对象；只要含有iter（）和next()方法，就是迭代器。可以使用next方法取值"""

from collections import Iterable
from collections import Iterator
class Diy:
    def __init__(self):
        self.names = []

    def add_name(self, name):
        self.names.append(name)

    #变成可迭代对象，魔术方法
    def __iter__(self):
        print('Diy().__iter__方法被调用')
        return DiyIter(self.names)
        #如果只传self，无法使用len(self.names),因为传递的是Diy对象，位置参数。引用。打印的是diy对象地址
        # 如果传递self.names，这是一个列表，可以使用len()


    #1.range()是否是迭代对象 >>__iter__ ,iter()
    #2.iter(对象) >>return 返回值
    #3.返回迭代器  >>__iter__,__next__依赖于next方法取值

class DiyIter: #迭代器
    def __init__(self,names):
        self.start_num = 0
        self.names = names
        # print(names)
        # print(id(names))
        # print(self.names)
        # print(id(self.names))
    def __iter__(self):
        print('DiyIter().__iter__方法被调用')
        return self
    def __next__(self): #自带循环功能
        # pass
        if self.start_num < len(self.names):
            print('DiyIter().__next__方法被调用')
            a = self.names[self.start_num]
            self.start_num+=1
            return a
        else:
            raise StopIteration
            #python停止循环的固定方式

man1 = Diy()
man1.add_name('赵一')
man1.add_name('钱二')
man1.add_name('孙三')
# print(isinstance(man1, Iterable),end='\n') #迭代对象
man2 = iter(man1)       #迭代器对象
print(isinstance(man2, Iterator))
try:
    while True:
        print(next(man2))
except StopIteration:
    print('\n','bobo的波很大')



# for i in man1: #for循环的实质：自动执行python内置的iter()方法，next()，自动取值下一个，直到stopiteration。
#     print(i)               # 迭代对象的iter()方法，迭代器的next（）方法

# for i in DiyIter(['张三', '李四', '王五', '赵六']):  # 迭代对象的iter()方法，迭代器的next（）方法
#     print(i)


























