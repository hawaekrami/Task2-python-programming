# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:24:31 2024

@author: UOD Student
"""

import random
import Hangman_stages
wordlist=["happy", "weather", "orange", "apple", "carrot"]
lives=6
chosenword=random.choice(wordlist)
print(chosenword)
display=[]
for x in range(len(chosenword)):
    display+='-'
    
print(display)    
gameover= False
while not gameover:
    guessedletter=input("Guess a letter: ").lower()
    for position in range(len(chosenword)):
        letter=chosenword[position]
        if letter==guessedletter:
              display[position]=guessedletter
    print(display)          
    if guessedletter not in chosenword:
        lives-=1
        if lives==0:
            gameover=True
            print("You lose!!") 
    if '-'not in display:
        gameover=True
        print("You win!!") 
    print(Hangman_stages.stages[lives])     
        
              
    
    
    
    
    
    
    
    
    
    
    
    
    
    









