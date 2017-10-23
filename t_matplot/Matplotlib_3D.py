# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#3D 数据
fig = plt.figure() #定义一个窗口
ax = Axes3D(fig) # 把fig 加入到3D
#X,Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y =np.meshgrid(X,Y) #把 X,Y mesh到底面的面上。
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#rstride=1,cstride=1 代表行跨度，列跨度。
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
#zdir='z' 表示参考那个轴压下去,offset=-2表示压的坐标轴比0低2个坐标轴
ax.set_zlim(-2,2) #固定等高线图的高度
plt.show()