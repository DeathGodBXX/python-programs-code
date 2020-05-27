#线程看似多任务，线程Cpython GIL 全局解释锁 快速的切换，假的多任务
import time
import threading
def sing():
    for i in range(3):
        print("波霸老师在唱歌")
        time.sleep(0.8)

def dance():
    for i in range(3):
        print("波霸老师在跳舞")
        time.sleep(0.8)  #CTRL+鼠标点函数名

def main ():
    t1= threading.Thread(target=sing) #创建对象 子线程
    t2= threading.Thread(target=dance)#子线程
    t1.start()#线程的启动,调用
    t2.start()

if __name__=="__main__":
#主线程 子线程  主线程等待子线程全部结束之后才结束
    main()















































































