# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql1 = "select * from xs"
sql2 = "select * from xh"
df1 = pd.read_sql(sql1,con,index_col='id')
df2 = pd.read_sql(sql2,con,index_col='id')
for j in range(0,3):
	list = []
	for i in range(0,10):
		a = df1.iloc[j,i]
		b = df2.iloc[j,i]
		c = b/a
		list.append(c)

listj = []
listj.append(list)
e = pd.DataFrame(list,listj)
print(e)
print("is done")
