# -*- coding: UTF-8 -*-
import pandas as pd
import pymysql
from sqlalchemy import create_engine
# 打开数据库连接
# python3:mysql+pymysql，python2:mysql+mysqldb
#con = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='laopo', charset='utf8')
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
sql = "select * from test"
df = pd.read_sql(sql,con,index_col="id")
# pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)[source]
print(df)