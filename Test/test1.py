# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20130101',periods=6)
b = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(b)
