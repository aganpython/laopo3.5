# -*- coding: utf-8 -*-
# 类和类之间的关系：继承、组合
# 依赖关系-参数传递
# 关联关系-一个类包含另外一个类
# 如何使用 继承和组合 has a 还是 is a


class Author(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Course(object):
    def __init__(self, name, runtime, author):
        self.name = name
        self.runtime = runtime
        self.author = author


class Site(object):
    def __init__(self, name, address, courses):
        self.name = name
        self.address = address
        self.courses = courses


a = Author('agan', 30)
c1 = Course('aaa', 111, a)
c2 = Course('bbb', 222, a)

s = Site('www', 'wwww.haha.com', [c1, c2])

print(s.name)
print(s.address)

courses = s.courses
for c in courses:
    print(c.name,c.runtime,c.author.name)