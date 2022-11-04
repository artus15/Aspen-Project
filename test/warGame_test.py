import unittest
import os
import sys
os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from backend.warGame.warGame import *

class warGameTest(unittest.TestCase):
    def test_deal(self):
        '''Test if the dealCards method gives the two players the same number of cards
        '''
        deck1 = dealCards()[0]
        deck2 = dealCards()[1]
        self.assertEqual(len(deck1), len(deck2))
    
    def test_show_rules(self):
        '''Test the method showRules which give the link to the rules of the game
        '''
        self.assertEqual(showRules(),"Rules can be found at: https://bicyclecards.com/how-to-play/war/")
        
    def test_play(self):
        '''Test the play functionnality of the war game
        '''
        count, winner, _ = play("Artus", "Aspen")
        self.assertTrue(count>0)
        self.assertTrue(winner=="Artus" or winner == "Aspen")
