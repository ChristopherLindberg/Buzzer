
from Card import Card

def get_cards():
    cards = []
    
    # add tårer cards
    for i in range(1, 9):
        newCard = Card(question = '%PLAYER% skal drikke {} tårer.'.format(i), lives = 3)
        cards.append(newCard)
        
        
    # add text cards
    
    cards.append(Card(question = "%PLAYER% skal kaste med to terninger og drikke antallet af øjne.", lives = 2))
    
    cards.append(Card(question = "Alle drikker en frisk øl. Den der bliver færdig langsomst er træmand i tre runder.", lives = 1))
    
    cards.append(Card(question = "%PLAYER% Bliver ved med at slå med terningerne til %PLAYER% får en 6\'er. Husk altid at drikke - selv når du får 6 (Max = 4).", lives = 1))
    
    cards.append(Card(question = "Alle slår med en terning. Den der slår højest må give 10 tårer ud.", lives = 1))
    
    cards.append(Card(question = "%PLAYER% er træmand de næste fem runder. Hvis det ikke giver mening i spillet drikker %PLAYER% 10 tårer.", lives = 1))
    
    cards.append(Card(question = "Fællesskål!", lives = 6))
    
    cards.append(Card(question = "%PLAYER% skal tage en halv bunder!", lives = 2))
    
    cards.append(Card(question = "%PLAYER% skal tage en bunder!", lives = 1))
        
    cards.append(Card(question = "%PLAYER% skal hjælpe %OPPONENT% så meget som er påkrævet de næste 2 runder eller 3 minutter - hvad end der giver mening.", lives = 2))
    
    cards.append(Card(question = "%PLAYER% skal udfordre %OPPONENT% i en kort udfordring. Taberen tager 8 tårer - med mindre andet aftales.", lives = 3))

    cards.append(Card(question = "%PLAYER% skal tage et shot af det stærkeste alkohol til rådighed - med mindre andet aftales.", lives = 3))

    cards.append(Card(question = "%PLAYER% skal slå med en terning. Alle andre skal satse på hvad det bliver og give/tage hvad øjene viser alt efter om de vandt.", lives = 3))
    
    return cards