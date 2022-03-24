# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:05:24 2022

@author: WINDOWS_X
"""

# generate a sample time series
import pandas as pd
from datetime import datetime, timedelta



read_file = pd.read_csv('data_olah.csv')
df = pd.DataFrame(read_file)

#ind = pd.date_range(df["start"].min(), df["end"].max(), freq ='6H')
#my_timelist = [pd.date_range(df["start"].min(),df["end"].max(), freq ='6H')]
#df['id_column'] = df[df.columns[3:4]].apply(lambda x:','.join(x.dropna()),axis=1)
#print(my_timelist)
#df["id_colums"] = df["id1"].astype(str)+','+df["id2"].astype(str)
print(df.info())
print(df)


"""#df = df.sort_values(by="start")

#min_datetime = df.["start"].
#print(df["interval"].isna().sum())
date1 = df["start"].min()
date2 = df["end"].max()
start = datetime(date1)
end = datetime(date2)
interval = end - start
print(df["start"].info())
#print(interval)"""
#sortData = df[["start","end","cellTower", "id_colums"]]
#sortData.to_csv('data_olah.csv',  encoding='utf-8', index=False)

"""s = pd.Series(["A", "B", "C", "D", "E"], index=pd.date_range("2000-01-01", periods=5, freq="6h"))
print(s)

# these two indices should access the same value ("C")
integer_index = 2
# Converts the string into a datetime object
date_index = datetime.strptime("2000-01-02 00:00", "%Y-%m-%d %H:%M")
print(date_index) # 2000-01-02 00:00:00q"""

#print(s[integer_index])  # prints "C"
#print(s[date_index])  # prints "C"


#print(s[integer_index - 2])  # prints "A"

"""one_day = timedelta(days=1)
print(s[date_index - one_day]) # prints "A"
print(date_index - one_day) # 2000-01-01 00:00:00"""

"""date_1 = '19/7/2004 06:00:0.0'
date_2 = '22/6/2005 18:00:0.0'
date_format_str = '%d/%m/%Y %H:%M:%S.%f'
start = datetime.strptime(date_1, date_format_str)
end =   datetime.strptime(date_2, date_format_str)
# Get interval between two timstamps as timedelta object
diff = end - start
# Get interval between two timstamps in hours
diff_in_hours = diff.total_seconds() / 3600
print('Difference between two datetimes in hours:')
print(diff_in_hours)"""

#ind = pd.date_range('19-7-2004 6:00:00.0', periods = 1355, freq ='6H')

#print(ind)