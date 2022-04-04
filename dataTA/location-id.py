# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:40:53 2022

@author: WINDOWS_X
"""
import pandas as pd # data processing
"""read_file = pd.read_excel('location_dataset.xlsx')

#df.replace(11,104)
#n = len(df['area id'].unique())
read_file.to_csv("location_dataset.csv", index=None, header=True)
df = pd.DataFrame(pd.read_csv("location_dataset.csv"))

print(df)
#temp = df.replace({'area id':{35783:74, 5193:75, 32028:76, 20036:77, 29301:78, 29302:103}})
#df.insert(1,"location",True)

#temp.to_csv('location.csv', index=False, encoding='utf-8')
#print(temp['area id'].unique())


read_file = pd.read_csv('location.csv')
df = pd.DataFrame(read_file)
print(df['area id'].unique())"""

from random import randint

time = pd.to_datetime( ['2016-01-01 00:00:00', '2016-01-01 05:00:00', 
                        '2016-01-01 10:00:00', '2016-01-02 01:00:00', 
                        '2016-01-02 04:00:00', '2016-01-01 02:00:00', 
                        '2016-01-01 08:00:00', '2016-01-01 14:00:00',
                        '2016-01-02 03:00:00' ]
                      )

id_1 = [1] * 5
id_2 = [2] * 4

lists = [0] * 9
for i in range(9):
    l = [randint(0,10)  for _ in range(randint(1,5) ) ]
    l = list(set(l))
    lists[i] = l

data = {'timestamp': time, 'id': id_1 + id_2, 'lists': lists}
example = pd.DataFrame(data=data)
#a = [list(set(l)) for l in example.lists]
#example.loc[:,'lists'] = a
example.set_index('timestamp').groupby('id').lists.resample('D').sum()

print(example)