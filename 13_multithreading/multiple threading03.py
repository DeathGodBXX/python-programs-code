"""
利用类实现多线程任务
"""



# import threading
# import time
#
# class Demo(threading.Thread):
#     #必须要有实例方法，run()固定名称，不可更改
#     def run(self):
#         for i in range(3):
#             time.sleep(0.8)
#             print(threading.enumerate())
#
# if __name__=="__main__":
#     d1=Demo()
#     d1.start() #线程启动
#     time.sleep(3)
#     print(threading.enumerate())

import threading
import time
def demo1():
    print("everything is OK")
class Demo(threading):

    def run(self):
        d1 = threading.Thread(target=demo1)
        d1.start()
        for i in range(3):
            print(i)
            time.sleep(0.8)
    print(threading.enumerate())

if __name__=="__main__":
    d1=Demo()




# """多线程共享全局变量"""
# import threading
# import time
#
# num1=1
# #修改全局变量，global
# #可变类型和不可变类型   global添加在不可变类型前
# def demo1():
#     global num1
#     num1+=1
#     print("在demo1中，num1的值是:",num1)
#
# def demo2():
#     # global num1
#     # num1+=1
#     print("在demo2中，num1的值是:",num1)
#
# def main():
#     t1=threading.Thread(target=demo1)
#     t2=threading.Thread(target=demo2)
#     t1.start()
#     time.sleep(0.8)
#     t2.start()
#     time.sleep(0.9)
#     print("在main函数中，num1的值为:",num1)
#
# if __name__=="__main__":
#     main()





















