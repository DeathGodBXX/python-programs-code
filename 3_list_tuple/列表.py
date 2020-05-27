# 99乘法表
# j=1
# while j<=9:
#     i=1
#     while i<=j:
#         print("%s*%s=%s"%(i,j,i*j),end=("\t"))//分号和数据间不需要加逗号,但是end前要加逗号
#         i+=1
#     print()
#     j+=1


"""
列表(数组)
变量名=[数据1,数据2,数据3....]
赋值
变量名=值



"""
#列表可以赋值不同类型,可以认为都是string，但是利用列表数值元素相加能够正常运算,string型加，即时连接
# _list_=[1,2,3,"hello","武汉加油"]
# _list_[4]="武汉加油，湖北加油"
# print(_list_[1]+_list_[2],_list_[3]+_list_[4])

# list1=[1,2,6,4,5,1,1]
# list1.append(3)
# print(len(list1))
# print(list1.__len__())
# print(list1.__len__())两个__

# list1.sort(reverse=True) #不带参数是从大到小，修改inverse是从小到大
# print(list1)
# list1.insert(2,3)  #指定index位置插入数据，第一个数值是index,后面的是数据
# print(list1)
# list2=[7,10,"_course"]
# list1.extend(list2)
# print(list1)
# list1.pop(2) #删除指定index下的数据
# print(list1)
# print(list1.count(1))
# print(list1.__len__())

"""
插入
列表.insert(索引,数据)在指定位置插入数据
列表.append()可以在列表末尾追加元素
列表,extend()列表的连接

删除
del 列表[索引] 删除列表指定位置数据
列表.pop() 默认删除末尾数据
列表.pop(索引)删除索引值
列表.remove(数据)删除掉第一个出现的数据
列表.clear() 清空列表

修改
列表[索引]=数据  修改指定位置数据

统计
列表.count(数据) 统计数据出现次数
列表.len()统计列表长度

排序
列表.sort() 升序排序
列表.sort(reverse=True)降序排序
列表.reverse() 逆序,反转


"""
























































































