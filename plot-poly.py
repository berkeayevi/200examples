# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 17:10:35 2020

@author: BerkeAyevi
"""

import random 
import matplotlib.pyplot as plt
import numpy as np

n= int(input("give input"))

yvalues =[]
xvalues=[]
def generator(x,n):
    c =random.random()
    a= c*(x**n)
    return a

for i in range(0,n):
    for j in np.linspace(-2,2,100):
        a = generator(j,n)
        yvalues.append(a)
        xvalues.append(j)
        
    
    
plt.plot(xvalues,yvalues)
plt.show()    
