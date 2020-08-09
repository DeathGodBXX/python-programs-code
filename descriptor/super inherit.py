class father():
    def play(self):
        print("钓鱼")


class son(father):
    def play(self):
        # 父类调用的三种格式
        father.play(self)
        super(son, self).play()
        super().play()
        print("打球")


son1 = son()
son1.play()
print(son.__mro__)
print(son.mro())
# print(son.__mro__)
# print(son.__mro__)

# 通过son.mro()查看mro信息，继承[son,father,object],
# 其中super(son,self).play(),表示从son之后father,object查找，
# 利用self=son1的实例，获取运行结果
#
