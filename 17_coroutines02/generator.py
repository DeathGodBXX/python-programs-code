"""
生成器
"""
#生成器是特殊的迭代器
#可以使用next()函数取值
#但是内部没有__next__方法和__iter__方法

#列表推导式
#最简单的生成器 generator 特殊迭代器  >>>for循环可以取值   保存生成数据的代码
# list1 = [i for i in range(1, 11)]
# print(list1)
#
#
# print(i for i in range(1,11))
# list2 = (i for i in range(1, 11))
# print(len(list2))  #生成器无法使用len()，由于生成器是一次取一个，惰性计算，不知道后续有多少个数据。
#上述生成器代码先打印，再赋值，再打印，内存地址是一样的；
# 如果先赋值，再打印两次，内存地址改变
# 原因:赋值式的左右两端，左端可见，右端不可见,如果没用变量保存右端的话

# print(list2)
# print(id(list2))
#
# for i in list2:
#     print(i, end=',') 生成器利用for,可以取值



#生成器的表现形式 生成器模板
#1。是一个函数，保存生成数据的代码
#2。内部必须要有关键字 yield

# 0,1,1,2 ,3,5,8,13,21,....
def fei_bo(n):
    """生成斐波那契数列"""
    a,b =0, 1
    start_num = 0
    while start_num < n:
        name = yield a
        print(name)
        a,b =b,a+b
        start_num+=1
    #while循环结束，抛出StopIteration ，再return
    return "波霸在秀波"

#如果default有值，不会抛出StopIteration,而是返回default的值；如果default没值，会抛出StopIteration
fei_bo1 = fei_bo(5)
print(next(fei_bo1))
fei_bo1.send('逼霸在秀逼')  #send和next()都有启动yield的能力

#send不要用在第一次生成器模板中，由于先执行yield a,先next(),再send()
#TypeError: can't send non-None value to a just-started generator

for i in fei_bo1:
    print(i,end=',')  #由于send，类中print(name)了，第一次a=1也返回了，但是没有变量接收打印，所以最后结果只有一个1























