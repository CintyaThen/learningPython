# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:40:53 2022

@author: WINDOWS_X
"""
import pandas as pd # data processing
read_file = pd.read_excel('location_dataset.xlsx')

#df.replace(11,104)
#n = len(df['area id'].unique())
read_file.to_csv("location_dataset.csv", index=None, header=True)
df = pd.DataFrame(pd.read_csv("location_dataset.csv"))
print(df)
#temp = df.replace({'area id':{35783:74, 5193:75, 32028:76, 20036:77, 29301:78, 29302:103}})
#df.insert(1,"location",True)

#temp.to_csv('location.csv', index=False, encoding='utf-8')
#print(temp['area id'].unique())


"""read_file = pd.read_csv('location.csv')
df = pd.DataFrame(read_file)
print(df['area id'].unique())"""