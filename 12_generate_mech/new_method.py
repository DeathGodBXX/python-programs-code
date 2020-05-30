# class Man():
#     def  __new__(cls, *args, **kwargs):#new方法不重写可以创建多个对象，系统自带的new方法，重写加调用可以创建对象，可以很多个
#         print("调用new方法")
#         instance = object.__new__(Man) #只重写new方法，不调用object的new方法，则不创建对象
#         return instance      #重写并返回__new__
#     def __init__(self, name, age):
#         print("调用init方法")
#         self.name = name
#         self.age = age
# #类创建对象依赖于objec的new方法 ，init方法依赖于new方法
#
#
# man1 = Man("波霸","18")
# print(id(man1))
# man2 = Man("巴伯","20")
# print(id(man2))
#
# help(object.__new__)

#单例模式  new方法生成单一对象，利用if条件控制
class Man:# 利用类变量控制单一对象的生成， 为何能做到？类只有一个，类变量每个都是唯一的，故而将未来定义的对象与类变量挂钩，也就是引用
    __instance = None
    def __init__(self,*args,**kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        # __instance = None
        if cls.__instance is None:
            cls.__instance = object.__new__(Man)
        return cls.__instance

man1 = Man()
man2 = Man()
if id(man1) == id(man2):
    print('单例模式开启')
else:
    print('非单例模式')


# print(id(Man.instance))
print(id(Man.__new__(Man)))  #如果instance不设置成私有变量，这四个地址一样，说明对象的地址真正的与类变量挂钩了

print(id(Man))


# class Man:
#     pass
# man1 = Man()
# print(id(man1))
#
# man2 = Man()
# print(id(man2))












