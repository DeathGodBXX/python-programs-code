# input()函数

# name=input("请输入你的名字:")
# print(name)
# print(type(name))

# input()函数得到的都是字符型
# 数据类型的转换str>>>int
# a = input("请输入第一个数字:")
# b = input("请输入第二个数字:")
# print(a+b)  #input()函数得到的都是字符型，如果不加类型转换，只是两个相加，只是连接两个字符

# a = int(input("请输入第一个数字:"))
# b = int(input("请输入第二个数字"))
# print(a+b)

# a = input("请输入第一个数字:")
# b = input("请输入第二个数字:")
# print(int(a)+int(b))


# 格式化输出
# name = "历史"
# print("这个人的名字:%s"%name)

# name="李四"
# gender="男"
# age=23
# height=1.8
# print("这个人的名字:%s,性别:%s,年龄:%d,身高:%.2f"%(name, gender, age, height))   #必须用括号括起来
# print("这个人的名字:%s,性别:%s,年龄:%d,身高:%.2f"%name, %gender, %age, %height)   #运行错误，无效语法
# %s 字符串型 %d 整型数 %f 浮点型
# %.3f 浮点型,保留三位小数,而且五舍六入  %4d 整型数,不够的话，前面补上空格
#%% 输出%
# a = 13.35
# print('a =%5.1f'%a) #%m.nf // n表示小数位数，不足则补0，多了就五舍六入；
                    # m-n-1表示要保留的整数位数，如果比实际整数位数多，则整数前补充空格，少的话，左对齐，无变化

"""
演示比较运算符
"""
"""
== 判断是否相等
!= 不等于
> 大于
< 小于
>=大于等于
<=小于等于
"""

"""
比较关系运算符
判断题:
1和3都是整数 and 两个都正确，整体才为true
1或3是int 型, or (或)
1不是 int型   not 否定

"""
# print(1 and 3 is int)  #1，3的类型确实是int,但是不取出类型，则只是判断 数值1和3是否等于int
# print(type(1 and 3)is int)
# print(1 is 1)
# print(1 is 3)
# print(type(1) is int)

"""
if type(1 and 3) is int:
    print("1和3都是整数")
else:
    print("1和3至少有一个不是整数")


if type(1 or 3.0) is int:
    print("1或者3.0是整数")
else:
    print('1和3.0都不是整数')


if type(1) is not int:
    print("1不是整数")
else:
    print("1是整数")

"""


"""
演示if分支语句

小明，考试了
100，游戏机
90，游乐园
80，玩具
60到80，功过相抵
小于60，小心屁股
if 条件：
  前面要缩进+ 执行代码
if 条件：
  缩进+执行代码
else：
  缩进加代码

"""

b = input("请输入你的成绩:")
# print(type(b))#默认的输入类型都是str 想编程数值型，必须类型转换
a = int(b)
if a == 100:
    print("奖励游戏机")
elif a >= 90:
    print("周末去游乐园")
elif a >= 80:
    print("奖励一个玩具")
elif a >= 60:
    print("什么奖励都没有")
else:
    print("屁股要倒霉了")








# print("我吃了早饭")
# if 条件:#tab键缩进
#     执行代码
# if False:
#     print("我吃了午饭")
# if True:#系统有个默认值True
#     print("我吃了午饭")
# print("我吃了晚饭")
"""
两个数字进行比较，打印较大值


"""

# a = 2
# b = 3
# if a>b:#a较大，打印a
#     print(a)
# else:#a<=b ，打印b
#     print(b)

"""
通过键盘输入得到一个值，判断是偶数还是奇数
"""

"""
a =int(input("请输入一个数字:"))#进行类型转换
if a%2==0:
    print("%s是偶数"%a)
else:
    print("%s7是奇数"%a)
"""






















