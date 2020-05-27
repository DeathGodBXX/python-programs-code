import gevent
import time

def sing():
    for i in range(1,6):
        print('*****bobo老师在唱第%s歌******'%i)
        gevent.sleep(0.5)
        #不认可其他函数的延迟操作time.sleep(0.5)

def dance():
    for i in range(1,6):
        print('------bobo老师在跳第%s舞------'%i)
        gevent.sleep(0.5)

#创建对象
g1 = gevent.spawn(sing)
g2 = gevent.spawn(dance)

def main():
    g1.join()
    g2.join()

if __name__ == '__main__':
    main()


#协程 调用switch方法，进行任务切换

























