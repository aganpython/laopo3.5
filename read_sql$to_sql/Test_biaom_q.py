# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from q2014"
df = pd.read_sql(sql,con,index_col='id')
# 得出每一列的数据类型
types = df.dtypes
# 选择具有浮点数据的那些列
float_columns = types[types.values == 'float64'].index

q1 = df.ix[:,['q1']]
q2 = df.ix[:,['q2']]
q3 = df.ix[:,['q3']]
q4 = df.ix[:,['q4']]
q5 = df.ix[:,['q5']]
q6 = df.ix[:,['q6']]
q7 = df.ix[:,['q7']]
q8 = df.ix[:,['q8']]
q9 = df.ix[:,['q9']]
q10 = df.ix[:,['q10']]
q11 = df.ix[:,['q11']]
q12 = df.ix[:,['q12']]
q13 = df.ix[:,['q13']]
q14 = df.ix[:,['q14']]
q15 = df.ix[:,['q15']]
q16 = df.ix[:,['q16']]
q17 = df.ix[:,['q17']]
q18 = df.ix[:,['q18']]
q19 = df.ix[:,['q19']]
q20 = df.ix[:,['q20']]
q21 = df.ix[:,['q21']]
q22 = df.ix[:,['q22']]
q23 = df.ix[:,['q23']]
q24 = df.ix[:,['q24']]
q25 = df.ix[:,['q25']]
q26 = df.ix[:,['q26']]
q27 = df.ix[:,['q27']]
q28 = df.ix[:,['q28']]
q29 = df.ix[:,['q29']]
q30 = df.ix[:,['q30']]

#将整列的值都分别乘
qq1 = q1.apply(lambda x: x*10000*1000*0.7143)
qq2 = q2.apply(lambda x: x*10000*1000*0.9)
qq3 = q3.apply(lambda x: x*10000*1000*0.2857)
qq4 = q4.apply(lambda x: x*10000*1000*0.2857)
qq5 = q5.apply(lambda x: x*10000*1000*0.2857)
qq6 = q6.apply(lambda x: x*10000*1000*0.9714)
qq7 = q7.apply(lambda x: x*100000000*0.5714)
qq8 = q8.apply(lambda x: x*100000000*1.286/10000)
qq9 = q9.apply(lambda x: x*100000000*2.714/10000)
qq10 = q10.apply(lambda x: x*100000000)
qq11 = q11.apply(lambda x: x*10000*1000*1.4571)
qq12 = q12.apply(lambda x: x*10000*1000*1.4286)
qq13 = q13.apply(lambda x: x*10000*1000*1.7143)
qq14 = q14.apply(lambda x: x*10000*1000*1.5714)
qq15 = q15.apply(lambda x: x*10000*1000*1.4571)
qq16 = q16.apply(lambda x: x*10000*1000*1.4571)
qq17 = q17.apply(lambda x: x*10000*1000*1.5)
qq18 = q18.apply(lambda x: x*10000*1000*1.4143)
qq19 = q19.apply(lambda x: x*10000*1000*1.3648)
qq20 = q20.apply(lambda x: x*10000*1000*1.4672)
qq21 = q21.apply(lambda x: x*10000*1000*1.3307)
qq22 = q22.apply(lambda x: x*10000*1000*1.0918)
qq23 = q23.apply(lambda x: x*10000*1000*1.7143)
qq24 = q24.apply(lambda x: x*10000*1000*1.5714)
qq25 = q25.apply(lambda x: x*10000*1000*1.1429)
qq26 = q26.apply(lambda x: x*100000000*1.33)
qq27 = q27.apply(lambda x: x*10000*1000*1.7572)
qq28 = q28.apply(lambda x: x*0.03412/1000)
qq29 = q29.apply(lambda x: x*100000000*0.1229)
qq30 = q30.apply(lambda x: x*10000*1000*1)
d = pd.concat([qq1,qq2,qq3,qq4,qq5,qq6,qq7,qq8,qq9,qq10,qq11,qq12,qq13,qq14,qq15,qq16,qq17,qq18,qq19,qq20,qq21,qq22,qq23,qq24,qq25,qq26,qq27,qq28,qq29,qq30],axis=1,join='inner')
#print(d)
d.to_sql(name = 'qq2014',con = con,if_exists = 'replace')
print(d)
print("is done")
