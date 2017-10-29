# -*- coding: utf-8 -*-

class Foo(object):
    a = 1
    _b = 2
    __c = 3
    def __init__(self, x, y, z):
        self.x = x
        self._y = y
        self.__z = z
    def m1(self):
        print('m1')
    def _m2(self):
        print('m2')
    def __m3(self):
        print('m3')

print(Foo.a)
print(Foo._b)
#print(Foo.__c)
print(Foo._Foo__c) # python 没有真正的访问控制，只是通过变量名称来约定

f = Foo(100, 200, 300)
print(f.x)
print(f._y)
#print(f.__z)
print(f._Foo__z)

f.m1()
f._m2()
#f.__m3()
f._Foo__m3()


# 前面有一个下划线 ——foo 是受保护的（自己和继承可以使用）
# 前面有两个下划线 ————foo 是私有的（自己可以使用）