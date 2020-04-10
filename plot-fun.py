# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:24:44 2020

@author: dogru
"""
import matplotlib.pyplot as plt

f=open("fun.txt")
lines=f.readlines()
q=[]
for i in lines:
    s=i.split()
    q.append(s)
    
y=[]
x=[]
for i in range(len(q)):
    c=q[i][1]
    z=q[i][0]
    y.append(c)
    x.append(z)
    
plt.plot(x,y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()