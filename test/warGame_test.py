import unittest
import os
import sys
os.path.join(os.path.dirname(__file__), '../')
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from warGame.warGame import *

class warGameTest(unittest.TestCase):
    def test_deal(self):
        self.assertEqual("yes","yes")