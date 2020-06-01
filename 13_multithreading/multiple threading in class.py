"""
利用类实现多线程任务
"""

# import threading
# import time
#
#
# class Demo(threading.Thread):
#     # 必须要有实例方法run，run()固定名称，不可更改 代表线程的启动。
#     # 大概是通过main（）函数中，t1.start，启动这个run函数，线程启动
#     # run方法于线程启动相关
#     def run(self):
#         for i in range(3):
#             time.sleep(0.8)
#             print(threading.enumerate())
#
#
# if __name__ == "__main__":
#     d1 = Demo()
#     d1.start()  # 线程启动
#     time.sleep(3)
#     print(threading.enumerate())

"""**************"""

# import threading
# import time
#
#
# def demo1():
#     print("everything is OK")
#
#
# class Demo(threading):
#     def run(self):
#         d1 = threading.Thread(target=demo1)
#         d1.start()
#         for i in range(3):
#             time.sleep(0.8)
#             print(threading.enumerate())
#
# if __name__ == "__main__":
#     d1 = Demo()
#     time.sleep(3)
#     print(threading.enumerate())

# 报错 class Demo(threading):
# TypeError: module.__init__() takes at most 2 arguments (3 given)


