# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from m2010"
df = pd.read_sql(sql,con,index_col='id')
# 得出每一列的数据类型
types = df.dtypes
# 选择具有浮点数据的那些列
float_columns = types[types.values == 'float64'].index
#float_df = df[float_columns]  所有的列
m1 = df.ix[:,['m1']]
m2 = df.ix[:,['m2']]
m3 = df.ix[:,['m3']]
m4 = df.ix[:,['m4']]
m5 = df.ix[:,['m5']]
m6 = df.ix[:,['m6']]
m7 = df.ix[:,['m7']]
m8 = df.ix[:,['m8']]
m9 = df.ix[:,['m9']]
m10 = df.ix[:,['m10']]
m11 = df.ix[:,['m11']]
m12 = df.ix[:,['m12']]
m13 = df.ix[:,['m13']]
m14 = df.ix[:,['m14']]
m15 = df.ix[:,['m15']]
m16 = df.ix[:,['m16']]
m17 = df.ix[:,['m17']]
m18 = df.ix[:,['m18']]
m19 = df.ix[:,['m19']]
m20 = df.ix[:,['m20']]

#将整列的值都分别乘
mm1 = m1.apply(lambda x: x*10000*1000*0.7143)
mm2 = m2.apply(lambda x: x*10000*1000*0.9)
mm3 = m3.apply(lambda x: x*10000*1000*0.2857)
mm4 = m4.apply(lambda x: x*10000*1000*0.2857)
mm5 = m5.apply(lambda x: x*10000*1000*0.9714)
mm6 = m6.apply(lambda x: x*100000000*0.5714)
mm7 = m7.apply(lambda x: x*100000000*0.1786)
mm8 = m8.apply(lambda x: x*10000*1000*1.4286)
mm9 = m9.apply(lambda x: x*10000*1000*1.4714)
mm10 = m10.apply(lambda x: x*10000*1000*1.4714)
mm11 = m11.apply(lambda x: x*10000*1000*1.4571)
mm12 = m12.apply(lambda x: x*10000*1000*1.4286)
mm13 = m13.apply(lambda x: x*10000*1000*1.7143)
mm14 = m14.apply(lambda x: x*10000*1000*1.5714)
mm15 = m15.apply(lambda x: x*100000000*1.33)
mm16 = m16.apply(lambda x: x*10000*1000*1.1429)
mm17 = m17.apply(lambda x: x*10000*1000*0.5571)
mm18 = m18.apply(lambda x: x*0.03412/1000)
mm19 = m19.apply(lambda x: x*100000000*0.1229)
mm20 = m20.apply(lambda x: x*10000*1000)
d = pd.concat([mm1,mm2,mm3,mm4,mm5,mm6,mm7,mm8,mm9,mm10,mm11,mm12,mm13,mm14,mm15,mm16,mm17,mm18,mm19,mm20],axis=1,join='inner')
print(d)
d.to_sql(name = 'mmm2010',con = con,if_exists = 'replace')

print("is done")
