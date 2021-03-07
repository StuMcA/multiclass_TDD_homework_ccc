import unittest

from classes.karaoke_bar import KaraokeBar
from classes.room import Room
from classes.guest import Guest

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        rooms = [Room("Haddaway's Hideaway", 15)]
        self.karaoke_bar = KaraokeBar("CodeClan Caraoke", rooms, 10000, 15)
        self.guest_1 = Guest("Bonnie Tyler", 500)
        self.guest_2 = Guest("Axl Rose", 5)


    def test_karaoke_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.karaoke_bar.name)

    def test_karaoke_bar_has_rooms(self):
        self.assertEqual(1, len(self.karaoke_bar.rooms))

    def test_karaoke_bar_has_money(self):
        self.assertEqual(10000, self.karaoke_bar.till)

    def test_karaoke_bar_has_entry_fee(self):
        self.assertEqual(15, self.karaoke_bar.entry_fee)

    def test_charge_guest_entry_fee(self):
        self.karaoke_bar.charge_guest_entry_fee(self.guest_1)
        self.assertEqual(10015, self.karaoke_bar.till)
        self.assertEqual(485, self.guest_1.wallet)

    def test_check_in__can_afford(self):
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.assertEqual(10015, self.karaoke_bar.till)
        self.assertEqual(485 , self.guest_1.wallet)
        self.assertEqual(1, len(self.karaoke_bar.rooms))

    def test_check_in__cant_afford(self):
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_2)
        self.assertEqual(10000, self.karaoke_bar.till)
        self.assertEqual(5 , self.guest_2.wallet)
        self.assertEqual(0, len(self.karaoke_bar.rooms[0].guests))

    def test_check_in__room_full(self):
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_in_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.assertEqual(15, len(self.karaoke_bar.rooms[0].guests))


    def test_add_guest_to_room(self):
        self.karaoke_bar.add_guest_to_room(self.karaoke_bar.rooms[0], self.guest_1)
        self.assertEqual(1, len(self.karaoke_bar.rooms[0].guests))

    def test_check_out_guest(self):
        self.karaoke_bar.add_guest_to_room(self.karaoke_bar.rooms[0], self.guest_1)
        self.karaoke_bar.check_out_guest(self.karaoke_bar.rooms[0], self.guest_1)
        self.assertEqual(0, len(self.karaoke_bar.rooms[0].guests))

