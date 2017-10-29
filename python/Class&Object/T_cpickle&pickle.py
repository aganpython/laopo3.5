# -*- coding: utf-8 -*-
try:
    import cPickle as pickle
except ImportError:
    import pickle


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('agn', '30')


# 对象序列化 就是把对象持久保存成文件格式
# 使用pickle 的dumps 或者 dump 序列化
def write():
    with open('test.data', 'wb') as f:
        b = pickle.dumps(p)
        f.write(b)


# 对象反序列化 就是把对象从文件转换为对象
# 使用pickle 的load方法反序列化
def read():
    with open('test.data', 'rb') as f1:
        p = pickle.load(f1)
        print(p.name)
        print(p.age)


write()
read()

# 不光是对象，像列表，字典都可以
