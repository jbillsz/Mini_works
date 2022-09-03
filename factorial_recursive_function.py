# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:43:29 2022
a factorial case recursive programming
@author: User
"""
def main():
    #the main problem which accepts the factorial number
    number = int(input("Put number here: "))
    fact = factorial(number)
    
    print(f"The factiorial of {number} is {fact}.")
    
def factorial(num):
    #the recursive control bit which contains the conditionals
    if num==0:
        return 1
    else:
            return num* factorial(num-1)
        
main()#calling the main function


        