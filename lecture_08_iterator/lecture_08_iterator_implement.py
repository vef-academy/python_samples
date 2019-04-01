#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

###############################################################################
# Name        : lecture_08_iterator_implement.py
# Author      : 
# Version     :
# Copyright   : Your copyright notice
# Description : Implement our own iterators
###############################################################################

# Implement our 'iterable' object and 'iterator' object

class RangeDown:
    """ RangeDown class init range from stop to 0 """
    def __init__(self, _stop):
        self._stop = _stop
    
    def __iter__(self):
        return RangeDownIterator(self._stop)

class RangeDownIterator:
    """ RangeDownIterator class is iterator of RangeDown class """
    def __init__(self, _stop):
        self._cur = _stop

    def __next__(self):
        self._cur -= 1
        if self._cur < 0:
            raise StopIteration
        else:
            return self._cur

if __name__ == "__main__":
    myRange = RangeDown(5)
    # We could get our iterator by build-in func iter()
    itr = iter(myRange) 
    print(type(itr)) 

    # Or using for loop
    for i in myRange:
        print(i, end=' ')
