# def demo1():
#     print(i)
# def demo2():
#     try:
#         demo1()
#     except:
#         print("傻逼波波已解决")#异常的拦截
# def demo3():
#     demo2()
#
# try:
#     demo3()  #demo3调用demo2,demo2正常使用异常处理运行，但是里面的demo1运行出错，所以只有demo2报错，demo3不报错
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
















