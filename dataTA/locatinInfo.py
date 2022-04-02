# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:57:24 2022

@author: WINDOWS_X
"""

import pandas as pd # data processing
read_file = pd.read_csv('location_dataset.csv')
df = pd.DataFrame(read_file)
#temp1 = df['start'].min()
#temp2 = df['end'].max()
df1 =  df[["start","end"]]
df1['startNew'] = [pd.date_range(df1["start"].min(),df1["end"].max(), freq ='6H')]

print(df1)

