# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:54:48 2022
Tower of hanoi
@author: User
"""
def main ():
    """This is the main function which calls the tower of hanoi game"""
    num_disc = 3 # number of discs to be used
    from_peg =1 # first peg
    to_peg =3 #third peg
    temp_peg =2 # second peg to be used as a temporary peg
    
    tower_of_hanoi(num_disc,from_peg, to_peg,temp_peg) #A function 
    print("All pegs are moved")
    
def tower_of_hanoi(num_disc,from_peg, to_peg,temp_peg): 
    """A function which simulates the tower of hanoi"""
    if num_disc >0:
        tower_of_hanoi(num_disc-1,from_peg,temp_peg,to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        tower_of_hanoi(num_disc-1,temp_peg, to_peg,from_peg)
        

main()
        
    