# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:57:48 2021

@author: Kajol Shutra Dhar
"""

#%%
import random

def problem2_6():
  
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    for roll in range(0,100):
        firstDice = (random.randint(1,6))
        secondDice = (random.randint(1,6))
        print(firstDice + secondDice)
        