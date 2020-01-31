# DATE       : 07/11/2019
# Author    : Berke Ayevi
# Version   : Python 3.6.8
# Description : integral.py

import math
x0 = 2
x1 = 3
n = int(input("resolution: "))


a = (x1-x0)/float(n)
b = 0.5*(math.log(x0) + math.log(x1))

for i in range (1,n):
    b = b + math.log((x0 + i*a))

g = a*b

print(g)

