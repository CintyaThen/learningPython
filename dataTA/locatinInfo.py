# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:57:24 2022

@author: WINDOWS_X
"""

import pandas as pd # data processing
#import sysmpy as sy
"""
Slice data and list of area id
df = pd.read_csv("location_dataset.csv",usecols=['start','area id','id_colums'],
                                                 index_col='start', parse_dates=True)

df = pd.DataFrame(df)
#df.set_index(keys = ["start", "id_colums"])
df = df.groupby([df.index.floor("6H"), "id_colums"]).agg({'area id': lambda x: list(set(x))})
#print(df)

"""
"""
df = df.groupby([df.index.floor("6H"), "id_colums"]).agg({'area id': lambda x: list(x)})

df = pd.read_csv("locationInfo.csv")
df = pd.DataFrame(df)

print(df.head())"""
df = pd.read_csv("locationInfo.csv")
df = pd.DataFrame(df)
df = df.set_index(['start','id_colums'])



#print(df)
df.to_csv('locationInfo.csv',  encoding='utf-8')