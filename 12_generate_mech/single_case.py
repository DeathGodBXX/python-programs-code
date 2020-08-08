# 单例模式  new方法生成单一对象，利用if条件控制  内存地址一样,重复利用同一内存呢地址
class Man:
    # 类变量是共享的，if控制只有一个值，达到只创建一个实例的效果----单例模式
    __instance = None

    def __init__(self, args):
        self.args = args

    def __new__(cls, *args, **kwargs):
        # __instance = None
        if cls.__instance is None:
            cls.__instance = object.__new__(Man)  # 静态方法
            # cls.__instance = object.__new__(cls)
            # cls.__instance = super().__new__(cls)
        return cls.__instance

    # new方法用来生成实例对象，修改之后，实例对象的地址就是cls.__instance的地址

    def play(self):
        print('I can sing')

    def return_args(self):
        return self.args


man1 = Man('匆匆那年')
print(man1.return_args())
print(id(man1))
man2 = Man('一切静好')
print(man2.return_args())
print(id(man1))
if id(man1) == id(man2):
    print('单例模式开启')
else:
    print('非单例模式')

# print(id(Man.instance))  # 私有变量，外部不可访问
print(id(Man.__new__(Man)))  # 如果instance不设置成私有变量，这四个地址一样，说明对象的地址真正的与类变量挂钩了
print(id(Man))


# class Man:
#     pass
#
#
# man1 = Man()
# print(id(man1))
# man2 = Man()
# print(id(man2))
