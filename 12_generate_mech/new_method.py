class Man():
    def __new__(cls, *args, **kwargs):
        # new方法不重写可以创建多个对象，系统自带的new方法，重写加调用可以创建对象，可以很多个
        print("调用new方法")
        # instance = super().__new__(Man)  # 等价
        instance = object.__new__(Man)  # 只重写new方法，不调用object的new方法，则不创建对象
        return instance  # 重写Man里的new方法并返回__new__

    def __init__(self, name, age):
        print("调用init方法")
        self.name = name
        self.age = age


# 类创建对象依赖于objec的new方法 ，init方法依赖于new方法


man1 = Man("波霸", "18")
print(id(man1))
man2 = Man("巴伯", "20")
print(id(man2))

# help(object.__new__)
# new方法生成实例，init方法初始化实例
