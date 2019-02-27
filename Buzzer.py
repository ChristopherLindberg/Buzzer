# -*- coding: utf-8 -*-
from random import uniform, randint, shuffle
from time import sleep
import os 
from CreateQuestions import get_cards
from Card import Card
from Player import Player
import re
from pygame import mixer # Load the required library

def create_deck():
    
    cards = get_cards()
    
    deck = []
    for card in cards:
        
        for i in range(card.lives):
            
            newCard = Card(question = card.question)
            deck.append(newCard)


    return deck

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pick_opponent(players, name):
    
    usedNames = [player.name for player in players if player.name != name]
    
    return usedNames[randint(0, len(usedNames)-1)]

   
def pick_player(players):
    usedNames = [player.name for player in players]
    
    return usedNames[randint(0, len(usedNames)-1)]
     
def get_names():
    #Creates a list of names and checks with the user that the list is correct.
    while True:
         
        names = []
        print("Enter exit to quit names")
        
        while True:
            name = input("Enter name: ")
            if name.lower() in ['exit', 'e', 'q', 'quit']:
                break;
            else:
                names.append(name)
                clear()
                print("Enter exit to quit names")
        
        for i in range(3):
            shuffle(names)
        
        print("I found {} names.".format(len(names)))
        print("The names are:")
        print(names)
        if input("Are these names correct? y/n ").lower() == 'y':
            clear()
            break
        
    players = []
    for name in names:
        players.append(Player(name))
        
    return players

# init gui
#gui = GUI(font=40)


# init mixer
mixer.init()
mixer.music.load('{}/Buzzer.mp3'.format(os.getcwd()))

# set players and time
players = get_names()
waitMin = 3*60
waitMax = 5*60

# for testing
#waitMin = 0
#waitMax = 1

clear()

while True:
    
    # while game is running
    print('Shuffling cards')
    
    # create deck
    cards = create_deck()
    
    # shuffle
    shuffle(cards)
    
    while len(cards) != 0:
        #  wait a specific time
        sleep(uniform(waitMin, waitMax))
        clear()
    
    
        # get player
        playerName = pick_player(players)
        
        # get opponent
        opponentName = pick_opponent(players, playerName)
        
    
        cardIndex = randint(0, len(cards) - 1)
        card = cards[cardIndex] #selected card
        
        # reduce card lives
        cards[cardIndex].lives -= 1
        
        if cards[cardIndex].lives == 0:
            cards.pop(cardIndex)
        
        printString = card.question
        
        
        
        
        # input player
        printString = re.sub('%PLAYER%', playerName, printString)
        
        # input opponent
        printString = re.sub('%OPPONENT%', opponentName, printString)
        
        # print question
        print(printString)
        
        # play sound
        mixer.music.play()