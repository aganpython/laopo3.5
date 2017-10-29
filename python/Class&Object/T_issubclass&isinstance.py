# -*- coding: utf-8 -*-
# issubclass

# class Animal(object):
#     pass
#
# class dog(Animal):
#     pass
#
# class cat(object):
#     pass
# print(issubclass(dog,Animal))
# print(issubclass(cat,Animal))

# isinstance

# class Animal(object):
#     pass
#
#
# class dog(Animal):
#     pass
#
#
# class cat(object):
#     pass
#
#
# d = dog()
# c = cat()
#
# print(isinstance(d, dog))
# print(isinstance(c, Animal))

# 属性操作
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#
# p = Person('agan')
# print(hasattr(p, 'name'))
# print(getattr(p, 'name'))
# setattr(p, 'name', 'big agan')
# print(p.name)

# dir()
# vars() 和 dir() 类似，只是给定的对象必须有一个——dict——属性

class Person(object):
    def __init__(self, name):
        self.name = name


p = Person('agan')
print(dir(p))
print('vars starting \n')
print(vars(p))
