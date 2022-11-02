import unittest
import os
import sys
os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from warGame.cards import *

class CardTest(unittest.TestCase):
    def test_create_card(self):
        '''Test the simple creation of a card
        '''
        card = Card("Hearts", 1)
        self.assertEqual(card.val, 1)
        self.assertEqual(card.suit, "Hearts")
        
    '''
    This list of tests test the different outputs of the function showCard        
    '''
    def test_show_ace(self):
        card = Card("Hearts", 1)
        self.assertEqual(card.showCard(), "Ace of Hearts")
        
    def test_show_jack(self):
        card = Card("Hearts", 11)
        self.assertEqual(card.showCard(), "Jack of Hearts")
    
    def test_show_queen(self):
        card = Card("Hearts", 12)
        self.assertEqual(card.showCard(), "Queen of Hearts")
        
    def test_show_king(self):
        card = Card("Hearts", 13)
        self.assertEqual(card.showCard(), "King of Hearts")
        
    def test_show_card(self):
        card = Card("Hearts", 5)
        self.assertEqual(card.showCard(), "5 of Hearts")

if __name__ == '__main__':
    unittest.main()