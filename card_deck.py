# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:38:23 2022
a program which runs and randomly deals you a deck of cards
@author: User
"""
import random
card_deck ={
    'ace of spade' : 1 ,'2 of Spade' : 2,
    '3 of spade': 3,'4 of spade': 4,
    '5 of spade': 5,'6 of spade': 6,
    '7 of spade': 7,'8 of spade': 8,
    '9 of spade': 9,'10 of spade': 10,
    'King of spade': 10,'Queen of spade': 10,
    'Jack of spade': 10,
    
    'ace of club' : 1 ,'2 of club' : 2,
    '3 of club': 3,'4 of club': 4,
    '5 of club': 5,'6 of club': 6,
    '7 of club': 7,'8 of club': 8,
    '9 of club': 9,'10 of club': 10,
    'King of club': 10,'Queen of club': 10,
    'Jack of club': 10,
    
    'ace of Hearts' : 1 ,'2 of Hearts' : 2,
    '3 of Hearts': 3,'4 of Hearts': 4,
    '5 of Hearts': 5,'6 of Hearts': 6,
    '7 of Hearts': 7,'8 of Hearts': 8,
    '9 of Hearts': 9,'10 of Hearts': 10,
    'King of Hearts': 10,'Queen of Hearts': 10,
    'Jack of Hearts': 10,
     
    'ace of Diamonds' : 1 ,'2 of Diamonds' : 2,
    '3 of Diamonds': 3,'4 of Diamonds': 4,
    '5 of Diamonds': 5,'6 of Diamonds': 6,
    '7 of Diamonds': 7,'8 of Diamonds': 8,
    '9 of Diamonds': 9,'10 of Diamonds': 10,
    'King of Diamonds': 10,'Queen of Diamonds': 10,
    'Jack of Diamonds': 10,
    }

key, value = random.choice(list(card_deck.items()))
# takes two assignments and turns the card deck dictionary into a list
card_deck[key] = value
print(f' You, have been dealt, {key}')
