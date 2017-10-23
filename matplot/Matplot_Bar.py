# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
#Bar 柱状图
n = 12
X = np.arange(n)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
plt.bar(X,+Y1,facecolor='red',edgecolor='white')#设置X,Y显示，主颜色，边颜色
plt.bar(X,-Y2,facecolor='blue',edgecolor='white')
for x,y in zip(X,Y1):#zip 表示可以打包同时输出X,Y1,如果不用zip 只能一次输出一个
	plt.text(x+0.07,y+0.05,'%.2f'%y,ha='center',va='bottom')#添加注释，位置、保留几位小数
for x,y in zip(X,Y1):
	plt.text(x+0.07,-y-0.2,'-%.2f'%y,ha='center',va='top')


plt.xlim(-.5,n) #设置X范围
plt.ylim(-1.25,1.25) #设置Y范围
plt.xticks(()) #设置X ticks 空
plt.yticks(()) #设置X ticks 空
plt.show()