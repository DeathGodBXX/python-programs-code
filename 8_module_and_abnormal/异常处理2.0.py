# def demo1():
#     print(i)
# def demo2():
#     try:
#         demo1()
#     except:
#         print("傻逼波波已解决")#异常的拦截
# def demo3():
#     demo2()
# try:
#     demo3()
# except:
#     print("bobo傻逼已解决")
try:
    def demo1():
        print()
    def demo2():
        try:
            demo1()
        except:
            print("demo1()出错")
    def demo3():
        demo2()

demo3()
except ZeroDivisionError:
    print("0做除数了")
















