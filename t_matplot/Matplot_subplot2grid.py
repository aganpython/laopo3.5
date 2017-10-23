# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#分格显示 subplot2grid
# method 1: subplot2grid
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
ax3 = plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
ax5 = plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)

#3行，3列，从00原点开始，跨度3列，1行。

#method2: gridspec

#method3:easy to define structure

plt.tight_layout()
plt.show()
