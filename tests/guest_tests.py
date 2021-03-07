import unittest

from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Bonnie Tyler", 500)
        self.guest_2 = Guest("Meat Loaf", 25, Song("Raspberry Beret", "Prince"))

    def test_guest_has_name(self):
        self.assertEqual("Bonnie Tyler", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(500, self.guest.wallet)

    def test_guest_favourite_song__empty_by_default(self):
        self.assertEqual(None, self.guest.favourite_song)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Raspberry Beret", self.guest_2.favourite_song.name)
        self.assertEqual("Prince", self.guest_2.favourite_song.artist)
