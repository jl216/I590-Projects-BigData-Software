'''
Created on Jan 18, 2016

@author: jwlee
'''

import sys

def fizzbuzz(a):
    for i in range(1,a+1):
        if i % 2 == 0 and i % 3 == 0:
            print ("fizzbuzz")
        elif i % 2 == 0:
            print ("fizz")
        elif i % 3 == 0:
            print ("buzz")
        else:
            print (i)

if len(sys.argv) > 1:
    input_number = int(sys.argv[1])
    fizzbuzz(input_number)