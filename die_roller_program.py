# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:55:21 2021
dice programming

@author: User
"""

import random # import random to set your max and min values
min = 1 #setting a minimum value of 1 since a die begins from one
max =6 # set maximum value of 6 since die ends at six.
number = random.randint(min, max) #using the random integer from the random module
roll = input('Will you like to roll again?:') #an input to take the user's choice

while roll =="Yes" or roll =="Y" or roll == "yes" or roll == "y": # a while loop to continue looping through the statements.

    number = random.randint(min, max)
    # I input the number variable in here because the while loop needs to go through it as it user inputs his choice
    # calling it outside the loop will only make only one random generated number only be used to loop through the statements
    if number == 1:
        print("========")
        print("|      |")
        print("|  0   |")
        print("========")
    if number ==2:
        print("========")
        print("|      |")
        print("|  00  |")
        print("========")
    if number ==3:
        print("========")
        print("|      |")
        print("|  000 |")
        print("========")
    if number == 4:
        print("========")
        print("|   0  |")
        print("|  000 |")
        print("========")
    if number ==5:
        print("========")
        print("|  00  |")
        print("|  000 |")
        print("========")
    if number ==6:
        print("========")
        print("|   000|")
        print("|  000|")
        print("========")
    else: print('Better luck')
    roll = input('Will you like to roll again?:')# this kind of works the same way as the number variable