from collections import Iterable


class Diy:
    def __init__(self):
        self.names = []
        self.start_num = 0

    def add_name(self, name):
        self.names.append(name)

    # 变成可迭代对象，魔术方法
    def __iter__(self):
        return self

    def __next__(self):  # 自带循环功能
        if self.start_num < len(self.names):
            a = self.names[self.start_num]
            self.start_num += 1
            return a
        else:
            raise StopIteration
            # python停止循环的固定方式


man1 = Diy()
man1.add_name('赵一')
man1.add_name('钱二')
man1.add_name('孙三')
print(isinstance(man1, Iterable))  # 迭代对象
print(iter(man1))  # 迭代器对象
print(next(man1))
print(next(man1))
print(next(man1))

# 1.可迭代对象，2.迭代器，3.迭代取值
# 是否含有__iter__，
# 调用iter方法，返回迭代器对象，是否含有__iter__,__next__,
# 调用next方法取值
for i in man1:
    print(i)

# question：主函数里有没有调用类的私有函数的接口？？？？？？check it?????????
