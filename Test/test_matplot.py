# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#test5 tick 能见度
x = np.linspace(-3,3,50)
y = 0.1*x
plt.figure()
plt.plot(x,y,linewidth=10)
plt.ylim(-2,2)
ax = plt.gca()

plt.show()

#test4 Annotation 标注
#x = np.linspace(-3,3,50)
#y = 2*x + 1

#plt.figure(num=1,figsize=(8,5)) # figure 定义大小 num 图表的数字 代表整个图
#plt.plot(x,y)
#x0 = 1
#y0 = 2*x0 + 1
#plt.scatter(x0,y0,s=50,color='b')
#plt.plot([x0,x0],[y0,0],'k--',lw=2.5)
# method 1
#plt.annotate(r'$2x+1=%s$'% y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
#			 fontsize=36,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))#注释、位置、偏yi、字体大小
# method 2
#plt.text(-3.7,3,r'$this is annotation$',fontdict={'size':36,'color':'r'}) #位置、注释、字体大小、颜色
#ax = plt.gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_positon(('data',0))

plt.show()

#test3 legend()#显示图例
#x = np.linspace(-3,3,50)
#y1 = 2*x + 1
#y2 = x**2
#plt.figure(num=3,figsize=(8,5)) # figure 定义大小 num 图表的数字 代表整个图
#l1, = plt.plot(x,y2,label='up')
#l2, = plt.plot(x,y1,color='red',linewidth=5.0,linestyle='--',label='down')#颜色、线宽、样式
#plt.legend()#显示图例 label 设置名字,best 位置最佳，会自动调整
#plt.legend(handles=[l1,l2,],labels=['aaa','bbb'],loc='best')
#plt.xlim(-1,2)#X轴取值范围
#plt.ylim(-2,3)#Y轴取值范围
#plt.xlabel("this is X")#X轴标签名称lplt.ylabel("this is Y")#Y轴标签名称
#new_ticks = np.linspace(-1,2,5)
#print(new_ticks)
#plt.xticks(new_ticks) # 更改下标，赋予新的有特性的下标
#plt.yticks([-2,-1.8,-1,1.22,3],['really bad','bad','normal','good','really good'])# 更改下标，赋予新的有特性的下标
#plt.show()

#test2
#x = np.linspace(-3,3,50)
#y1 = 2*x + 1
#y2 = x**2
#plt.figure(num=3,figsize=(8,5)) # figure 定义大小 num 图表的数字 代表整个图
#plt.plot(x,y2)
#plt.plot(x,y1,color='red',linewidth=5.0,linestyle='--')#颜色、线宽、样式
#plt.xlim(-1,2)#X轴取值范围
#plt.ylim(-2,3)#Y轴取值范围
#plt.xlabel("this is X")#X轴标签名称lplt.ylabel("this is Y")#Y轴标签名称
#new_ticks = np.linspace(-1,2,5)
#print(new_ticks)
#plt.xticks(new_ticks) # 更改下标，赋予新的有特性的下标
#plt.yticks([-2,-1.8,-1,1.22,3],['really bad','bad','normal','good','really good'])# 更改下标，赋予新的有特性的下标
#plt.show()

#test1
# x = np.linspace(-1,1,50)
# y = 2*x +1
# y = x**2
# plt.plot(x,y)
#print(y)
#plt.show()
