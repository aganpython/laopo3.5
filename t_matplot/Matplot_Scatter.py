# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
#Scatter 散点图
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X) # for color value
plt.scatter(X,Y,s=75,c=T,alpha=0.5)
#plt.scatter(np.arange(5),np.arange(5))
plt.xlim(-1.5,1.5) #设置X范围
plt.ylim(-1,5,1,5) #设置Y范围
plt.xticks(()) #设置X ticks 空
plt.yticks(()) #设置X ticks 空
plt.show()