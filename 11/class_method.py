"""
类方法
"""
class Chinese:
    def __init__(self,name,place):
        self.name = name
        self.place = place
    #类方法, 不可修改的
    @classmethod
    def say_fighting(cls):
        print("我是中国人，我为祖国加油")
    #对象可修改
    def myself(self):
        print("my name is %s, my place is %s "%(self.name, self.place))

man1 = Chinese("波霸", "湖北")
#实例方法的调用
man1.myself()
#类方法的调用
Chinese.say_fighting()






















