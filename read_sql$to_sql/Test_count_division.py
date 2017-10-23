# -*- coding: UTF-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import random
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from test1"
df = pd.read_sql(sql,con,index_col='id')
# 得出每一列的数据类型
types = df.dtypes
# 选择具有浮点数据的那些列
float_columns = types[types.values == 'float64'].index
float_df = df[float_columns]  #所有的列
d = float_df.apply(lambda x: x/1000)
d.to_sql(name = 'mmm2004',con = con,if_exists = 'replace')
print("is done")