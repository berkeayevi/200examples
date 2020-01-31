# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:10:21 2019

@author: BerkeAyevi
"""

import math

pi= math.pi

def degree2rad(x):
    
    a = (x* pi)/180
    return a

c =[]
for i in range (0,46):
    
    a =math.sin(degree2rad(i))
    c.append(a)
d=[]
for i in range (0,46):
    d.append(i)
fid= open("output.txt","w")
for i in range(0,46):
    fid.write(str(d[i]))
    fid.write("      ")
    fid.write(str(c[i]))
    fid.write("\n")
    
fid.close()
    
    