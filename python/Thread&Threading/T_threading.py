# -*- coding: utf-8 -*-

import threading
from time import ctime, sleep


def func1():
    for i in range(5):
        print('func1 :%d \n' % i)
        sleep(1)


def func2():
    for j in range(5):
        print('func2 :%d \n' % j)
        sleep(1)


def main():
    print('start:', ctime())
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('end:', ctime())


if __name__ == '__main__':
    main()
