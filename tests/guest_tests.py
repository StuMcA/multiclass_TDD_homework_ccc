import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Bonnie Tyler", 500)

    def test_guest_has_name(self):
        self.assertEqual("Bonnie Tyler", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(500, self.guest.wallet)