import unittest

from classes.drinks_bar import DrinksBar
from classes.drink import Drink
from classes.room import Room
from classes.guest import Guest
from classes.karaoke_bar import KaraokeBar

class TestDrinksBar(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Bonnie Tyler", 500)
        self.guest_2 = Guest("Meat Loaf", 17)
        rooms = [Room("Haddaway's Hideaway", 15)]
        drinks = [Drink("Tennents", 2.99)]
        self.drinks_bar = DrinksBar(rooms[0], 1000, drinks)
        self.karaoke_bar = KaraokeBar("CodeClan Caraoke", rooms, 10000, 15)

    def test_drinks_bar_has_till(self):
        self.assertEqual(1000, self.drinks_bar.till)

    def test_drinks_bar_has_drinks(self):
        self.assertEqual(1, len(self.drinks_bar.drinks))

    def test_cash_taken_starts_zero(self):
        self.assertEqual(0, self.drinks_bar.cash_taken)

    def test_sell_drink__can_afford(self):
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.drinks_bar.sell_drink(self.karaoke_bar.rooms[0], self.guest_1, self.drinks_bar.drinks[0])