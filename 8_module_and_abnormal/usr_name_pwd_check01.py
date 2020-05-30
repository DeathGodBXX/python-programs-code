user_name = input("请输入用户名:")
user_pwd = input("请输入密码:")


# 自定义异常类
class Name_error(Exception):
    pass


class Pwd_error(Exception):
    pass


def check(name, pwd):
    if len(name) > 8 or len(name) < 3:
        raise Name_error("用户名长度不在3到8个字符之间")
    if not name.isalnum():
        raise Name_error("名字只能出现英文字母和数字")
    if len(pwd) != 6:
        raise Pwd_error("密码长度必须是六位")
    if not pwd.isnumeric():
        raise Pwd_error("密码不是纯数字")


try:
    check(user_name, user_pwd)
except Name_error as e:
    print(e)
except Pwd_error as e:
    print(e)

# usr_name = input("请输入用户名：")
# if usr_name >= u'\u4e00' and usr_name <= u'\u9fa5':  # 与汉字编码相关的
#     print("True")
# else:
#     print("False")
