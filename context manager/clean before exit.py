import atexit
import time


@atexit.register
def clean():
    print('清理任务')


def main():
    time.sleep(1)
    1 / 0


main()

# 程序退出前，执行的操作

