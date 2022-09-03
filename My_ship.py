# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 22:05:30 2021
A project on my own to understand object oriented programming.
@author: Louis James Billah
Project is a success
can use more refinement.
Key concepts of OOP
Object Oriented analysis
Unified Modified Language
Composition,aggregation, inheritance, polymorphism, method creation

"""

class Central_room:
    "Main central control room"
    def statement(self):
        print("Welcome Captain,to the control room")

class Bridge:
    "Corridor connecting all the rooms"
    def bridge_connect(self):
        print('Main corridor, where are you going?')

class Engine:
    "This is the engine of the ship."
    def engine(self):
        print('This is the engine.')
    def engine_on(self):
        "A method to turn the engine."
        print("Engine on!")
    def engine_off(self):
        "A method to turn engine off"
        print("Engine off!")
    
class Engine_room:
    "Calling a composition method for the engine room with"
    def __init__(self):
        "Instantiating the class Engine as aa public attribute."
        self.engine_room = Engine() #This is the instance of the engine
    def engine_slot(self):
        "This is the slot for the engine"
        self.engine_room.engine() #this calls the attribute of the Engine class.
    def turn_on_engine(self):
        self.engine_room.engine_on() #this calls the attribute of the engine class
    
    def turn_off_engine(self):
        self.engine_room.engine_off() #this calls the engine off feature from the engine class.

class turbine(Engine):
    "Turbine in the plane"
    
    def rev_up(self):
        "This means the engine is rev-ed up!"
        print("Turbines started.")
    def rev_down(self):
        "This means engine has been turned off"
        print("Turbines turned down.")

class wing:
    "This class describes the wings of the space ship"
    def wing_adjustment(self):
        print("Wing adjusted for flight")

class Vertical_stabilizer(wing):
    "The stabilizer class which is the rear wing"
    def wing_adjustment(self): #calling a method override here
        print("Vertical Stabilizer adjusted for flight.")
    
    def rudder(self): # rudder is a part of the rear adjustments so it has to be a method not a class
        print('Rudder adjusted!')
        
class horizontal_stabilizer(wing):
    "A stabilizer class which is in the rear wing."
    def wing_adjustment(self): #calling method override
        print('Horizontal Stabilizer adjusted for flight.')

    def rudder(self):
        print("Rudder adjusted. ") #Didn't create a class for stabilizers so i had to retype it.
        
class ship:
    "This is the main class which is going to be composed of the other classes."
    def __init__(self,name): # calling the composite attributes of ohter classes.
        "Defining all the composite attributes of the spaceship."
        "All these attributes are from an exisiting class which exhibit composition, inheritance or polymorphism."
        self.name = name
        self.corridor = Central_room()
        self.bridge = Bridge()
        self.engine_room = Engine_room()
        self.wing = wing()
        self.turbine = turbine()
        self.Vertical_stabilizer = Vertical_stabilizer()
        self.horizontal_stabilizer = horizontal_stabilizer()
        
    def ship_corridor(self):
        "Main's ship control room"
        print(f'This is the {self.name} command centre.')
        self.corridor.statement() #calls the Central room's statement class

    def ship_bridge(self):
        "Ship's bridge which links all rooms."
        self.ship_bridge.bridge_connect()
        
    def ship_engine_room(self):
        "Ship's  main engine room."
        print(f"{self.name}'s main ship engine is located here.")
        self.engine_room.engine_slot()
    
    def ship_engine_on(self):
        "Turns ship engine on"
        self.engine_room.turn_on_engine()
        #This is a composition within a composition
    
    def ship_engine_off(self):
        "Turns ship engine off"
        self.engine_room.turn_off_engine()
        # This is also a composition within a composition
        
    def ship_turbine_on(self):
        "This is for the ship's turbines in the wings, also an engine."
        #This turns the ship engine on
        self.turbine.rev_up()
    
    def ship_turbine_off(self):
        "This is for the ship's turbine."
        self.turbine.rev_down()
        
    def ship_vertical_stabilizer(self):
        "This is for the stabilizers"
        print("Stabilizer stabilizing....1...2...3.")
        self.Vertical_stabilizer.wing_adjustment()
        print("Rudder stabilising 1.....2....3")
        self.Vertical_stabilizer.rudder()
    
    def ship_horizontal_stabilizer(self):
        "This is for the horizontal stabilizer"
        print("Stabilizer stabilizing.....1....2...3")
        self.horizontal_stabilizer.wing_adjustment()
        print("Rudder stabilising.......1....2...3.")
        self.horizontal_stabilizer.rudder()
        
S = ship('Louis')
S.ship_turbine_on()
S.ship_turbine_off()
S.ship_horizontal_stabilizer()
S.ship_engine_on()
S.ship_engine_off()
S.ship_engine_room()
S.ship_corridor()
S.ship_vertical_stabilizer()