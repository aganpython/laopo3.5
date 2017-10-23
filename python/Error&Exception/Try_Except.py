# -*- coding: UTF-8 -*-

#1 未加异常处理

# def loop(l):
#
#     print(l[6])
#
# loop([1,2])
# print("结束了")

#2 加了异常处理
# def loop(l):
#     try:
#         print(l[6])
#     except Exception as e:
#         print("发生了错误")
#
# loop([1,2])
# print("结束了")

#3
# age = input("请输入年龄")
# int_age = int(age)
# print(int_age)
# print('其他程序执行')

#4
# age = input("请输入年龄:...")
# try:
#     int_age = int(age)
#     print(int_age)
# except ValueError as ve:
#     print('输入类型出现错误')
#     print(ve)
#
# print('其他程序执行')

#5
# l = [1,2,3]
# a, b = 0,1
#
# print(l[5])
# print(b/a)
# print(x)
# print('end.....')

#6
# l = [1,2,3]
# a, b = 0,1
#
# try:
#     print(l[5])
# except IndexError as ie:
#     print('索引越界')
#     print(ie)
# try:
#     print(b/a)
# except ZeroDivisionError as zde:
#     print('除数不能为0')
#     print(zde)
# try:
#     print(x)
# except NameError as ne:
#     print('变量没有定义')
#     print(ne)
# print('end.....')

#7
l = [1,2,3]
a, b = 0,1

try:
    print(l[5])
    print(b / a)
    print(x)
except IndexError as ie:
    print('索引越界')
    print(ie)

except ZeroDivisionError as zde:
    print('除数不能为0')
    print(zde)

except NameError as ne:
    print('变量没有定义')
    print(ne)
print('end.....')

