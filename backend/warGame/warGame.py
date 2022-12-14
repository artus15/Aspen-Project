import os
import sys
os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from warGame.deck import *
from warGame.player import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    warcount = 0
    while(len(p1)!=0 and len(p2)!=0):
        count = count+1
        p1, p2, total = playHand(p1, p2)
        warcount = warcount+total
    if(len(p1)==0):
        print("Player P2 won after {}".format(count)+" turns")
        return count, player2.name, warcount
    else:
        print("Player P1 won after {}".format(count)+" turns")
        return count, player1.name, warcount
            
def playHand(p1, p2):
    '''This method plays a hand, and gives the winning player the cards played
    '''
    wartotal = 0
    cardsPlayed = []
    buff1 = draw(p1)
    buff2 = draw(p2)
    cardsPlayed.append(buff1)
    cardsPlayed.append(buff2)
    if(buff1.val == buff2.val):
        buff1, buff2, p1, p2, cardsPlayed, wartotal = war(p1, p2, cardsPlayed, buff1, buff2)
    if(buff1.val < buff2.val):
        p2 = addCards(p2, cardsPlayed)
    else:
        p1 = addCards(p1, cardsPlayed)
    return p1, p2, wartotal

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
    wartotal = 1
    wartotall = 0
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
        buff1, buff2, p1, p2, cardsPlayed, wartotall = war(p1, p2, cardsPlayed, buff1, buff2)
    return buff1, buff2, p1, p2, cardsPlayed, wartotal+wartotall

def warStatistics(total):
    turns = []
    wars = []
    for i in range(total):
        turns.append(play("p1", "p2")[0])
        wars.append(play("p1", "p2")[2])
    turns.sort()
    turns = np.array(turns)
    mean = np.mean(turns)
    sd = np.std(turns)
    pdf = normal_dist(turns,mean,sd)
    plt.plot(turns ,pdf , color = 'red')
    plt.xlabel('Data points')
    plt.ylabel('Probability Density')
    plt.show()
    wars.sort()
    wars = np.array(wars)
    mean = np.mean(wars)
    sd = np.std(wars)
    warsPdf = normal_dist(wars,mean,sd)
    plt.plot(wars ,warsPdf , color = 'blue')
    plt.xlabel('Data points')
    plt.ylabel('Probability Density')
    plt.show()

    
def normal_dist(x , mean , sd):
    prob_density = np.round_((np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)/10000, 4)
    return prob_density