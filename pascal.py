# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:03:32 2019

@author: BerkeAyevi
"""
def adder(L):
    a=[]
    a.append(L[0])
    y = len(L)
    for x in range (1, y):
        a.append(L[x]+L[x-1])
    a.append(L[-1])
    return a

n=int(input("write a number: "))
L=[1]

for i in range(n):
    print(L)
    y=[]
    y.append(adder(L))
    L = y[0]
    
    