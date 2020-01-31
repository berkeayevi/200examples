# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:34:17 2019

@author: BerkeAyevi
"""
def reverse(n):
    if prime(n) == False: 
        return False 
    else:
        print("n is prime:",n)
        r = 0
        while n != 0: 
            d = n % 10
            r = r * 10 + d 
            n = int(n / 10)
        print("reverse is: ",r)
        return prime(r) 

def prime(n):
    for x in range(2, n): 
        if n % x == 0:
            return False      
    return True
n = int(input("give input: "))  
if reverse(n): 
    print("Prime too") 
else: 
    print("Not prime") 