"""
成员方法调用成员方法
类
"""

class Man():
    def sing(self):
        print("唱歌")
    def dance(self):
        print("跳舞")
    def run1(self):
        self.sing()
        self.dance()

man=Man()
man.run1()

























