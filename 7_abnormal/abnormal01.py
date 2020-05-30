"""
异常处理
语法格式一:一旦出现异常，直接执行except的处理代码
try:
    可能出现异常的代码
except：
    如果出现异常，替代处理的代码

"""

"""
语法格式二:
try:
    可能出现异常的代码
except：
    处理代码
finally:
    try代码结束后运行的代码(try和except可能同时要执行的文件)

"""

print("程序开始")
try:
    file1 = open("zhangfeipo04Big.f4v", "rb")  # read成功执行 打开一个文件
    file_context = file1.read()
    file1.write("找美美聊天")  # 写，引发异常
    # file1.close()              #执行不到 关闭文件
except:
    print("文件读取结束")
finally:
    file1.close()

print("程序结束")  # 执行不到
#

# a=1
# b=0
# if b==0:
#     raise ZeroDivisionError("division by zero")
# raise 抛出异常
