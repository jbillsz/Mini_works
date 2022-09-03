# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 20:53:18 2022

@author: User
"""
def main():
    numbers= list(range(1,10))
    my_sum = range_sum(numbers,2,5)
    print("The sum of the items from 2 to 5 is", my_sum)

def range_sum(numbers,start,finish):
   if start > finish:
       return 0
   else:
       
       return numbers[start] + range_sum(numbers,start+1, finish)
 
main()