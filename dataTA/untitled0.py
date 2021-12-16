# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:10:13 2021

@author: WINDOWS_X
"""


import pandas as pd # data processing
import matplotlib.pyplot as plt # plotting
from scipy.stats import norm
import os 
for dirname, _, filenames in os.walk('D:/TA_185314080/learningPython/dataTA'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

var = pd.read_excel('normalisasi reality dan haggle.xlsx', 'Normalisasi reality', header=None, 
                    usecols="C", nrows=3438)
varNew = pd.DataFrame(var)
#var = pd.read_excel('normalisasi reality dan haggle.xlsx', 'Normalisasi reality')
#var = pd.DataFrame(index=list[3438],columns=['A','C'])
#var = pd.read_excel('normalisasi reality dan haggle.xlsx', skiprows=3440-3441)
var_mean = varNew.mean()
var_std = varNew.std()
print(var)
print(var_mean)
print(var_std)
""""
dist = norm(var_mean, var_std)
values = [value for value in range (0, 1)]
probabilities = [dist.pdf(value) for value in values]
"""


#pypplot.hist(normalisasi reality dan haggle.xlsx, bins=50)
#pypplot.show()

plt.hist(varNew, bins=100, density=(True))
#plt.plot()
plt.show()