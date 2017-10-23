# -*- coding: UTF-8 -*-
import pandas as pd
import pymysql
from sqlalchemy import create_engine
# 打开数据库连接
# python3:mysql+pymysql，python2:mysql+mysqldb
#con = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='laopo', charset='utf8')
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from test1"
df = pd.read_sql(sql,con,index_col="id")
# pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)[source]
print(df)
a = df.fillna(value=0)
print(a)
#a.to_sql(name = 'test2',con = con,if_exists = 'append')
a.to_sql(name = 'test1',con = con,if_exists = 'replace')
# DataFrame.to_sql(name, con, flavor=None, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)[source]
#if_exists : {‘fail’, ‘replace’, ‘append’}, default ‘fail’
#fail: If table exists, do nothing.
#replace: If table exists, drop it, recreate it, and insert data.
#append: If table exists, insert data. Create if does not exist.


print('is done')