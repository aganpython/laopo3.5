# -*- coding: UTF-8 -*-
#raise 主动抛出异常
#raise可以在一定条件下，主动抛出异常。
#assert 断言
#当assert函数中的表达式运算结果为False时，就会抛出一个AssertionError异常。

# 1
# l = [1,2,3]
# index = 1
#
# if index >= len(l):
#     raise IndexError
# else:
#     print(l[index])

#2
# a = 0
# b = 10
# if a ==0:
#     raise ZeroDivisionError
# else:
#     print(b/a)

#3 常用于调整程序，判断程序是否正确
# a = 101
# assert (a == 101)
s = input('输入你的年龄：')
age = int(s)
assert (age > 0)
print(age)
