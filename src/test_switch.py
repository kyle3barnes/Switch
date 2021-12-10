import unittest
from src.main import Switch
from src.PlayingCard import *

class Testing(unittest.TestCase):

    def test_get_hand(self):
        deck = PlayingCard.generate_deck()
        deck = PlayingCard.shuffle_cards(deck)
        self.assertEqual(7, len(Switch.get_hands(deck, )[0]))

    def test_number_of_hands(self):
        deck = PlayingCard.generate_deck()
        deck = PlayingCard.shuffle_cards(deck)
        self.assertEqual(2, len(Switch.get_hands(deck, )))

    def test_user_turn(self):
        deck = PlayingCard.generate_deck()
        deck = PlayingCard.shuffle_cards(deck)
        self.assertNotEqual(deck, Switch.userTurn(deck, ['H7', ])[0])

   # def test_valid_good_input(self):
       # self.assertEqual(0, Switch.check_valid(self, 'H2', 0, ['D2', 'S7']))
