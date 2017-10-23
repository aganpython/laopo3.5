# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from test1"
df = pd.read_sql(sql,con,index_col="id")
print(df)
#b = random.randint(1000,2000) #随机整数
#b = random.uniform(1000,2000) #随机浮点数
#b = random.choice('abcd') #随机字符
#print(b)
#a = df.fillna(value=0)#使用0替代缺失值
#a = df.fillna('love')#用一个字符串代替缺失值
a = df.fillna(method='pad')#用前一个数据代替NaN：method='pad'
#a = df.fillna(method='bfill')#与pad相反，bfill表示用后一个数据代替NaN。
#a = df.fillna(method='bfill',limit=1)#用limit限制每列可以替代NaN的数目，下面我们限制每列只能替代一个NaN#
#a =df.fillna(df.mean())#使用平均数或者其他描述性统计量来代替NaNi
print(a)



# -*- coding: UTF-8 -*-
