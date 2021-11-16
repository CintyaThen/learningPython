# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
2
import numpy as np # linear algebra
import pandas as pd # data processing


import os
for dirname, _, filenames in os.walk('D:/TA_185314080/learningPython/titanic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
train_data = pd.read_csv("D:/TA_185314080/learningPython/titanic/train.csv");
train_data.head()

test_data = pd.read_csv("D:/TA_185314080/learningPython/titanic/test.csv")
test_data.head()
test_data = pd.read_csv("D:/TA_185314080/learningPython/titanic/test.csv")
test_data.head()
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)
men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)