"""
继承
调用格式
"""


class Father():
    def __init__(self):
        self.name = None
        self.place = None

    def myself(self):
        print("%s, %s" % (self.name, self.place))


# 子类可以继承父类的实例变量,父类的私有属性不可被继承
class Son(Father):
    def sing(self):
        print("擅长唱歌")


son = Son()
son.name = "小明"
son.place = "湖北"
son.myself()
son.sing()


# check classmethod and staticmethod 的使用方法




