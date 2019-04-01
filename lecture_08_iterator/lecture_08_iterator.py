#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

###############################################################################
# Name        : lecture_08_iterator.py
# Author      : 
# Version     :
# Copyright   : Your copyright notice
# Description : Iterators
###############################################################################

# In python, we could get 'iterator' object from 'iterable' object by
#   iterable.__iter__() or iter(iterable) or for item in iterable loop
# We could get next item from 'iterator' object by
#   iterator.__next__() or next(iterator) or for item in iterable loop


# 1. Using iter() and next() built-in functions
lst = [0, 1, 2]
lst_itr = iter(lst)
print(type(lst_itr))  # <class 'list_iterator'>

print(next(lst_itr))
print(next(lst_itr))
print(next(lst_itr))
# print(next(lst_itr)) # Raise error StopIteration

# 2. Using __iter__() and __next__() member methods
lst_itr2 = [3, 4].__iter__()
print(lst_itr2.__next__())
print(lst_itr2.__next__())
# print(lst_itr2.__next__) # Raise error StopIteration

# 3. Using for loop
for item in [5, 6, 7]:
  print(item)
