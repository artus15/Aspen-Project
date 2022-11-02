import unittest
import os
import sys
os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from warGame.deck import *

class DeckTest(unittest.TestCase):    
    
     
    def test_shuffle_deck(self):
        '''Test the shuffle method by drawing two cards supposed to have not following value 
        or different suit (false 1 out of 51 times)
        '''
        deck = buildDeck()
        deck = shuffle(deck)
        card1 = draw(deck)
        card2 = draw(deck)
        self.assertFalse(card1.val == card2.val+1 and card1.suit == card2.suit)    
        
        
    def test_add_card(self):
        '''Test the addCard methos buy adding one into the deck, and popping in back 
        '''
        emptyDeck = []
        card = Card("Hearts", 1)
        deck = addCard(emptyDeck, card)
        self.assertEqual(card, draw(deck))

        
if __name__ == '__main__':
    unittest.main()