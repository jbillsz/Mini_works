# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:28:18 2022

@author: User
"""

class Personnel():
    def __init__(self,name,address,age, phone):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone = phone
        
    def set_name(self,name):
        self.__name = name
    
    def get_name(self):
        print(self.__name)
        
    def set_age(self,age):
        self.__age = age
    
    def get_age(self):
        print(self.__age)
     
    def set_phone(self,phone):
        self.__phone = phone
    
    def get_phone(self):
        print(self.__phone)
     
    def set_address(self,address):
        self.__address = address
    
    def get_address(self):
        print(self.__address)
     
        
Louis = Personnel('Louis','P.O.Box Dk 249', 23, 550001782)
Louis.set_address('Adenta Rd 2988')
Louis.get_address()