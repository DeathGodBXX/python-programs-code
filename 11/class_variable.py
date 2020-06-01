"""
演示类变量
"""


class Man:  # 传参
    gender = "男"  # 类变量 类变量只能用类.类变量名修改类变量

    def __init__(self, name, place):
        self.name = name
        # self.gender = gender
        self.place = place

    def myself(self):
        print("我是%s,性别%s,住址%s" % (self.name, self.gender, self.place))


man1 = Man("波霸", "湖北")  # 类和对象不是同一块存储空间
# print(Man.name)  # 不可以直接使用类变量，但是可以使用实例变量

# 对象名.类变量名 对象的私有变量属性
man1.gender = "nv"
print(man1.gender)
print(Man.gender)

# 类名.类变量名 类
Man.gender = "女"
print(man1.gender)
print(Man.gender)

# man1.name = "波霸"
# man1.gender = "男"
# man1.place = "湖北"
# man1.myself()

# man1 = Man("周周", "男", "湖南")
# man1.myself()
