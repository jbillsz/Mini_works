# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 22:35:36 2022

@author: User
"""
import random
a= int(input("How many numbers do you want to generate?:"))
def Lotto(a):
    lotto = [0]*a #creates a list based on the number 0f elements    
    print("I am generating at random seven numbers")
    for value in range (a):
        lotto[value]= random.randint(0,9)# generates a specific random number for specific index in the list
    #a for loop which prints the numbers in the list
    for num in lotto:
        print(num)
        
        
        
        
Lotto(a)