#-*- coding: utf-8 -*-
class Myclass(object):
    cv = 1
#使用@staticmethod标示，可以不用实例化，直接通过类名称调用
    @staticmethod
    def mystaticm1():
        print('this is static....')

#类方法和静态方法类似，使用@classmethod标示，但是第一个参数必须是类本身cls
    @classmethod
    def myclassm1(cls):
        print('this is class....')
#实例方法,必须实例化才能调用,静态方法不能访问实例变量，也不能访问类变量，python没有静态变量
    def myinstancem1(self):
        print('this is instance......')

Myclass.mystaticm1()
Myclass.myclassm1()

a = Myclass()
a.myinstancem1()