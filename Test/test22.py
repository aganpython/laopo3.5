# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from qq2014"
df = pd.read_sql(sql,con,index_col='id')
#计算各列数据总和并作为新列添加到末尾
df['Col_sum'] = df.apply(lambda x: x.sum(), axis=1)
#计算各行数据总和并作为新行添加到末尾
#df.loc['Row_sum'] = df.apply(lambda x: x.sum())
#计算选中行、选中几列的和
list=[]
for i in range(len(df)):
	b = df.loc[i,['q23','q26','q29']].sum()
	#找到选中行，最后一列的值
	c = df.iloc[i,-1]
	d = b/c
	list.append(d)
list1 = []
list1.append(list)
#e = pd.DataFrame(list1,columns=['1','2','3','4'])
e = pd.DataFrame(list1)
f = e.T
#g = pd.concat([df,f],axis=1,join='inner')
g = pd.merge(df,f,how='left',left_index=True,right_index=True)
print(df)
print(b)
print(c)
print(e)
print(f)
print(g)
g.to_sql(name = 'qqq2014',con = con,if_exists = 'replace')
print("is done")