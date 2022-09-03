# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:20:10 2022
Greatest common divisor
@author: User
"""
def main():
    """A function recursive function"""
    x = int(input ("Input number here:"))
    y = int(input ("Input another number here:"))
    print(f"The GCD of {x} and {y} is {gcd(x,y)}")
   
    
    
def gcd(x,y):
    """A function which prints the highest GCD between two numbers"""
    """x is the start point, y is the end point"""
    if x % y==0:
        return y
    else:
        return(x, x%y)
    
    
main()