"""
递归函数，函数内部对自身函数的调用，具有明确的结束标志

"""


# 1到指定函数的求和
# 1到100求和
# 1到99，再加100
# 1到98，再加98
# 。。。。
# python解释器只解决1000次调用以下的递归调用

def sum0(a):
    if a == 1:
        return 1
    return sum0(a - 1) + a


i = sum0(100)
print(i)
