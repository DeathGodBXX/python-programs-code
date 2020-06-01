"""greenlet封装yield"""
from greenlet import greenlet
import time


def sing():
    while True:
        print('*****bobo老师在唱歌******')
        time.sleep(0.5)
        g2.switch()


def dance():
    while True:
        print('------bobo老师在跳舞------')
        time.sleep(0.5)
        g1.switch()


g1 = greenlet(sing)
g2 = greenlet(dance)


def main():
    g1.switch()  # >>>>切换
    # g2.switch()


if __name__ == '__main__':
    main()
