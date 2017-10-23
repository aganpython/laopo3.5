# 构造方法也叫初始化方法
#
# 构造方法是一个特殊的方法，名称为：init
#
# 作用是用来初始化实例变量
#
# 当实例化变量时调用

#1
# class Person(object):
#     def __init__(self):
#         print('init....')
#
# per = Person()

#2
'''
class Person(object):
    def __init__(self, name, age):
        self.per_name = name
        self.per_age = age

per = Person('agan', 29)
print(per.per_name,per.per_age)
'''

'''
默认构造方法

没有参数的构造方法就是默认的

系统默认提供

如果自己定义了新的构造方法，默认构造方法就不存在了

python 不支持方法重载

也不支持构造方法重载
'''
