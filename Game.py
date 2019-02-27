# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:45:21 2018

@author: Lindberg
"""


from random import uniform, randint, shuffle
from time import sleep
import os 
from CreateQuestions import get_cards
from Card import Card
from Player import Player
import re
from pygame import mixer # Load the required library


class Game():

    
    def __init__(self):
        
        # init mixer
        mixer.init()
        self.mixer = mixer.music
        self.mixer.load('{}/Buzzer.mp3'.format(os.getcwd()))
    
        self.players = None
        
        self.waitMin = 0*60
        self.waitMax = 0.4*60
        
        self.sleepTime = None
        
        self.player = None
        self.opponent = None
        
        self.status='paused'
        self.started = False
        # setup
        self.get_names()

    def sleep_game(self):
        
        while self.status.lower() != 'paused' or self.sleepTime > 0:
            self.sleepTime -= 1
            sleep(1)

    @staticmethod
    def create_deck():
        
        cards = get_cards()
        
        deck = []
        for card in cards:
            
            for i in range(card.lives):
                
                newCard = Card(question = card.question)
                deck.append(newCard)
    
    
        return deck

    def pick_opponent(self):
        
        usedNames = [player.name for player in self.players if player.name != self.playerName]
        self.opponentName = usedNames[randint(0, len(usedNames)-1)]

   
    def pick_player(self):
        usedNames = [player.name for player in self.players]
        self.playerName = usedNames[randint(0, len(usedNames)-1)]
     
    def reset(self): 
        self.playerName = None
        self.opponentName = None
        
        
    def get_names(self):
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
                    print("Enter exit to quit names")
            
            for i in range(3):
                shuffle(names)
            
            print("I found {} names.".format(len(names)))
            print("The names are:")
            print(names)
            if input("Are these names correct? y/n ").lower() == 'y':
                break
            
        players = []
        for name in names:
            players.append(Player(name))
            
        self.players = players

    
    def main(self):
        
        while True:
            
            # while game is running
            print('Shuffling cards')
            
            # create deck
            cards = self.create_deck()
            
            # shuffle
            shuffle(cards)
            
            while len(cards) != 0:
                #  wait a specific time
                self.sleepTime = uniform(self.waitMin, self.waitMax)
                
                # sleep game
                self.sleep_game()
            
                # get player
                self.pick_player()
                
                # get opponent
                self.pick_opponent()
                
            
                cardIndex = randint(0, len(cards) - 1)
                card = cards[cardIndex] #selected card
                
                # reduce card lives
                cards[cardIndex].lives -= 1
                
                if cards[cardIndex].lives == 0:
                    cards.pop(cardIndex)
                
                printString = card.question
                
                
                
                
                # input player
                printString = re.sub('%PLAYER%', self.playerName, printString)
                
                # input opponent
                printString = re.sub('%OPPONENT%', self.opponentName, printString)
                
                # print question
                print(printString)
                
                # play sound
#                self.mixer.play()
                print('music')
                
                # reset
                self.reset()
                
                
                
                