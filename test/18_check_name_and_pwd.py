class RegisterError(Exception):
    pass


def check_name_and_pwd(name, pwd):
    if (name == 'seven' and pwd == '123') or (name == 'alex' and pwd == '456'):
        print('登录成功')
    else:
        raise RegisterError('登录失败，请重新登录')


i = 1
while i <= 3:
    try:
        name = input('请输入用户名：')
        pwd = input('请输入密码：')
        check_name_and_pwd(name, pwd)
        break
    except Exception as e:
        print(e)
        i = i + 1
