# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from test1"
df = pd.read_sql(sql,con,index_col='id')
#print(df)
#print(df.index)
# 得出每一列的数据类型
types = df.dtypes
#print(types)
# 选择具有浮点数据的那些列
float_columns = types[types.values == 'float64'].index
#float_df = df[float_columns]
m1 = df.ix[:,['m1']]
m2 = df.ix[:,['m2']]
m3 = df.ix[:,['m3']]
m4 = df.ix[:,['m4']]
# 对选择的列计算总分，在lambda中的x是一个Series，代表了某一列
#count = float_df.apply(lambda x: np.sum(x))
#如果要在行上使用apply()方法，只要指定参数axis = 1即可
#count = float_df.apply(lambda x: np.sum(x),axis = 1)
#print(count)
#将整列（行）的值都分别乘2
mm1 = m1.apply(lambda x: x*3)
mm2 = m2.apply(lambda x: x*100)
mm3 = m3.apply(lambda x: x*150)
mm4 = m4.apply(lambda x: x*200)
d = pd.concat([mm1,mm2,mm3,mm4],axis=1,join='inner')
print(d)
d.to_sql(name = 'test3',con = con,if_exists = 'replace')

print("is done")
