# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import pandas as pd
import pymysql
import numpy as np

# 打开数据库连接
con = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='laopo', charset='utf8')
#sql = "select * from test"
sql = "SELECT city,`2000年环境治理投资`,`2001年环境治理投资`,`2002年环境治理投资`,`2003年环境治理投资`FROM test"
df = pd.read_sql(sql,con,index_col="city")
#print(df.fillna(value=0))
print(df.sort_values("2000年环境治理投资"))

#print(df.head(4))
#print(df.T)

con.close()
print("is done")

#df = pd.read_sql(sql,con,index_col=["id","city"])
#print df.tail(6)
#print df.head()
#print df.dtypes
#print df.columns
#print df.index
#print df.values

#print df[0:3]
#print df[2:3]
#print df['A']
#print df.loc[2]
#print df.loc[2,'C']
#print df.iloc[1:3,1:3]
#逐个不连续的筛选
#print df.iloc[[0,3],2:4]
#mixed selection:ix

#print df.ix[:2,['A','D']]
#Boolean indexing 是否筛选
#print df[df.A>500]

#只要一行里面有一个空值，这一行就全删除了
#print df.dropna(axis=0,how='any')
#只要一列里面有一个空值，这一列就全删除了
#print df.dropna(axis=1,how='any')
#只有一列里面全是空值，这一列才删除
#print df.dropna(axis=1,how='all')
# 填充数据 把 空值全部填充成0

# 通过这个函数，当有空值时，显示True
#print df.isnull()
# 当面对一大片数据时，不容易用肉眼判断数据表中是否有空值，可以用np.any来判断，返回True,说明里面有空值
#print np.any(df.isnull()==True)

#按轴排序  True 正序、False 倒序 默认True
#print df.sort_index(axis=0,ascending=False)
#print df.sort_index(axis=1,ascending=False)
#print df.sort_index(axis=1,ascending=True)
#print df.sort_index(axis=0,ascending=True)
#转置数据
#print df.T
#描述显示数据快速统计摘要
#print df.describe()