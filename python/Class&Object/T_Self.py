'''

    self:是指当前对象本身
    在类里面的方法第一个参数必须是self
    self 其实是可以写成this的
    self 一般用来指定同名的实例变量与参数

'''


# 1
# 谁调用我，当前对象就是谁。
# self:是指当前对象本身 ，此例中self为P1
# class Person(object):
#     def __init__(self):
#         print(id(self))
# p1 = Person()
# print(id(p1))

# 2
# class Person(object):
#     def say_hello(self, name):
#         print(id(self))
#         print('hello, ', name)
#
#
# p1 = Person()
# print(id(p1))
# p1.say_hello('agan')

# 3 self 一般用来指定同名的实例变量与参数
class Animal(object):
    def eat(this, milk):
        this.milk = milk


a = Animal()
a.eat('milk')

# 4 self 一般用来指定同名的实例变量与参数
# self.milk 表示实例变量
# milk 表示参数
# class Animal(object):
#     def eat(self,milk):
#         self.milk = milk
# a = Animal()
# a.eat('agan')
