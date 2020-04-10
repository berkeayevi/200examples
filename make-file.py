# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:42:56 2020

@author: dogru
"""

n=int(input("Please write n: "))
f=open("data.txt","w")

for i in range(n):
    x=i*1.0/n
    y=x**2
    z=x**3
    f.write("{0:9.3f} ,{1:9.3f} ,{2:9.3f} /n".format(x,y,z))
    
    
f.close    
    