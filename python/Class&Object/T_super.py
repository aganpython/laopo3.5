# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


# super 引用父类
class Manager(Person):
    def __init__(self):
        super().__init__('agan', 30)

    def m_display(self):
        super().display()
        print('先父类的，再子类的')


m = Manager()
m.m_display()
