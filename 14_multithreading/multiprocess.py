import multiprocessing
# 线程占用资源少，进程占用资源多，进程更依赖于cpu核数，更能并行  无序输出
import time
import os  # 获取进程号


def sing():
    for i in range(3):
        print("波霸在秀奶")
        print("奶霸的id是：", os.getpid())
        time.sleep(0.8)


def dance():
    for i in range(3):
        print("逼霸在秀逼")
        print("逼霸的id是：", os.getpid())
        time.sleep(0.8)


def main():
    t1 = multiprocessing.Process(target=sing)
    t2 = multiprocessing.Process(target=dance)
    t1.start()
    t2.start()
    time.sleep(3)
    print("主进程的id是：", os.getpid())


if __name__ == "__main__":
    main()
