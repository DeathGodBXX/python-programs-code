import time


def sing():  # 函数含有yield，为生成器模板
    while True:
        print("***bobo老师再唱歌***")
        time.sleep(0.3)
        yield  # 暂停，切换


def dance():
    while True:
        print("----bobo老师在跳舞-----")
        time.sleep(0.5)
        yield  # 暂停，切换


def main():
    s1 = sing()
    d1 = dance()
    while True:
        try:
            next(s1)  # 生成器模板，利用next()取值
            next(d1)
        except Exception:
            break


if __name__ == '__main__':
    main()

# 单进程，单线程，多任务  并发  协程
# 多线程，多进程，耗费资源
