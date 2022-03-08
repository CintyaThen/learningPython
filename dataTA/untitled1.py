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

read_file = pd.read_table('reality-mining-proximity.csv') #read csv file
df = pd.DataFrame(read_file) # read csv to dataframe
df['start'] = df['start'].astype('datetime64[ns]') # change start type from object to datetime
df['end'] = df['end'].astype('datetime64[ns]') # change end type from object to datetime

#df.insert(5, "interval", True)
#df["interval"] = df["end"] - df["start"]

df.to_csv('proximity-data_asli.csv', index=False, encoding='utf-8')



print(df)
#df['start'] = pd.to_datetime(df['start'], format())
#print(df['start'])
#print(list(df.columns))
#desc = df["start"].describe()
#desc = df["id1"].describe()
#print(desc)
print(df["interval"].isna().sum())
#print(df.info())








#df.head()
#print(df.to_string())

#row_labels = [']
#df.index = row_labels

#x1 = df.brics.loc["Mean"]
#print(x1)
#airwise_dists = squareform(pdist(df, 'euclidean'))
# =
# = scip.exp(-pairwise_dists ** 2 / s ** 2)