# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#test5
data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
data = data.cumsum()
ax = data.plot.scatter(x='A',y='B',color='red',label='Class1')
data.plot.scatter(x='A',y='C',color='Green',label='Class2',ax=ax)
plt.show()
print(data)

#test4
#data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
#data = data.cumsum()
#data.plot.scatter(x='A',y='B',color='red',label='Class1')
#plt.show()
#print(data)

#test3
#data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
#data = data.cumsum()
#data.plot()
#plt.show()
#print(data)

#test2
#data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
#data.head()# 默认显示前5行，也可以写入数字定义显示几行
#data.plot()
#plt.show()
#print(data)

# test1
#data = pd.Series(np.random.randn(1000),index=np.arange(1000))
#data = data.cumsum() # 累加
#data.plot()#存数据
#plt.show()#显示数据
#print(data)