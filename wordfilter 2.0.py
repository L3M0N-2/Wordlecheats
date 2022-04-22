#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:38:17 2022

@author: lemoneucalyptus
"""

import pandas as pd 
words = pd.read_csv('wordbank.csv') 

i = 1
while i == 1:
    guess=list(input('what is the word you tested?').lower())
    color=list(input('what color are the corresponding places (0 for grey, 1 for yellow, 2 for green'))
    
    for j in range(0,len(color)):
        letter=guess[j]
        place=j+1
        if color[j] == '0':
            for ind in range (1,6):  
                words=words[words.iloc[:,ind] != letter] 
                ind += 1
        elif color[j] == '1':
            words = words[(words ==letter).any(axis=1)]      
            words=words[words.iloc[:,place] != letter]
        elif color[j] == '2':
            words = words[(words ==letter).any(axis=1)]      
            words = words[words.iloc[:,place] == letter] 
        j+=1
    
    print(words)
    print('you have a total of ',len(words.index),'remaining options')
    
    stop = input("did you finish the game?(Y for yes))").lower()
    if stop == 'y':
        print('Thank you for using!')
        break
    else:
        continue