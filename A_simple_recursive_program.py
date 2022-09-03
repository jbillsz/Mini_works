# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:46:12 2022
Recursive python
what is recursive python
a function that calls itself
@author: User
"""

#a simple recursive function
#Imagine a person dialling their number on their a phone and calling themself
#or imagine a person speaking in third person, that's how a recursive program
#works

def main():
    message()
    
def message():
    print('This is a recursive function')
    message()
        
        
main()