# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 00:04:02 2021

@author: CintyaThen
"""
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # character, including spaces and commas!
    for letter in "hoho": 
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
