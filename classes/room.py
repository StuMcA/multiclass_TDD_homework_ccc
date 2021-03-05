class Room:
    
    def __init__(self, name):
        self.name = name
        self.guests = []
        self.playlist = []

    def add_song_to_playlist(self, song):
        self.playlist.append(song)