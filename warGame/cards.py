class Card: 
    def __init__(self, suit, val):
        '''Initiate each card with:
            suit: Spades, Hearts, Diamonds, Clubs
            val: 1 (ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 (jack), 12 (queen), 13(king)
        '''
        self.suit = suit
        self.val = val
        
    def showCard(card):
        '''This method prints a card, following the format:
            VAL of SUIT
        '''
        if(card.val==1):
            print("{} of {}".format("Ace", card.suit))
            return "{} of {}".format("Ace", card.suit)
        elif(card.val==11):
            print("{} of {}".format("Jack", card.suit))
            return "{} of {}".format("Jack", card.suit)
        elif(card.val==12):
            print("{} of {}".format("Queen", card.suit))
            return "{} of {}".format("Queen", card.suit)
        elif(card.val==13):
            print("{} of {}".format("King", card.suit))
            return "{} of {}".format("King", card.suit)
        else:
            print("{} of {}".format(card.val, card.suit))
            return "{} of {}".format(card.val, card.suit)