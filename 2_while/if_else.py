"""
演示if分支语句语法格式三
if 条件一：
    执行代码
elif 条件二:
    执行代码
else ：
    执行代码
"""

"""
num=int(input("请输入你的成绩:"))
if num==100:
    print("去游乐园")
elif num>=90:
    print("玩具")
else:
    print("nothing")
"""

# 输入一个数字，首先判断是否不大于10，再判断是否是偶数
num1 = int(input("请输入一个数字:"))
if num1 <= 10:
    if num1 % 2 == 0:
        print("%s是偶数" % num1)
    else:
        print("%s是奇数" % num1)
else:
    print("这个数大于10")
































