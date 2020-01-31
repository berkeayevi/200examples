# DATE       : 31/10/2019
# Author    : Berke Ayevi
# Version   : Python 3.6.6
# Description : scalar product.


import math

n = int(input("Number of n : "))

V1=[]
V2 =[]

if (n>0 and n <= 20):
    
    for z in range (0,n):
        a = math.cos ((math.pi*z)/16)

        b = math.sin((math.pi*z)/21)

        V1.append(a)
        V2.append(b)

    for t in range (0,n):
        
    
        a=0
        
        a = a+V1[t]* V2[t]
        
    print(a)
        
else:
    
    print("n must be positive")
    
    
    
    
    
    
    
    
    
    
