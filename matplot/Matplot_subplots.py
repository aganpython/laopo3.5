# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

#分格显示 subplots
#method3:easy to define structure
f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])
ax12.bar([1,2],[1,2])

plt.tight_layout()
plt.show()

