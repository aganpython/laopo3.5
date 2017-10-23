# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
fp="e:/shangquan1.xlsx"
data=pd.read_excel(fp,index_col=None,header=None,encoding='utf8')
print(data)
#data = (data - data.min())/(data.max() - data.min())
m,n=data.shape
#第一步读取文件，如果未标准化，则标准化
data=data.as_matrix(columns=None)
#print(data)
#将dataframe格式转化为matrix格式
k=1/np.log(m)
#print(k)
yij=data.sum(axis=0)
#print(yij)
pij=data/yij
#print(pij)
#第二步，计算pij
test=pij*np.log(pij)
test=np.nan_to_num(test)
ej=-k*(test.sum(axis=0))
#计算每种指标的信息熵
wi=(1-ej)/np.sum(1-ej)
print(wi)
#计算每种指标的权重