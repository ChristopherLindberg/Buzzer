class Card():
    
    question = ''
    lives = 1 
    
    def __init__(self, question, lives=1):
        
        self.question = question
        self.lives = lives