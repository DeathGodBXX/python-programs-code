"""任务远远多于进程池"""
import multiprocessing
import os, time, random
def demo(msg):
    t_start = time.time()
    print('马%s开始执行，进程号是%d'%(msg, os.getpid()))
    #random.random()随机生成0-1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, '执行完毕，耗时%.2f'%(t_stop - t_start))

if __name__ == '__main__':
    po = multiprocessing.Pool(3)#最大三个进程池
    print('------start-------')
    for i in range(1,11):
        po.apply_async(demo, (i,) )
        #实列对象.apply_async(调用目标，(传递的参数元组,))
        #每次循环，将使用空闲进程
    po.close()#关闭进程池，不再接收请求
    po.join() #等待po中所有子进程执行完毕，必须放在close（）之后
    print('-------end--------')

















