# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql1 = "select * from xs"
sql2 = "select * from xh"
df1 = pd.read_sql(sql1,con,index_col='id')
df2 = pd.read_sql(sql2,con,index_col='id')
list = []
for i in range(0,10):
	a = df1.iloc[0,i]
	b = df2.iloc[0,i]
	c = b/a
	list.append(c)
list1 = []
list1.append(list)
e = pd.DataFrame(list1)
print(e)
print("is done")
