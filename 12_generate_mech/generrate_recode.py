"""
继承重写

"""
class father():
    def play(self):
        print("钓鱼")

class son(father):
    def play(self):
        #父类调用的三种格式
        father.play(self)
        super(son,self).play()
        super().play()
        print("打球")

son1=son()
son1.play()
print(son.__mro__)
# print(son.__mro__)
# print(son.__mro__)
















































