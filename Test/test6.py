import numpy as np
import pandas as pd

fp = "e:/shangquan.xlsx"
data = pd.read_excel(fp, skiprows=[0], index_col=None, header=None, encoding='utf8')  #
# data = (data - data.min())/(data.max() - data.min())
data = data.drop([data.columns[0]], axis=1, inplace=False)
# print(data)
m, n = data.shape  # m,n为行和列
# 第一步读取文件，如果未标准化，则标准化
data1 = data.as_matrix(columns=None)
# print(data)#ndarray,数组
# 将dataframe格式转化为matrix格式
k = 1 / np.log(m)
yij = data1.sum(axis=0)
pij = data1 / yij
# 第二步，计算pij
test = pij * np.log(pij)
test = np.nan_to_num(test)
ej = -k * (test.sum(axis=0))
# 计算每种指标的信息熵
wi = (1 - ej) / np.sum(1 - ej)
# 计算每种指标的权重
print(wi)
print(wi.dtype)
a = wi.tolist()
# print(a)
print(a[0])

b = data
#print(b)
#print(b.iloc[0, 0])
for i in range(9):
	for j in range(11):
		b.iloc[j, i] = a[i] * b.iloc[j, i]
print(b)
c = data.sum(axis=1)
print(c)


