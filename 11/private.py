"""
演示私有属性和封装
"""
class Man():
    def __init__(self):
        self.name = None
#         变量私有化，变量名前加两个下划线，打印出来说明没这个变量
        # 成员方法 中间商，间接抛出私有属性,通过def demo(self)抛出私有属性
        self.__id_card = None

    def get_id_card(self):
        return self.__id_card

    #修改或设置私有变量方法
    def set_id_card(self,id_card):
        self.__id_card = id_card

man1=Man()
# print(man1.name)
# print(man1.id_card)
# print(man1.demo())
man1.set_id_card(131229421937491)
print(man1.get_id_card())

#方法可以私有，一般用不上



















