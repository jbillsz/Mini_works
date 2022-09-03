# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:00:39 2021
A program for Billah Corporation
@author: User
"""

name = input("Administrator name: \t") # Takes user input
#The hourly_rate variable stores the hourly rate 
hourly_rate = float(input("\nInput today's hourly rate($) :\t"))
#Takes the input of the number of employees
number_of_employees =int(input("\nHow many people worked today? :\t"))
# A function that combines all the variables into a function
def pay_rate(name, hourly_rate):
    print(f"\nWelcome, {name}.")
    #Used a list comprehension here
    #a for loop will still work here but the list comprehesion shortens
    #the code and makes it more readable
    #example
    #create a list and replace the items using the for loops and index methods
    #hours= [0]*number_of_employees instead of using list comprehensions
    
    hours = [value *1 for value in range(number_of_employees)] 
    
    for index in range(number_of_employees):
        print(f"\nHow many hours did employee {index+1} work?")
        hours[index]= int(input("\nInput his hours here:\t"))
    
    for index in range(number_of_employees):
        print(f"\nEployee {index+1} made ${hours[index]*hourly_rate}" )
        

pay_rate(name, hourly_rate)