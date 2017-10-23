# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(99).reshape(11,9),index=list('abcdefghigk'),columns=list('ABCDEFGHI'))

print(data)
