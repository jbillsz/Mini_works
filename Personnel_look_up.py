# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:50:05 2022
OOP 
@author: User
"""

class Employee():
    """An employee class which holds the following attributes:
        name,ID number , department and job title"""
    def __init__(self,name,id_number,deparment,job_title):
        self.name = name
        self.id_number = id_number
        self.deparment = deparment
        self.job_title = job_title
        



number= int(input('How many employees are registered:'))
for i in range (number):
    """A for loop which loops through the number of employees and prints
    each ones data"""
    name=input('\nEmployee name: ')
    id_number=input('\nEmployee ID: ')
    department=input('\nEmployee department:')
    job_title= input('\nEmployee position:')
    user=Employee(name,id_number,department, job_title) 
    print(f'\n{user.name} is the user name.'
          f'\n{user.id_number} is the user id.'
          f'\n{user.deparment} is the user department.')