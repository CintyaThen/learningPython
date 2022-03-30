# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 15:41:19 2022

@author: WINDOWS_X
"""
import pandas as pd
from datetime import datetime, timedelta
df = pd.DataFrame({
    'weekstart':['01-Jan-18','08-Jan-18','15-Jan-18','22-Jan-18'],
    'weekend':['07-Jan-18','14-Jan-18','21-Jan-18','28-Jan-18'],
    'Spend':[34235.922,37359.6048,38916.1164,36903.8628],
    'Daily':[4890.846,5337.086,5559.445,5271.98],
})
print(df)

df2=pd.DataFrame(columns=['Date','Amount'])
df2['Date']=pd.to_datetime(df2['Date'])
#df2.reset_index(level=0,inplace=True)
print(df2)

for key,value in df.iterrows():
    #print(key,value)
    amount=value['Daily']
    for date in pd.date_range(value['weekstart'], value['weekend']):
        #print(date)
        df2=df2.append({"Date":date,"Amount":amount},ignore_index=True)

index=range(1,len(df2)+1) 

df2.set_index(pd.Index(index),'index',inplace=True)
df3=pd.DataFrame(columns=['mulai','akhir','spe','hariandes'])
print(df2)
 