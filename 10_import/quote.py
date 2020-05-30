"""
引用
引用是指变量指向数据存储空间的现象
相同的数据使用同一个空间存储，节约内存占用
使用id(数据)操作可以获取数据存储的内存空间的引用地址

"""
# 数值>>不可变类型 小于一定数值，数值所对的内存地址不会更换；超过一定数值，数值所对的内存地址一直更换（数值不会改变）
# 不可变类型  数值，字符串，元组等
# a=1000
# b=1000
# print("a的内存地址为:%s",id(a))
# print("b的内存地址为:%s",id(b))

# 列表>>可变类型  使用就会开辟内存，即使数据更改，内存地址也不会更改；即使数据相同的列表，所开辟的内存也是不一样的
# （假设只想对一个列表更改数据，如果两个的内存地址一样，那么两个数据都被改变了，这样就不稳定了）
# 可变类型 列表，对象，字典等等
# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))


# list1 = [1, 2, 3]
# print(list1)
# print(id(list1))
# print(id(list1[0]))
# 对照c语言，print(id(list1))和print（id(list1[0]))必然是一样的，但是python不一样，这是因为，数值用的是引用，所以print(id(list1[0]))其实等于print(id(1))
# print(id(1))
# print(id(list1[1]))
# print(id(2))
# print(id(list1[2]))
# print(id(3))
# list1.append(4)
# print(id(list1))
# print(id(list1[0]))
# print(id(1))
# print(id(list1[1]))
# print(id(2))
# print(id(list1[2]))
# print(id(3))
# print(id(list1[3]))
# print(id(4))

# 不可变类型，修改数值，内存更改；可变类型，修改数值，内存不变

"""
def test1():
    print("---在test1中----")

test1()

#调用引用，函数两个名字
test2=test1

print(id(test1))
print(id(test2))

test2()
test1()

"""

# a = 1
# b = a
# b = 2
# print(id(a))
# print(id(b))


# def test1():
#     print("---在test1中----")
#
#
# test1()
# test2 = test1
# # 给test1取别名，实质上是上test2也指向test1的函数地址
# print(id(test1))
# print(id(test2))
# test2()




