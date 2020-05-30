# 自定义异常类
class Name_error(Exception):
    pass


class Pwd_error(Exception):
    pass


class check_name():
    def __init__(self, name):
        self.name = name

    def check_name_len(self):
        if len(self.name) > 8 or len(self.name) < 3:
            raise Name_error("用户名长度不在3到8个字符之间")

    def check_name_isalnum(self):
        if not self.name.isalnum():  # 无法区分字母数字和汉字，因为汉字转码成字母数字了
            raise Name_error("用户名只能出现英文字母和数字")


class check_pwd():
    def __init__(self, pwd):
        self.pwd = pwd

    def check_pwd_len(self):
        if len(self.pwd) != 6:
            raise Pwd_error("密码只能是六位")

    def check_pwd_isnumeric(self):
        if not self.pwd.isnumeric():
            raise Pwd_error("密码必须是纯数字")


r = 1
while r != 0:
    try:
        user_name = input("请输入用户名:")
        name = check_name(user_name)
        name.check_name_len()
        name.check_name_isalnum()
        user_pwd = input("请输入密码:")
        pwd = check_pwd(user_pwd)
        pwd.check_pwd_len()
        pwd.check_pwd_isnumeric()
    except Name_error as e:
        print(e)
    except Pwd_error as e:
        print(e)
    finally:
        r = int(input("是否继续登录，0结束，非0继续"))














