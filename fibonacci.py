# DATE       : 31/10/2019
# Author    : Berke Ayevi
# Version   : Python 3.6.6
# Description : Fibonacci numbers.



n = int (input("how much fibonacci number do you want: "))
a = 0
b = 1
x = 0
if (n > 0 ):
    if (n==1):

        print("1")

    elif(n==2):

        print("1,1")

    else:
        while (x<n):

            c = a + b

            a = b

            b = c

            print(c)

            x = x +1

        
else:
        print("number must be positive integer")
        
        
