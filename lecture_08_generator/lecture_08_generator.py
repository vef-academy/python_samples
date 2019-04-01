#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

###############################################################################
# Name        : lecture_08_generator.py
# Author      :
# Version     :
# Copyright   : Your copyright notice
# Description : Generator
###############################################################################

# Generators are iterators, but you can only iterate over them once
# It don't store all values in memory, they generate the values on the fly
# For more info how yield works:
#   https://pythontips.com/2013/09/29/the-python-yield-keyword-explained/

def RangeDown(stop):
    """ A generator function contain yield statement, generate number 
    from stop to 0 """
    cur = stop-1
    while cur >= 0:
        yield cur   # produce result each time function run
        cur -= 1

if __name__ == "__main__":
    myRange = RangeDown(5)

    for i in myRange:
        print (i)

    # Second time for loop didn't work with myRange 
    # for i in myRange:   
    #     print(i)

