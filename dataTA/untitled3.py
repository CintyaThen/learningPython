# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:21:49 2022

@author: WINDOWS_X
"""

import pandas as pd
from datetime import datetime, timedelta



read_file = pd.read_csv('data_olah.csv')
df = pd.DataFrame(read_file)
#rint(df)

#f_list = [df["id_colums","cellTower"]]
#istCellTower = df["cellTower"].tolist()
#istPair = df["id_columns"].tolist()

"""for i,j in df.iterrows():
    print(i,j)
    print()"""
startTime = df["start"].min()
endTime = df["end"].max()
#rint(listCellTower)
def time_list(start, end):
start_time = datetime.strptime(start, '%Y-%m-%d %H:%M:%S.%f')
end_time = datetime.strptime(end, '%Y-%m-%d %H:%M:%S.%f')
#splitDates = pd.date_range(start, end, freq='6H')  
time_list = []
while start_time <= end_time:
    time_list.append(start_time.strftime('%Y-%m-%d %H:%M:%S.%f'))
    start += timedelta(hours=6)
    return time_list

startTime = df["start"].min()
endTime = df["end"].max()
times = time_list(startTime, endTime)
for time in times:
    print(time)

#print(splitDates)