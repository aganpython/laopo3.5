# -*- coding: utf-8 -*-

# 实例属性（变量）
# class Site(object):
#     def __init__(self, name, address, phone):
#         self.name = name
#         self.address = address
#         self.phone = phone
#
#     def about(self):
#         print(self.name, self.address, self.phone)
#
#
# site = Site('agan', 'shanghai','13162502812')
# site.about()

# 类属性（变量）

class Site(object):
    name = 'agan'
    address = 'shanghai'
    phone = '13162502812'
    sex = 'nan'

    # 实例方法，可以访问类属性（变量）
    def about(self):
        print(self.name, self.address, self.phone)

    def __init__(self, sex):
        self.sex = sex

    # 静态方法，不能访问实例变量（属性）
    @staticmethod
    def get_sex():
        print(Site.sex)

    # 类方法，不能访问实例变量（属性）
    @classmethod
    def get_msg(cls):
        print(cls.name, cls.address, cls.phone)


Site.get_sex()
Site.get_msg()
site = Site('nan')
site.about()
