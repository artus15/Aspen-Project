import os
import sys
os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from warGame.deck import *
from warGame.player import *

def showRules():
    print("Rules can be found at: https://bicyclecards.com/how-to-play/war/")
    return "Rules can be found at: https://bicyclecards.com/how-to-play/war/"
    
def dealCards():
    '''This method deals the cards to the two players
    '''
    p1, p2= [], []
    deck = buildDeck()
    deck = shuffle(deck)
    while(len(deck)!=0):
        if(len(deck)%2==0):
            addCard(p1, draw(deck))
        else:
            addCard(p2, draw(deck))
    return p1, p2

def play(firstPlayer, secondPlayer):
    '''This method plays the war game until a player wins
    '''
    player1, player2 = Player(firstPlayer), Player(secondPlayer)
    p1, p2 = player1.deck, player2.name
    p1, p2 = dealCards()
    count = 0
    while(len(p1)!=0 and len(p2)!=0):
        count = count+1
        p1, p2 = playHand(p1, p2)    
    if(len(p1)==0):
        print("Player P2 won after {}".format(count)+" turns")
        return count, player2.name
    else:
        print("Player P1 won after {}".format(count)+" turns")
        return count, player1.name
            
def playHand(p1, p2):
    '''This method plays a hand, and gives the winning player the cards played
    '''
    cardsPlayed = []
    buff1 = draw(p1)
    buff2 = draw(p2)
    cardsPlayed.append(buff1)
    cardsPlayed.append(buff2)
    if(buff1.val == buff2.val):
        buff1, buff2, p1, p2, cardsPlayed = war(p1, p2, cardsPlayed, buff1, buff2)
    if(buff1.val < buff2.val):
        p2 = addCards(p2, cardsPlayed)
    else:
        p1 = addCards(p1, cardsPlayed)
    return p1, p2

def addCards(p, cards):
    '''This method inserts cards in the winner's deck
    '''
    cards = shuffle(cards)
    while(len(cards)!=0):
        p = addCard(p, cards.pop())
    return p

def war(p1, p2, cardsPlayed, buff1, buff2):
    '''This method takes care of the War situation
    '''
    if(len(p1)>2 and len(p2)>2):
        cardsPlayed.append(draw(p1))
        cardsPlayed.append(draw(p2))
        buff1 = draw(p1)
        buff2 = draw(p2)
        cardsPlayed.append(buff1)
        cardsPlayed.append(buff2)
    elif(len(p1)==1):
        cardsPlayed.append(draw(p2))
        buff1 = draw(p1)
        buff2 = draw(p2)
        cardsPlayed.append(buff1)
        cardsPlayed.append(buff2)
    elif(len(p2)==1):
        cardsPlayed.append(draw(p1))
        buff1 = draw(p1)
        buff2 = draw(p2)
        cardsPlayed.append(buff1)
        cardsPlayed.append(buff2)
    elif(len(p1)==0):
        cardsPlayed.append(draw(p2))
        buff2 = draw(p2)
    else:
        cardsPlayed.append(draw(p1))
        buff1 = draw(p1)
    if(buff1.val == buff2.val):
        buff1, buff2, p1, p2, cardsPlayed= war(p1, p2, cardsPlayed, buff1, buff2)
    return buff1, buff2, p1, p2, cardsPlayed
