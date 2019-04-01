#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

###############################################################################
# Name        : lecture_02_operator_overloading.py
# Author      : 
# Version     :
# Copyright   : Your copyright notice
# Description : Operator Overloading Example in python
###############################################################################

# Python supports operators overloading (like C++)
# via overriding the corresponding magic functions.
# Example: Find magic function in int class
# >> dir(int)   # list all atribute and method in int class


class Point:
    """ Class Point """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "point({},{})".format(self.x, self.y)

    def __eq__(self, right):
        """ Overload operator == """
        if (self.__class__.__name__ == right.__class__.__name__):
            return (self.x == right.x and self.y == right.y)
        raise TypeError("Not a 'cicle object'")
    
    def __add__(self, right):
        """ Overload operator + """
        if (self.__class__.__name__ == right.__class__.__name__):
            return Point(self.x + right.x, self.y + right.y)
        raise TypeError("Not a 'cicle object'")

if __name__ == '__main__':
    # Test point class
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    p3 = Point(1, 2)
    print(p1 == p2)    # False
    print(p1 == p3)    # true
    print(p1 + p2)     # (4, 6)
