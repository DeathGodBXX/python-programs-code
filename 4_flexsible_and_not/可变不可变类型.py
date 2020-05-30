"""
演示可变类型和不可变类型
列表可变，内存不变，元组不可变，内存改变
列表和元组，字典都是可迭代对象
"""
# 列表和元组
# list1=[1,2,3]
# for i in list1:
#     print(i)
# print("list1定义的时候内存地址为:",id(list1))
# list1.append(4)

# print('修改后，list1的内存地址是:', id(list1))
# 列表是可变的，内存地址修改前后不变
# tuple1=(1,2,3)
# tuple1.__new__()
# print("tuple1的内存地址:",id(tuple1))
# tuple1=(1,2,3,4)
# print("tuple1的内存地址:",id(tuple1))
# 元组是不可变的，追加模式都没有，手动添加，所以最终的ip地址会改变

"""
演示列表和元组的转换
"""
# 列表转换为元组  迭代
# list1 = [1, 2, 3]
# list1.append(4)
# print(list1,end='\n\n')
# print(tuple(list1))
# 元组转换为列表   #tuple不可变是，指向不变
# tuple1 = (1, 2, 3)
# list2 = list(tuple1)
# print(list2)
# list3 = list2.append(4)    #由元组转换成列表，再赋值给另外的列表，此时列表得不到转换后的值
# print(list2)
# print(list3)


tuple1 = (1, 2, 3)
list2 = list(tuple1)
print(list2)
list3 = list2.append(4)
# append无返回值，所以调用，没有值传递给list3,但是list3=list2,修改过的list2,list3的值就不是None

list3 = list2
print(list2)
print(list3)

# list_a = [1,2,3]
# list_b =list_a
# print(list_a)
# print(list_b)
# tuple2 = tuple1+(4,)
# print(tuple2)

"""
字典的演示
"""
# 变量的方式
# name = "bobo"
# gender = "男"
# age = "28"


# 键值对，键是唯一的，值不限制
# 变量名={键1：值1，键2：值2，。。。}
# 取出值，变量名[键名];修改变量值，变量名[键名]=值   字符串
# dict1={"name":"bobo","性别":"男","年龄":"28"}
# print(dict1)

"""
演示字典的基本操作
"""
# dict1={"a":"a1","b":"b1"}
# print(dict1)
# print(dict1[1]) #键就是索引
# print(dict1["a"])
# c = 1
# d = 2
# c1 = 1
# d1 = 3
# dict2 = {c: c1, d: d1}
# print(dict2)
# dict1["a"]="a2"
# list1=[1,2,3]
# list1[3]=4  #索引超出时，报错
# dict1["d"]="d1"
# print(dict1)
# del dict1['b']
# print(dict1)
# dict1.clear()
# print(dict1)
# del dict1
# print(dict1)
# 使用for循环遍历字典数据   赋值给i以键名，再根据键名查找数值
# for i in dict1:
#     print(i, ':', end=' ')
#     print(dict1[i])

# data = [1]*5  #列表元素复制5个
# print(data)

# dict2 = dict(dict1)
# print(dict2)

# dict3 = {'Name': '游朋卓', 'Age': '弟弟', 'Name': '系建行'}

# print(dict3)

# dict4 = {['Name']:'游朋卓'}
# print(dict4)

# dict4 = {'Name': ['游朋卓','系建行'] }
# print(dict4)  #键唯一，值不必
