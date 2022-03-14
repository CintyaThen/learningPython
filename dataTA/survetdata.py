# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd 
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#import Dataset
def importdata():
    balance_data = pd.read_file("reality-mining-survey.txt")
    
    #printing Dataset Shape
    print ("Dataset length: ", len(balance_data))
    print ("Dataset Shape: ", balance_data.shape)
    
    #printing Dataset observations
    print("Dataset: ", balance_data.head())
    return balance_data

#Function split dataset
#def splitDataset(balance_data):
    
    #separating the target variable
   # X = balance_data.values[:, 1:5]
  #  Y = balance_data.values[:, 0]
    
    #Splitting the Dataset into train and test
 #   x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size)*/

def main():
    data = importdata()
    
if __name__ =="__main__":
    main()
    