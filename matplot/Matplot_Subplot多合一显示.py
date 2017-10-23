# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
#Subplot 多合一显示
plt.figure()

plt.subplot(2,2,1) #两行两列第一个位置
plt.plot([0,1],[0,1])
plt.subplot(2,2,2)
plt.plot([0,1],[0,2])
plt.subplot(2,2,3)
plt.plot([0,1],[0,3])
plt.subplot(2,2,4)
plt.plot([0,1],[0,4])
plt.show()