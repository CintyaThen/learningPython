# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:53:43 2022

@author: WINDOWS_X
"""

import pandas as pd # data processing
import matplotlib.pyplot as plt # plotting
from scipy.spatial.distance import pdist, squareform
import os 
"""for dirname, _, filenames in os.walk('D:/TA_185314080/learningPython/dataTA'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
x = pd.read_csv("D:/TA_185314080/learningPython/dataTA\DATA TA_Bag1Lengkap.csv")
x.head()"""
df = pd.read_csv('DATA TA_Bag1Lengkap.csv')
#print(df.to_string())
print(df)
row_labels = ['Mean', 'Variance']
df.index = row_labels
print(df)
#x1 = df.brics.loc["Mean"]
#print(x1)
#airwise_dists = squareform(pdist(df, 'euclidean'))
# =
# = scip.exp(-pairwise_dists ** 2 / s ** 2)