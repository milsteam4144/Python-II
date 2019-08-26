"""
Created on Sat Nov 10 11:26:33 2018

@author: Mallory
"""
from newArrayClass import Array

#This is to test the size() method
a = Array(10)

a[1] = 1

a[8] = 1

print(a.size())
#The logical size should be 9


b = Array(5)

b[2] = 45
b[4] = 45



#The logical size should be 5

print(b.size())

