# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:18:39 2019

@author: BerkeAyevi
"""

def file2vector(x):
    y= open(x)
    b = y.read()
    z = b.split()
    t=[]
    for i in z:
        t.append(float(i))
    return t

def outer (x,y):
    z=[]
    v=len(x)
    v0=len(y)
    for i in range(v):
        a=[]
        for q in range(v0):
            a.append(float('{:.2f}'.format(x[i]*y[q])))
            z.append(a)
            
    return z

x0=file2vector("vector1.txt")
x1=file2vector("vector2.txt")

yp=outer(x0,x1) 

f = open("output.txt","w")

f.write(str(yp))

f.close()
