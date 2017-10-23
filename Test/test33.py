# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql1 = "select * from xs"
sql2 = "select * from xh"
df1 = pd.read_sql(sql1,con,index_col='id')
df2 = pd.read_sql(sql2,con,index_col='id')
#print(df1)
#print(df2)
a1 = df1.iloc[1,0]
b1 = df2.iloc[1,0]
print(a1)
print(b1)
c1 = b1/a1
print(c1)
a2 = df1.iloc[1,1]
b2 = df2.iloc[1,1]
c2 = b2/a2
print(c2)
a3 = df1.iloc[1,2]
b3 = df2.iloc[1,2]
c3 = b3/a3
print(c3)