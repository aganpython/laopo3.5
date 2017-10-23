# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#分格显示 gridspec
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
ax2 = plt.subplot(gs[1,:2])
ax3 = plt.subplot(gs[1:,2])
ax4 = plt.subplot(gs[-1,0])
ax5 = plt.subplot(gs[-1,-2])

#method3:easy to define structure

plt.tight_layout()
plt.show()

