# DATE       : 17/10/2019
# Author    : Berke Ayevi
# Version   : Python 3.6.6
# Description : Convert a byte (8 bits) into a decimal number.


script = [1,1,0,0,0,1,0,1]

resut= ((2**0)* script[7])+ ((2**1)* script[6])+ ((2**2)* script[5])+ ((2**3)* script[4])+ ((2**4)* script[3])+ ((2**5)* script[2])+ ((2**6)* script[1]) +((2**7)* script[0])

print(resut)
