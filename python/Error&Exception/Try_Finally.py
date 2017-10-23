# -*- coding: UTF-8 -*-
#try-finally语法
# try:
#     程序代码...
# except IndexError as ie:
#     处理异常...
# finally:
#     不管是否有异常发生都会执行的代码块,
# 注意：finally部分的代码块，不管是否有异常发生，都会执行，常用来释放系统资源，例如：打开的外部文件、数据库连接等。

#1

# l = [1,2,3]
# try:
#     print(l[10])
# except IndexError as ie:
#     print('索引越界')
#     print(ie)
# finally:
#     print('不管是否有异常发生都会执行的代码块')

#2

# f = open('test.txt')
# age = int(f.read())
# print(age)
# f.close()
# print('end.....')

#3
try:
    f = open('test.txt')
    age = int(f.read())
    print(age)
except Exception as e:
    print(e)
finally:
    f.close()
    print('文件被关闭')
print('end.....')