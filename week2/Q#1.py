# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:52:36 2019

@author: ORCAS_ISLAM
"""
# Define a class named Shape and its subclasses Square and Circle. Each shape will have a method of area and a method of perimeter (default value of both is 0).
#The Square class has an init function which takes a length as an argument
#The Circle class has an init function which takes a radius as an argument
#Add also a representation method for each shape.
#Don’t forget to use private variables where needed, and use inheritance and overriding where needed!

import math
class Shape(object):
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Square(Shape):
    def __init__(self , length):
        self.__length=length
    def setLenght(self , length):
        self.__length=length
    def getLength(self):
        return self.__length
    def area(self):
        return self.__length * self.__length
    def perimeter(self):
        return 4*self.__length
        

class Circle (Shape):
    def __init__(self , radius):
        self.__radius=radius
    def setRadius(self , radius):
        self.__radius=radius
    def getRadius(self):
        return self.__radius
    def area(self):
        return self.__radius**2 * math.pi
    def perimeter(self):
        return 2*self.__radius* math.pi
    