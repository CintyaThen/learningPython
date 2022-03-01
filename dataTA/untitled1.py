# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:53:43 2022

@author: WINDOWS_X
"""

import pandas as pd # data processing
import datetime as dt # datetime module
import matplotlib.pyplot as plt # plotting
from scipy.spatial.distance import pdist, squareform
import os 
"""for dirname, _, filenames in os.walk('D:/TA_185314080/learningPython/dataTA'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
x = pd.read_csv("reality-mining-proximity.csv")
x.head()"""
read_file = pd.read_table('reality-mining-proximity.csv')
df = pd.DataFrame(read_file)
print(df)
#df['start'] = pd.to_datetime(df['start'], format())
#print(df['start'])
#print(list(df.columns))
#desc = df["start"].describe()
#desc = df["id1"].describe()
#print(desc)

print(df.info())








#df.head()
#print(df.to_string())

#row_labels = [']
#df.index = row_labels

#x1 = df.brics.loc["Mean"]
#print(x1)
#airwise_dists = squareform(pdist(df, 'euclidean'))
# =
# = scip.exp(-pairwise_dists ** 2 / s ** 2)