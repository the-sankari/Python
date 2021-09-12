# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:55:49 2021

@author: Kajol Shutra Dhar
"""

#%%
"""
Problem 2_5:
"""
import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  
    i = 0
    while i < 10:
        print(random.randint(1,6))
        i = i + 1
    