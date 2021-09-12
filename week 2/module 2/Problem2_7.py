# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:01:11 2021

@author: Kajol Shutra Dhar
"""

#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    sideA = float(input("Enter length of side one: "))
    sideB = float(input("Enter length of side two: "))
    sideC = float(input("Enter length of side three: "))
    s = 0.5 * (sideA + sideB + sideC)
    area = (s * ((s - sideA) * (s - sideB) * (s - sideC))) ** 0.5
    print("Area of a triangle with sides",sideA,sideB,sideC,"is", area)