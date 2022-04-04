# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:57:24 2022

@author: WINDOWS_X
"""

import pandas as pd # data processing
#import dateutil
df = pd.read_csv("location_dataset.csv",usecols=['start','area id','id_colums'], parse_dates=['start'])
agregated = df.agg({'area id': list})
grouped = df.set_index('start').groupby('start').resample('6H').sum()

#df2 = df.set_index(pd.DatetimeIndex(df["start"])).drop("start", axis=1)
#df = df.set_index('start').resample('6H').agg({'area id': list}).sum()
#df = df.groupby([pd.Grouper( "id_colums"]).agg({'area id': list}).sum()
#df.groupby(pd)
#dfg = df.
#df = df2.set_index('start')
#df = df.groupby('id_colums').agg({'area id': list})
#df2 = dfg.resample('6H').sum()
print(grouped)
"""agregated = df.agg({'area id': list})
grouped = df.set_index('start').groupby('id_colums').resample('6H').sum()
grouped.to_csv('locationInfo.csv',  encoding='utf-8')"""








"""read_file = pd.read_csv('location_dataset.csv', usecols=['start','area id','id_colums'])
time = 
df = pd.DataFrame(data=read_file)
#df = df.set_index(pd.DatetimeIndex(df['start']))
a = [list(set(l)) for l in df['id_colums']]
df.loc[:,'id_colums'] = a

df = df.set_index('start').groupby('area id').a.resample('6H').sum()
df = df.reset_index('id').reset_index()
print(df)

df1 =  pd.DataFrame(columns=['startNew', 'endNew'])
df1['startNew']= pd.to_datetime(df1['startNew'])
df1['endNew']= pd.to_datetime(df1['endNew'])

for key, value in df.iterrows():
    print(key, value)
    startNew = value['start']
    for date in pd.date_range(df['start'].min(), df['end'].max()):
        df2"""


#temp1 = df['start'].min()
#temp2 = df['end'].max()
#ind = pd.date_range(df["start"].min(), df["end"].max(), freq ='6H')
#df = df.set_index(ind)
#df.resample('W').sum()
#