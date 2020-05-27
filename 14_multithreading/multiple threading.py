"""互斥锁"""


import threading
import time

num1=0
def demo1(a):
    #最好不要对整个进程加锁，否则就跟单线程一样
    # lock1.acquire()
    global num1
    for i in range(a):
        lock1.acquire()
        num1+=1
        lock1.release()
    time.sleep(0.8)
    print("在demo1中，num1的数值为:",num1)
    # print(len(threading.enumerate()), "\n", threading.enumerate())
    # lock1.release()

def demo2(a):
    # lock1.acquire()
    global num1
    for i in range(a):
        lock1.acquire()
        num1+=1
        lock1.release()
    time.sleep(0.8)
    print("在demo2中，num1的数值为:",num1)
    # print(len(threading.enumerate()), "\n", threading.enumerate())
    # lock1.release()
#创建互斥锁
lock1=threading.Lock() #


def main():
    a=10
    t1=threading.Thread(target=demo1, args=(a,))#实例方法，传参
    t2=threading.Thread(target=demo2, args=(a,))
    # print(len(threading.enumerate()), "\n", threading.enumerate())
    t1.start()
    t2.start()
    #如果demo1,demo2不添加sleep，只能查到一个主线程，除非a较大
    print(len(threading.enumerate()), "\n", threading.enumerate())
    time.sleep(3)
    print("在main函数中，num1的数值为:", num1)

if __name__=="__main__":
    main()




#原子性




















































