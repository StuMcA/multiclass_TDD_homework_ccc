import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Friday I'm In Love", "The Cure")
        self.song_2 = Song("Cosmic Dancer", "T-Rex")

    def test_song_has_name(self):
        self.assertEqual("Friday I'm In Love", self.song_1.name)

    def test_song_has_artist(self):
        self.assertEqual("The Cure", self.song_1.artist)