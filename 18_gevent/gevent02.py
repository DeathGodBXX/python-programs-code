import gevent
import time
#打补丁  先导入
from gevent import monkey
#将程序中的耗时操作，自动更改为gevent里的
monkey.patch_all()

def sing():
    for i in range(1, 6):
        print('*****bobo老师在唱第%s歌******'%i)
        time.sleep(0.5)

def dance():
    for i in range(1, 6):
        print('------bobo老师在跳第%s舞------'%i)
        time.sleep(0.5)

def main():
    gevent.joinall([
        gevent.spawn(sing),
        gevent.spawn(dance)
    ])

if __name__ == '__main__':
    main()


#协程 调用switch方法，进行任务切换


#进程 最稳定     耗费资源大
#线程 效率最高   并发
#协程            必须有延迟操作，效率低下


#为何会报错？？？？？？？？？？？？？







