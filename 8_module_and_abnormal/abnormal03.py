name = "小明同学"


# def check_name(name):
#     if name.find("明"):
#         print(f"{name}是反清分子，杀头")
#
#     # python的print字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式，如果字符串里面没有表达式，那么前面加不加f输出应该都一样.
#     else:
#         print(f"{name}是良民")
#
#
# check_name(name)

# 企业级处理异常，不写死，灵活性提高。。。


def check_name(name):
    if name.find("明") >= 0:
        raise NameError("这个人是个反清分子")  # python抛出异常的方式，利用raise抛出


def check_age(age):
    if age > 20:
        raise ValueError("这个人该当兵了")


# try:
#     name = input('请输入姓名：')
#     check_name(name)
#     print("这个人名字没问题")
# except NameError as e:  # e用来接收NameError后面的返回值
#     print(e)
#
# try:
#     age = int(input('请输入年龄：'))
#     check_age(age)
#     print("这个人不用当兵")
# except ValueError as e:
#     print(e)

if __name__ == '__main__':
    r = 1
    while True:
        try:
            name = input('请输入姓名：')
            check_name(name)
            print('这个人名字没问题')
        except NameError as e:
            print(e)
        finally:
            try:
                age = int(input('请输入年龄：'))
                check_age(age)
                print('这个人年龄没问题')
            except ValueError as e:
                print(e)
        r = int(input('是否想继续查询姓名和年龄，请输入数字：（0表示结束,其他表示继续）'))
        if r == 0:
            break



