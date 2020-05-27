"""queue 队列"""
# import multiprocessing
# q = multiprocessing.Queue()
# #往队列里添加数据  先进先出 低耦合
# q.put(123)
# q.put("hello")
# q.put([1,2,3])
# print(q.get())
# print(q.get())
# print(q.get())
#
# #等待队列里面的值
# # print(q.get())
# # print(q.get())
# #不等待队列里面的值
# print(q.get_nowait())

"""
模拟子进程A爬数据，子进程B清洗数据
"""

import multiprocessing

def demo1(q):
    """模拟下载数据"""
    data = [i for i in range(1,11)]
    for i in data:
        q.put(i)
    print('所有数据已经全部放进队列当中')

def demo2(q):
    """模拟清洗数据"""
    list1 = []
    while True:
        i = q.get()
        if i % 2 ==0:
            list1.append(i)
        #当队列为空，跳出循环
        if q.empty():
            break
    # while q.empty() == False:
    #     i=q.get()
    #     if i%2 == 0:
    #         list1.append(i)
    print("清洗后的数据结果：", list1)

def main():
    #创建queue队列，共享的
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=demo1, args=(q, ))
    p2 = multiprocessing.Process(target=demo2, args=(q, ))
    p1.start()
    p2.start()

if __name__ == '__main__':
    main()













