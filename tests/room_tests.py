import unittest

from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Haddaway's Hideaway")
        self.song = Song("Friday I'm In Love", "The Cure")


    def test_room_has_name(self):
        self.assertEqual("Haddaway's Hideaway", self.room.name)

    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))

    def test_add_song_to_playlist(self):
        self.room.add_song_to_playlist(self.song)
        self.assertEqual(1, len(self.room.playlist))