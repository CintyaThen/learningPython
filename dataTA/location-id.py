# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:40:53 2022

@author: WINDOWS_X
"""
import pandas as pd # data processing
read_file = pd.read_csv('areaid.csv')
df = pd.DataFrame(read_file)
df.insert(1,"location",True)
print(df)