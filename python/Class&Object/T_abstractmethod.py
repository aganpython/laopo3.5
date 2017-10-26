# -*- coding: utf-8 -*-
# 抽象方法--只有定义，没有实现。
# 一个类里面只要有一个或多个抽象方法，这个类就是抽像类
# 抽象类不能被实例化，只能作为子类被继承
# 接口里面没有任何实现的方法，所有的方法都是抽象方法
# 可以通过普通类来实现接口

# 抽象方法
# class USB(object):
#     def read(self):
#         pass

# 抽象类
# 一个类里面只要有一个或多个抽象方法，这个类就是抽像类
# 抽象类不能被实例化，只能作为父类被继承

import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def run(self):
        pass

    def sleep(self):
        print('sleep....')


class Dog(Animal):
    def run(self):
        print('dog run....')


d = Dog()
d.sleep()
d.run()

# 接口
import abc


class USB(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def read(self):
        pass

    @abc.abstractclassmethod
    def write(self):
        pass


class Computer(USB):
    def read(self):
        print('read....')

    def write(self):
        print('write.....')


c = Computer()
c.read()
c.write()
