# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:11:29 2021
right angle triangle solver
@author: User
"""

from math import sqrt
print ("Welcome to the square root solver.")
base = int(input("Input base:"))
height = int(input("Input height:"))

def triangle (base, height):
    #creating a function which will calculate the length of the hypotenuse
    b2 = base**2
    h2 = height**2
    b_h = b2 + h2
    hypotenuse = sqrt(b_h)
    area = 0.5*(base * height)
    print(f"Hypotenuse is {hypotenuse} metres and area is {area} metre sqauared.")

# Note to self don't call a return function and a print function in the same function
triangle (base,height)

