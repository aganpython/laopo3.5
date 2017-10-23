# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
con = create_engine("mysql+pymysql://root:root@localhost:3306/laopo?charset=utf8")
fp="e:/testdata/2004data.xls"
#读取数据，并删除行头和列头，如果未标准化，则标准化
#data=pd.read_excel(fp,skiprows=[0],index_col=None,header=None,encoding='utf8')#
data = pd.read_excel(fp, index_col=0, encoding='utf8') #此法不用去掉第一列第一行
#data = data.drop([data.columns[0]], axis=1, inplace=False)
data = (data - data.min())/(data.max() - data.min())*10
#print(data)
m,n=data.shape#m,n为行和列
#print(data)#ndarray,数组
#将dataframe格式转化为matrix格式
data1=data.as_matrix(columns=None)
#第二步，计算pij
k=1/np.log(m)
yij=data1.sum(axis=0)
pij=data1/yij
#计算每种指标的信息熵
test=pij*np.log(pij)
test=np.nan_to_num(test)
ej=-k*(test.sum(axis=0))
#计算每种指标的权重
wi=(1-ej)/np.sum(1-ej)
#print(wi)
#print(wi.dtype)
a = wi.tolist()
print(a)
#对各个城市进行评分，先计算每个城市的每种指标，乘以每种指标的权重
b = data
print(b)
for i in range(len(a)):
	for j in range(len(b)):
		b.iloc[j, i] = a[i] * b.iloc[j, i]
print(b)
#把各个城市的分数合并
#axis=0)#计算每一列（二维数组中类似于矩阵的列）的和。竖着计算,a.sum(axis=1)#计算每一行的和。横着计算.
c = data.sum(axis=1)
#print(c)
a = pd.DataFrame(a,columns=list('w'))
c = pd.DataFrame(c,columns=list('k'))
g = pd.merge(b,c,how='left',left_index=True,right_index=True)
a.to_sql(name = 'test99',con = con,if_exists = 'replace')#把各指标权重写入到数据库
# b.to_sql(name = 'testb',con = con,if_exists = 'replace')#把各个城市的评分写入到数据库
c.to_sql(name = 't66',con = con,if_exists = 'replace')#把各个城市的总分写入到数据库
#g.to_sql(name = 'testg',con = con,if_exists = 'replace')#把各个城市的评分+总分写入到数据库
#print(d)
print("is done")



