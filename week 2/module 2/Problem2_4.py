# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:00:50 2021

@author: Kajol Shutra Dhar
"""

#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    lis = []
    for num in range(0,10):
        randNum = random.random()
        randNum = randNum * 5 + 30
        lis.append(randNum)
    print(lis)
    