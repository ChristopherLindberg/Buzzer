# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:29:11 2018

@author: Lindberg
"""

import tkinter as tk
from random import uniform, randint, shuffle
from time import sleep
import os 
from CreateQuestions import get_cards
from Card import Card
from Player import Player
import re
from pygame import mixer # Load the required library

#test1
class Game():
    
    def __init__(self, font):
        
        ### GUI related stuff
        
        # fontsize
        self.fontSize = font
        
        # GUI root
        self.root = tk.Tk()
    
        # text message
        self.message = tk.StringVar()
        self.message.set('Start Text')
               
        # variables
        self.status = 'Paused'
        
        # window title
        self.root.title(self.status)
        
        # init resize
        tk.Grid.rowconfigure(self.root, 0, weight=1 )
        tk.Grid.columnconfigure(self.root, 0, weight=1 )
    
    
        # init elements
        self.message_box()
        self.pause_button()
        self.start_button()
    
        
        ### GAME related stuff
        # init mixer
        mixer.init()
        self.mixer = mixer.music
        self.mixer.load('{}/Buzzer.mp3'.format(os.getcwd()))
    
        self.players = None
        
        self.waitMin = 3*60
        self.waitMax = 5*60
        
        self.sleepTime = None
        self.deck = None
        
        
        self.player = None
        self.opponent = None
        
        self.status='paused'
        
        
        ### debug mode
        self.debug = False
        
        if self.debug:
            self.waitMin = 0
            self.waitMax = 2
        
        ### setup
        self.get_names()
        self.create_deck()
        self.sleepTime = uniform(self.waitMin, self.waitMax)
    
        #%% rescale
        for rowValue in range(6):
            tk.Grid.rowconfigure(self.root, rowValue, weight=1)
        
        for columnValue in range(4):
            tk.Grid.columnconfigure(self.root, columnValue, weight=1)



    def change_status(self, title):
#        print(title)
        self.status = title
        self.root.title(title)


        # pause or resume game as well
        self.status = title
            
        while self.status != 'Paused':
            while self.status != 'Paused' and self.sleepTime > 0:
                sleep(0.1)
                self.sleepTime -= 0.1
                self.root.update()
                
            if self.sleepTime < 0:
                
                self.draw_card()
                self.root.update()
                self.sleepTime = uniform(self.waitMin, self.waitMax)
            
            if len(self.deck) == 0:
                self.create_deck()
                    


    def message_box(self):
        
        outputMessage = tk.Message(self.root, text='', textvariable = self.message, font=("Times", self.fontSize))
        
        # autoscale
        outputMessage.grid(row=0, column=0, rowspan=5, columnspan=4, sticky=tk.EW)

    def pause_button(self):
        pauseVariable = tk.StringVar()
        pauseVariable.set('Pause')
        
        pauseButton = tk.Button(self.root, textvariable = pauseVariable, font=("Times", self.fontSize), command=lambda title = 'Paused': self.change_status(title))
        

        # autoscale
        pauseButton.grid(row=5, column=1, rowspan=1, columnspan=1, sticky=tk.NSEW)


    def start_button(self):
        startVariable = tk.StringVar()
        startVariable.set('Start')
        
        startButton = tk.Button(self.root, textvariable = startVariable, font=("Times", self.fontSize), command=lambda title = 'Running': self.change_status(title))
        
        # autoscale
        startButton.grid(row=5, column=2, rowspan=1, columnspan=1, sticky=tk.NSEW)



    def font(self):
        pass
        ### set font size
        #fontStatus = t k.StringVar()
        #fontEntry = tk.Entry(root, textvariable = fontStatus)
        #fontStatus.set('Font size = 20')
        #fontEntry.grid(row=5, column=1, rowspan=1, columnspan=1)

    def start(self):
        self.root.mainloop()


    def sleep_game(self):
        
        while self.status.lower() != 'paused' or self.sleepTime > 0:
            self.sleepTime -= 1
            sleep(1)


    def create_deck(self):
        
        cards = get_cards()
        
        deck = []
        for card in cards:
            
            for i in range(card.lives):
                
                newCard = Card(question = card.question)
                deck.append(newCard)
    
    
        self.deck = deck
        self.message.set('Shuffling cards')
        shuffle(self.deck)


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

    
    def draw_card(self):
        
        # get player
        self.pick_player()
        
        # get opponent
        self.pick_opponent()
        
    
        cardIndex = randint(0, len(self.deck) - 1)
        card = self.deck[cardIndex] #selected card
        
        # reduce card lives
        self.deck[cardIndex].lives -= 1
        
        if self.deck[cardIndex].lives == 0:
            self.deck.pop(cardIndex)
        
        printString = card.question
        
        # input player
        printString = re.sub('%PLAYER%', self.playerName, printString)
        
        # input opponent
        printString = re.sub('%OPPONENT%', self.opponentName, printString)
        
        
        # set question into box
        self.message.set(printString)
        
        # play sound
        self.mixer.play()
        
        # reset
        self.reset()
        
        
                                               
# setup game
game = Game(font=40)

# start game/gui
game.start()