import os
import sys
os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from warGame.cards import *
import random

def buildDeck():
    '''This initiates a deck of cards, made out of 52 different cards
    '''
    cards = []
    for s in ["Spades", "Hearts", "Diamonds", "Clubs"]:
        for v in range(1,14):
            cards.append(Card(s,v))
    return cards 
                
def showDeck(deck):
    '''This methos prints every cards in the deck
    '''
    for c in deck:
        c.showCard()
    return True

def shuffle(deck):
    '''This method shuffles the deck
    '''
    for i in range(len(deck) -1, 0, -1):
        rand = random.randint(0, i)
        deck[i], deck[rand] = deck[rand], deck[i]
    return deck

def draw(deck):
    '''This method draws a card from the deck
    '''
    return deck.pop()

def addCard(deck, card):
    '''This method adds card to the deck
    '''
    deck.insert(0, card)
    return deck
