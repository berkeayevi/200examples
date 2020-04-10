# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:06:09 2020

@author: dogru
"""
import matplotlib.pyplot as plt
import numpy as np
import math
pi=math.pi

n=float(input("Please write n: "))
x = np.arange(-6*pi,6*pi,n)
y=np.sin(x)/x
plt.plot(x,y)
plt.show()

    
