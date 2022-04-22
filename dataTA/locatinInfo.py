# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:57:24 2022

@author: WINDOWS_X
"""

import pandas as pd # data processing
import numpy as np
#import sysmpy as sy
df = pd.read_csv("location_dataset.csv", usecols=['start','end','id_colums'],parse_dates = ['start','end'])
df = pd.DataFrame(df)
df['intercontact'] = df.groupby(['id_colums','start','end']).apply(lambda x:x['start'] - x['end'].shift(1))
df = df['intercontact']
print(df)
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
#df = pd.read_csv("locationInfo.csv", usecols=['area id'])
#df = pd.DataFrame(df)
#df = df.set_index(['start','id_colums'])

#def sumList(row):
#    return sum(listRow)
#s = [str (i) for i in df['area id']]
#res = str(" ".join(s))
#print(res)
#suml  = df['area id'].to_numpy()
#df["sum"] = sum(suml)
#df['area id'] = df['area id'].astype(str).astype(int)
#es = np.sum(df['area id'].iloc[1])
#print(res)
#df.to_csv('locationInfo.csv',       encoding='utf-8')