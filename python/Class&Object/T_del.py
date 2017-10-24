# -*- coding: utf-8 -*-
# Python 内存管理是自动完成的,通过垃圾回收器来管理内存,实现原理是引用计数，引用计数为0，自动清除内存
# 析构方法 __del__，当对象被从内存释放时，调用析构方法。

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('del.....')


p1 = Person('agan', '30')
print(p1.name)
print(p1.age)

from time import sleep

counter = 10

while True:
    print('counter:', counter)
    counter -= 1
    sleep(1)
    if counter < 0:
        break
