# -*- coding: UTF-8 -*-

#1.语法错误，SyntaxError: invalid syntax
# def f1()
#     print('f1.....')

#SyntaxError: invalid syntax

#2.0不能做分母错，ZeroDivisionError
# a, b = 0,1
# print(b/a)

#ZeroDivisionError: division by zero

#3.索引越界错误，IndexError

# l = [1, 2, 3, 4, 5]
# print(l[100])

# IndexError: list index out of range

#4.类型错误，ValueError
# x = int('abc')

# ValueError: invalid literal for int() with base 10: 'abc'

#5.变更或函数没有被定义，NameError

# print(x)

# NameError: name 'x' is not defined

#6.文件未找到错误，FileNotFoundError
# f = open('c:/test/test.txt')

# FileNotFoundError: [Errno 2] No such file or directory: 'c:/test/test.txt'

#7.ModuleNotFoundError
# import xxx

# ModuleNotFoundError: No module named 'xxx'

#8.ImportError
#from sys import xxx

# ImportError: cannot import name 'xxx'

