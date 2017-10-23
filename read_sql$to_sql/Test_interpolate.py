# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from xs1"
df = pd.read_sql(sql,con,index_col='id')
print(df)
b = df.interpolate()#使用插值法估计缺失值
print(b)
b.to_sql(name = 'xs' ,con = con,if_exists = 'replace')
print('is done')
