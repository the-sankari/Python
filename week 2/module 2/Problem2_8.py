# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:02:58 2021

@author: Kajol Shutra Dhar
"""

#%%
hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
#%%
def problem2_8(temp_list):
    sum_ = 0
    for temp in temp_list:
        sum_ = sum_ + temp
        temp = temp - 1
        average = sum_ / len(temp_list)
    print("Average:",average)
    print("High:", max(temp_list))
    print("Low:", min(temp_list))