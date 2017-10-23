# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#Contours 等高线图
def f(x,y):
	# the height function
	return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y) #把x,y绑定成网格的输入值。
# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)#把颜色放入到等高线上。cmap--每一个值对应一个有颜色的点。
# use plt.contour to add contour lines
# 8代表把等高给分成10部分，0代表分成2部分。
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
#adding label
plt.clabel(C,inline=True,fontsize=10)
#plt.clabel(C,inline=False,fontsize=10)
plt.xticks(())
plt.yticks(())
plt.show()
