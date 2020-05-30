"""
while 循环语法
语法格式：
while 条件：
    反复执行的代码
"""

# i=1           # 循环变量
# while i<=5:
#     print("hello,武汉加油")
#     i+=1

# 1.缩进非常重要，如果i+=1没有缩进，不进入while循环。：+ 缩进 等同于c中{......}内容
# 2.没有；
# 3.input("....")起着print()的作用，
# 4.把input（）返回值类型为string，如果想修改类型，需要强制类型转换int(input(.....)),不同于c中的（int）scanf（“...”,变量地址）

# input('请输入一个数值:')

"""
循环变量，死循环
"""

# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print("100以内整数相加得到:%s"%sum)

"""
演示循环的跳出和终止
"""

# num1=0
# while num1<10:
#     num1+=1
#     if num1==9:
#         continue
#     print("小明抄写了第%s遍"%num1)
# break跳出整个循环，continue跳出本轮循环接着循环后续过程（跳过本次循环的后续代码）

"""
循环嵌套的演示
"""
j = 1
while j <= 3:
    i = 1
    while i <= 3:
        print(i, end=" ")
        i += 1
    print()
    j += 1

"""
*
**
***
****
*****
"""
# j=1
# while j<=5:
#     i=1
#     while i<=j:
#         print("*",end="")#修改print()函数默认的换行
#         i+=1
#     print()#默认换行
#     j+=1

# print(1 == 3)
# print(1 == 3)
# print(1 == 3)
# print(1 == 3)
# print(1 == 3)
# print(1 == 3)
# print(1 == 3)

# 快速复制上一行 Ctrl+D Edit>>Duplicate line
# 撤销上一步操作  Edit>>Undo Ctrl+z
# 反撤销上一步操作 Edit>>Redo Ctrl+shift+z
