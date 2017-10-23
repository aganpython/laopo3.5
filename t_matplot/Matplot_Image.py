# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

#image data
a = np.array([0.31,0.36,0.42,0.36,0.43,0.52,0.42,0.52,0.65]).reshape(3,3)
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
#plt.imshow(a,interpolation='nearest',cmap='bone',origin='lower')
plt.colorbar() #添加颜色标注
#plt.colorbar(shrink=0.9) #压缩标注高度
plt.xticks(())
plt.yticks(())
plt.show()