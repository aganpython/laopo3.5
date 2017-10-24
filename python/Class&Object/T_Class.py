# 类和对象
#
# 类是抽象的、是一个模板
# 对象是具体的、是类的一个实例


# 1 实例人骑车
# class Person(object):
#     def ride(self,b):
#         b.run()
#
# class Bicycle(object):
#     def run(self):
#         print('run.....')
#
# b = Bicycle()
# tom = Person()
#
# tom.ride(b)

# 2
# class ClassName(object):
#     属性定义
#     方法定义

# class Animal(object):
#     aid = 123
#     def eat(self):
#         print('eat...')
#     def drink(self):
#         print('drink....')
#
# a = Animal() #类的实例化
# a.eat()
# a.drink()

# 3

class Person(object):
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name


p = Person(100, 'agan')

print(p.pid, p.name)
