# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymysql

con = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='laopo', charset='utf8')
sql = "SELECT * FROM test"
df = pd.read_sql(sql,con,index_col=["id","city"])
x = df.fillna(value=1)
y = 2*x +1
y = x**2
plt.plot(x,y)
plt.show()
print(x)

