# -*- coding: utf-8 -*-
# 继承方法和属性
# 多重继承

class Bird(object):
    def fly(self):
        print('fly......')


class Fish(object):
    def swim(self):
        print('swim......')


class FlyFish(Bird, Fish):
    pass


ff = FlyFish()
ff.fly()

ff.swim()
