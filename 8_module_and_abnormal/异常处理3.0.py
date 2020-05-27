# name="小明同学"
# def check_name(name):
#     if name.find==1:
#         print(f"{name}是反清分子，杀头")
#     else:
#         print(f"{name}是良民")
# check_name(name)




#企业级处理异常，不写死，灵活性提高。。。
name="波小明同学"
age=22
def check_name(name):
    if name.find("明")>=0:
        raise NameError ("这个人是个反清分子")#python抛出异常的方式，利用raise抛出

def check_age(age):
    if age>20:
        raise ValueError("这个人该当兵了")


try:
    check_name(name)
except NameError:
    print("这个人名字没问题")

try:
    check_age(age)
except ValueError:
    print("这个人不用当兵")














