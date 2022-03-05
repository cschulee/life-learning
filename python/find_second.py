#!/usr/bin/env python

#find_second.py arg1 arg2
#prints the index of the 2nd instance of arg2
#found within arg1

import sys

def find_second(a,b):
    x = a.find(b) #first instance
    return a.find(b,x+1) #second instance

print find_second(str(sys.argv[1]),str(sys.argv[2]))
